"""

1 Dimensional Array Creation & vector Array Creation
- numpy.array 함수를 이용하여 ndarray 타입의 1차원 행렬을 생성한다.
참고: 1xN 행렬은 row vector라고 칭하고, Nx1 행렬은 column vector라고 행한다.
     이들은 numpy에서는 2차원 행렬이다.

Python의 1차원 배열, data sequence : 예, list = [1, 2, 3, 4]
파이썬의 data sequence와 같은 행렬의 shape=(N,)이다. 이들은 1차원 배열이다.

Sequences allow you to store multiple values in an organized and efficient fashion.
There are several sequence types: strings, Unicode strings, lists, tuples, bytearrays, and range objects
Dictionaries and sets are containers for non-sequential data.
From the official Python Docs:
- Strings are immutable sequences of Unicode code points.
- Lists are mutable sequences, typically used to store collections of homogeneous items.
- Tuples are immutable sequences, typically used to store collections of heterogeneous data
    (such as the 2-tuples produced by the enumerate() built-in).
- Bytearray objects are mutable, they support the mutable sequence operations
    in addition to the common bytes and bytearray operations
- The range type represents an immutable sequence of numbers and is commonly used
    for looping a specific number of times in for loops.

"""

import numpy as np

# ---------------------------------------------------------------------------------------------
# print_att()
#   입력 파라미터 변수(ndarray)에 대한 정보를 출력하는 함수
#   입력 파라미터는 변수의 스트링을 취한다.
# ---------------------------------------------------------------------------------------------


def print_att(str_a):

    # str_a를 스트링으로 간주하고 실제 값을 evaluate 한다.
    a = eval(str_a)
    print(f"{str_a}={a}")

    # type(): 자료형을 반환한다.
    print(f"type({str_a})={type(a)}")

    # shape: 행렬의 모양(행x열)을 지정하는 멤버변수
    print(f"{str_a}.shape={a.shape}")

    # ndim: 행렬의 차원을 지정하는 멤버변수
    print(f"{str_a}.ndim={a.ndim}")

    # dtype: 행렬의 원소의 데이터형을 지정하는 멤버변수. 행렬은 모두 같은 데이터형으로 구성된다.
    print(f"{str_a}.dtype={a.dtype}")

    # itemsize: 한 원소를 표현하기 위해 필요한 데이터의 바이트 수
    print(f"{str_a}.itemsize={a.itemsize}")

    # size: array에 들어 있는 총 원소의 수
    print(f"{str_a}.size={a.size}")

    # 추가: 1차원이면 len() 함수로 원소의 수를 셀 수 있다.
    if a.ndim == 1:
        print(f'number of elements={len(a)}')

    print()


#"""
# --------------------------------------------------------------------------------------------------
# 실습 1: 매트릭스 곱셈연산. 매트릭스 곱셈 연산자 = @ 
# 1) M1.shape= (n1, m1), M2.shape= (n2, m2)일 때 
#   MM = M1 @ M2 연산의 결과의 shape는?: MM.shape = (n1, m1) x (n2, m2) = (n1, m2).  m1 = n2 이어야 한다.     
# 2) row vector는 1xN 매트릭스이다. column vector는 Nx1 매트릭스이다. 이들의 연산을 살펴본다. 
# --------------------------------------------------------------------------------------------------

# 1차원 sequence 데이터 선언
parm = [2, 3, 4]; r = np.array(parm)       # []가 인자안에 추가되었음을 유의!!!
print_att('r')
# r=[2 3 4]
# type(r)=<class 'numpy.ndarray'>
# r.shape=(3,)
# r.ndim=1
# r.dtype=int32
# r.itemsize=4
# r.size=3
# number of elements=3


# 1) row vector를 생성한다. r.shape=(1,3)
print("\n1) 2차원 row vector를 생성한다. r.shape=(1,3)")
parm = [2, 3, 4]; r = np.array([parm])       # []가 인자안에 추가되었음을 유의!!!
#parm = [[2, 3, 4]]; r = np.array(parm)      # 읫 줄과 같은 선언.
print_att('r')

# ===========> 출력 결과
# r=[[2 3 4]]
# type(r)=<class 'numpy.ndarray'>
# r.shape=(1, 3)
# r.ndim=2
# r.dtype=int32
# r.itemsize=4
# r.size=3

# 2) column vector를 생성한다. c.shape=(3, 1)
print("2) column vector를 생성한다. c.shape=(3, 1)")
parm = [[2.0], [3], [4]]      # column vector 생성용
c = np.array(parm)
print_att('c')

# ===========> 출력 결과
# c=[[2.]
#  [3.]
#  [4.]]
# type(c)=<class 'numpy.ndarray'>
# c.shape=(3, 1)
# c.ndim=2
# c.dtype=float64
# c.itemsize=8
# c.size=3



# 3) matrix multiplication, m = c @ r:  (3x1) @ (1x3) => 3x3 matrix
print("3) matrix multiplication, m = c @ r:  (3x1) @ (1x3) => 3x3 matrix")
m = c @ r
print_att('m')

# ===========> 출력 결과
# m=[[ 4.  6.  8.]
#  [ 6.  9. 12.]
#  [ 8. 12. 16.]]
# type(m)=<class 'numpy.ndarray'>
# m.shape=(3, 3)
# m.ndim=2
# m.dtype=float64
# m.itemsize=8
# m.size=9


# 4) matrix multiplication, s = r @ c: (1x3) @ (3x1) => 1x1 matrix, should be scalar
# numpy에서는 1x1 행렬을 2차원으로 간주한다.
print("4) matrix multiplication, s = r @ c: (1x3) @ (3x1) => 1x1 matrix")
print("스칼라 값을 반환해야 하지만 실제로는 1x1 매트릭스 형태로 반환한다.")
s = r @ c
print_att('s')

# ===========> 출력 결과
# s=[[29.]]
# type(s)=<class 'numpy.ndarray'>
# s.shape=(1, 1)
# s.ndim=2
# s.dtype=float64
# s.itemsize=8
# s.size=1


# 5) matrix multiplication, cc = m @ c: (2x2) @ (2x1) => 2x1 matrix
print("5) matrix multiplication, cc = m @ c: (2x2) @ (2x1) => 2x1 matrix")
m = np.array([[1, 10], [1, 1]])
c = np.array([[1], [1]])
cc = m @ c
print_att('cc')
# cc=[[11]
#  [ 2]]
# type(cc)=<class 'numpy.ndarray'>
# cc.shape=(2, 1)
# cc.ndim=2
# cc.dtype=int32
# cc.itemsize=4
# cc.size=2

exit(0)

#"""




#"""
# --------------------------------------------------------------------------------------------------
# 실습 2: 1차원 매트릭스.
# n개의 원소를 갖는 1차원 매트릭스, a의 shape는 a.shape=(n,)이다.
#   참고: python의 sequence 자료형과 유사. string, list, tuple은 sequence 자료형이라 한다.
#        그러나, 연산에 있어서는 sequence 자료형과 다른다.
#           사례:  sequence 자료형에 대한 +연산은 python에서는 concatenation으로 실현되지만, numpy에서는 각 요소에 대한 개별 덧셉으로 이루어진다.
# a.shape=(3,)      # 1x3 row vector가 아니라, 1차원 row vector이다..
# a.ndim=1          # 1차원 matrix이다.
#
# numpy에서는;
#   배열의 방향성이 있는, 즉 row/column 벡터는 2차원 매트릭스이다.
#       shape = (1, n): 2차원 matrix, row vector
#       shape = (n, 1): 2차원 matrix, column vector
#   1차원 데이터 배열은 그 방향성은 없다.
#       shape=(n,): 1차원 매트릭스, 방향이 없으므로 아래의 (1, n)/(n, 1) 매트릭스가 사용되는 연산에 사용할 수 있다.
#       1차원 배열은 len() 함수를 이용해 그 원소의 개수를 셀 수 있다.
#
# parm = ((1, 2, 3))      # (3,) array. 1차원
# parm = (1, 2, 3)      # (3,) array. 1차원
# parm = [1, 2, 3]      # (3,) array. 1차원
# parm = [[1, 2, 3]]      # (1, 3) array. 2차원
# parm = [(1, 2, 3)]      # (1, 3) array. 2차원
# parm = [((1, 2, 3))]      # (1, 3) array. 2차원
# --------------------------------------------------------------------------------------------------

# 1) 1차원 매트릭스 선언
print("1) 1차원 매트릭스 선언")
parm = [2, 3, 4]            # a.dtype=int32, a.itemsize=4
a = np.array(parm)
print_att('a')
# a=[2 3 4]
# type(a)=<class 'numpy.ndarray'>
# a.shape=(3,)          # 1x3 row vector가 아님에 유의. 그러나 대개의 경우 큰 무리없이 활용가능하다.
# 1x3 혹은 3x1벡터가 필요한 곳에 (3,) sequence를 활용가능하다.
# a.ndim=1
# a.dtype=int32
# a.itemsize=4
# a.size=3
# number of elements=3

# 3) 1차원 매트릭스는 치환행렬을 취해도 그 내용이 변하지 않는다. 방향이 없기 때문이다..
print("3) 1차원 매트릭스는 치환행렬을 취해도 그 내용이 변하지 않는다. 방향이 없기 때문이다..")
a_T = a.T            # a_T=a.transpose() 도 같은 표현이다.
print_att('a_T')
# a_T=[2 3 4]           # transpose가 전의 값, 형식이 같다.
# type(a_T)=<class 'numpy.ndarray'>
# a_T.shape=(3,)        # 3x1 column vector가 아님에 유의.
# a_T.ndim=1
# a_T.dtype=int32
# a_T.itemsize=4
# a_T.size=3
# number of elements=3

# 3) 1차원 매트릭스의 더하기 '+' 연산: 각 원소끼리 더한다. 두 원소의 shape가 같아야 한다.
print("3) 1차원 매트릭스의 더하기 '+' 연산: 각 원소끼리 더한다. 두 원소의 shape가 같아야 한다.")
b = np.array((2, 3.1, 40)) + np.array([2, 3, 4])
print_att('b')
# b=[ 4.   6.1 44. ]
# type(b)=<class 'numpy.ndarray'>
# b.shape=(3,)
# b.ndim=1
# b.dtype=float64
# b.itemsize=8
# b.size=3
# number of elements=3


print("4.1) 1차원 매트릭스들의 원소끼리 곱하기 '*' 연산: 두 변수의 shape가 같아야 한다.")
a = np.array([1, 2, 3])
c1 = a * a
print_att('c1')
# c1=[1 4 9]
# type(c1)=<class 'numpy.ndarray'>
# c1.shape=(3,)
# c1.ndim=1
# c1.dtype=int32
# c1.itemsize=4
# c1.size=3
# number of elements=3


print("4.2) 특이 사례: 1차원 매트릭스들의 '@' 연산: row vector @ column vector = (1, n) @ (n, 1)로 간주.")
print('(1 x n) @ (n x 1)의 매트릭스 연산으로 간주하여 스칼라 값(ndim=0)을 반환한다.')
c2 = a @ a
print_att('c2')
# c2=14
# type(c2)=<class 'numpy.int32'>
# c2.shape=()
# c2.ndim=0
# c2.dtype=int32
# c2.itemsize=4
# c2.size=1


# 5) 비고: 파이썬 sequence 데이터에 대한 '+' 연산. concatenation이 이루어진다. 원소의 개수가 달라도 된다.
# d = a * b      # 이 연산은 불가...
print("5) 비고: 파이썬 sequence 데이터에 대한 '+' 연산. concatenation이 이루어진다. 원소의 개수가 달라도 된다.")
a = [1, 2, 3]; b = [4, 5]
c = a + b
print(type(c), c)
# <class 'list'> [1, 2, 3, 4, 5]


# 6) 비고: np.arange() 함수는 shape=(n,)인 1차원 매트릭스를 생성한다.
print()
print("6) 비고: np.arange() 함수가 shape=(n,)인 1차원 매트릭스를 생성한다.")
a = np.arange(start=2, stop=5, step=1, dtype=None)
a = np.arange(5)
print_att('a')
# a=[0 1 2 3 4]
# type(a)=<class 'numpy.ndarray'>
# a.shape=(5,)
# a.ndim=1
# a.dtype=int32
# a.itemsize=4
# a.size=5


# 7) 특이 사례: c = a @ b: (2x2) @ (2,) => (2x2) @ (2,1) => (2x1) => transpose & dimension => (2,)
# 중요한 연산 아니므로 입문자는 pass 권유..
# 수학적으로는 불완전하지만, 연산 편의를 위해 특별히 제공하는 기능으로 보인다.
print('\n7) 특이 사례: c = a @ b: (2x2) @ (2,) => (2x2) @ (2,1) => (2x1) => transpose & dimension => (2,)')
a = np.array([[1, 2], [3, 4]])
print(f'a.shape={a.shape}, a=\n{a}')
b = np.array([10, 20])
print(f'b.shape={b.shape}, b=\n{b}')
c = a @ b
print(f'c=a @ b: c.shape={b.shape}, c=\n{c}')
# a.shape=(2, 2), a=
# [[1 2]
#  [3 4]]
# b.shape=(2,), b=
# [10 20]
# c=a @ b: c.shape=(2,), c=
# [ 50 110]

exit(0)


