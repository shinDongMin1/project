"""
numpy 배열 조작에 관계된 함수 혹은 메서드
NumPy Link : https://docs.scipy.org/doc/numpy/index.html

    0. arrange: 연속적인 원소로 이루어진 1차원 배열을 반환한다.
    1. reshape: shape를 지정한 대로 바꾸어 반환한다. 데이터를 원본과 공유한다.
    2. resize: 원본 자체의 모양을 바꾼다. 반환 값이 없다.
    3. ravel: 임의의 배열을 1차원 배열로 만들어 반환한다. 데이터를 원본과 공유한다.
    4. flatten: 임의의 배열을 1차원 배열로 만들어 반환한다. ravel과는 달리 데이터를 원본과 공유하지 않는다.

"""

import numpy as np


"""
# slicing operation
a = np.arange(1, 10, 0.5)       # start, stop, step
print(a.shape)

b = a[0:4]
print(b)

b = a[4:]
print(b)

exit()
"""

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

    # 한 원소를 표현하기 위해 필요한 데이터의 바이트 수
    print(f"{str_a}.itemsize={a.itemsize}")

    # array에 들어 있는 총 원소의 수
    print(f"{str_a}.size={a.size}\n")



"""
#--------------------------------------------------------------------------
# 실습 1: NumPy에서 제공하는 arange 함수, reshape 메서드를 활용한 연습
#
# numpy.arange([start, ]stop, [step, ]dtype=None)
#   start부터 stop까지 step의 증분으로 순차적으로 증가/감소하는 1차원 배열을 반환한다. 데이터형은 dtype로 주어진다.
#   https://numpy.org/doc/stable/reference/generated/numpy.arange.html
#
# 
# numpy.reshape(a, newshape, order='C')
#   https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html?highlight=reshape#numpy.reshape
# 기능: 해당 어레이에 대해 shape가 다른 뷰(View)를 생성한다.
# 특징:
#   가능한 복사해서 데이터를 생성한다고 하지만 배열의 데이터를 공유할 수 있다.
#   즉, b = a.reshape((2,3))을 수행하고 난 후 a를 수정하면 b도 같이 수정될 수도 있다. 
#   반환한 데이터의 배열이 연속성이 없을 수도 있다.
#   order='C' : C-like index order
#   원본 배열의 데이터를 공유하지 않는 새로운 복사본을 만들고 싶으면 ndarray.copy 메서드를 사용한다.
#--------------------------------------------------------------------------

a = np.arange(5)    # 0~4까지 1씩 증가하는 1차원 어레이 생성
print_att('a')
# a=[0 1 2 3 4]
# type(a)=<class 'numpy.ndarray'>
# a.shape=(5,)
# a.ndim=1
# a.dtype=int32
# a.itemsize=4
# a.size=5


b = np.arange(5).reshape(1, 5)     # row*column = 1*5. ndim= 2. a= [[0 1 2 3 4]]
print_att('b')
# b=[[0 1 2 3 4]]
# type(b)=<class 'numpy.ndarray'>
# b.shape=(1, 5)
# b.ndim=2
# b.dtype=int32
# b.itemsize=4
# b.size=5

c = np.arange(15).reshape(3, 5)     # row*column = 3*5. ndim= 2
print_att('c')
# c=[[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]
# type(c)=<class 'numpy.ndarray'>
# c.shape=(3, 5)
# c.ndim=2
# c.dtype=int32
# c.itemsize=4
# c.size=15

exit(0)
"""


"""
#--------------------------------------------------------------------------
# 실습 2 - reshape, resize, ravel, flatten 연습
#     1. reshape: shape를 지정한 대로 바꾸어 반환한다. 데이터를 원본과 공유한다.
#     2. resize: 원본 자체의 모양을 바꾼다. 반환 값이 없다. 그래서, 원본과 데이터를 공유하지 않는다.
#     3. ravel: 임의의 배열을 1차원 배열로 만들어 반환한다. 데이터를 원본과 공유한다.
#     4. flatten: 임의의 배열을 1차원 배열로 만들어 반환한다. ravel과는 달리 데이터를 원본과 공유하지 않는다.
#--------------------------------------------------------------------------

print('\n사례 1 ----- reshape()를 사용하여 원본 A의 모양을 바꾼 바꾼 경우. 바뀐 객체 B는 A와 자료를 공유한다.')
n1 = 3; n2 = 2
A = np.arange(n1 * n2)
print("A =", A)
# A = [0 1 2 3 4 5]

B = A.reshape(n1, n2)       # 3x2 array로 변환
print("B =\n", B)
# B =
#  [[0 1]
#  [2 3]
#  [4 5]]

# 다른 배열의 데이터를 공유하고 있는 뷰라면 해당 배열이 출력됩니다.
print("A.base =", A.base)      # A는 자체 생성하였으므로 base는 다른 객체를 지정하지 않는다.
# A.base = None

print("B.base =", B.base)  # 배열 B의 base를 출력한다. 어떤 값을 참조하는지 보인다.
# B.base = [0 1 2 3 4 5]       다른 객체를 지정한다.

# B.base와 A가 동일한 객체인지 확인해봅니다.
if B.base is A:  # is는 똑같은 객체인지 확인할 때 사용합니다.
    print("B는 A의 데이터를 공유한다.")
# 출력: B는 A의 데이터를 공유한다.

# A를 수정했는데 B도 같이 바뀌었다.
A[0] = 100
print("A =\n", A)
print("B =\n", B)
# B.base = [100   1   2   3   4   5]


print(f"참고: id(A) = {id(A)}, id(B) = {id(B)}")
# id(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 파이썬 함수이다.
# 같은 객체를 가리킨다면 id도 같을 것이다.
# id는 다르다.
# id(A) = 2160717135104, id(B) = 2161101985632
# base는 파이썬의 id()와 유사한 역할을 수행하는 numpy의 메서드이다.

A[0] = 9                    # A를 바꾸었는데 B의 내용도 같이 변한다.
print("B =\n", B)           # B[0]도 바뀐다.
# B =
#  [[9 1]
#  [2 3]
#  [4 5]]


print('\n사례 2 ------- copy()를 사용하여 객체를 복사할 경우. 자료가 copy되어 새로운 객체가 생성된다.')
A = np.arange(n1 * n2)
B = A.reshape(n1, n2).copy()        # 3x2 array로 변환한 후 copy()하여 객체 B를 생성한다.

print("A.base =", A.base)          # 자체 생성
# A.base = None

print("B.base =", B.base)          # 자체 생성
# B.base = None

if B.base is A:
    print("B는 A의 데이터를 공유한다.")
else:
    print("B는 A의 데이터를 공유하지 않는다.")
# 출력: B는 A의 데이터를 공유하지 않는다.

A[0] = 9                      # A를 바꾸어도 B는 바뀌지 않는다.
print("B =\n", B)
# B =
#  [[0 1]               B[0]가 바뀌지 않았다.
#  [2 3]
#  [4 5]]


print('\n사례 3 ---------- 원본 자체의 모양을 바꾸는 메서드 resize()')
C = A.resize(n2, n1)        # resize메서드는 반환 값이 없음에 유의. n1 = 3; n2 = 2
print("A =\n", A)           # resize는 해당 어레이의 원본 자체를 수정하여 크기를 조정한다.
# A =
#  [[9 1 2]
#  [3 4 5]]

print("C =\n", C)           # resize()에서는 반환하는 값이 없다. 원본 객체를 바꾼다.
# C =
#  None



print('\n사례 4 ------------ ravel: n차 배열을 1차원 배열로 만들어 반환한다. 데이터는 원본과 공유한다.')
AA = B.ravel()                    # AA는 B를 공유.
print("AA =", AA)
# AA = [0 1 2 3 4 5]
AA[0] = 100
print("AA.base =\n", AA.base)    # 공유하므로 base는 B의 위치에 있는 값을 가리킨다.
# AA.base =
# [[100 1]
#  [2 3]
#  [4 5]]
print("B.base =", B.base)
# B.base = None
print('B=\n', B)
# B=
#  [[100   1]
#  [  2   3]
#  [  4   5]]

# ravel() 메서드를 4차원 데이터에 적용해 본다.
AA.resize([n1, n2, 1, 1])     # n1 = 3; n2 = 2. 4차원으로 만들어 본다.
print(f'AA.shape={AA.shape}, AA.ndim={AA.ndim}')
CC = AA.ravel()         # ravel()은 차원을 가리지 않고 1차원으로 만든다.
print(f'CC.shape={CC.shape}', CC)


print('\n사례 5 ------------ flatten: n차 배열을 1차원 배열로 만들어 반환한다.\
 ravel()과는 달리 반환 값은 원본과 데이터를 공유하지 않는다.')
AA = B.flatten()                    #
print("AA =", AA)
# AA = [100 1 2 3 4 5]
print("AA.base =", AA.base)    # 공유하지 않고 새로 생성된 개체이기 때문에 base는 None의 값을 갖는다.
# AA.base = None
AA[0] = -1
print(f'AA=\n{AA}')
# [-1  1  2  3  4  5]
print(f'B=\n{B}')               # 공유하지 않기 때문에 A를 바꾸었다고 같이 바뀌지는 않는다.
# [[100   1]
#  [  2   3]
#  [  4   5]]
exit(0)
"""



"""
# ---------------------------------------------------------------------------------------
# 실습 3: reshape() 메서드의 응용 고급,  advanced topic
# ---------------------------------------------------------------------------------------

print("실습 3: reshape() 메서드 응용 고급")
# reshape() 함수는 지정한 크기로 재배열하는 함수이다.
r = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
print(f'\n1) r.shape={r.shape}, r=\n{r}')
r43 = np.reshape(r, (4, 3))

# 여기서 파라미터가 -1로 지정될 때가 있는데 이것의 의미는 다음과 같다.
# One shape dimension can be -1.
# In this case, the value is inferred from the length of the array and remaining dimensions.
# 즉, -1이 아닌 배열을 먼저 구성한 다음에 남은 원소로 나머지 배열을 이루라는 뜻이다.

rv = np.reshape(r, (-1, 1))     # X x 1 어레이. 12개의 원소이므로 (12x1)이 된다.
print(f'\n2) rv.shape={rv.shape}, rv=\n{rv}')
# rv.shape=(12, 1), rv=
# [[ 1]
#  [ 2]
#  [ 3]
#  [ 4]
#  [ 5]
#  [ 6]
#  [ 7]
#  [ 8]
#  [ 9]
#  [10]
#  [11]
#  [12]]

r1 = np.reshape(r, (1, -1))     # 1 x X 어레이. 12개의 원소이므로 (1x12)이 된다.
print(f'\n3) r1.shape={r1.shape}, r1=\n{r1}')
# r1.shape=(1, 12), r1=
# [[ 1  2  3  4  5  6  7  8  9 10 11 12]]

r2 = np.reshape(r, (2, 3, -1))     # (2, 3) 어레이로 총 12개의 원소가 되려면 (2, 3) 어레이가 2개ㅔ 있어야 한다.
print(f'\n4) r2.shape={r2.shape}, r2=\n{r2}')
# r2.shape=(2, 3, 2), r2=
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]
#
# [[ 7  8]
#   [ 9 10]
#   [11 12]]]

print(f'\n5) reshape(i, -1)에서 i=1, 2, 3, 4, 6 일 때의 반환 값을 살펴본다.')
for i in [1, 2, 3, 4, 6]:
    rr = r.reshape(i, -1)
    print(f'\nr.reshape({i}, -1): ', rr.shape, '\n', rr)

exit(0)
"""


# ---------------------------------------------------------------------------------------
# 실습 4: squeeze()함수, advanced topic
# squeeze() 함수는 어레이의 디멘전을 가장 최소화하여 표현할 수 있는 수준으로 줄인다.
# ---------------------------------------------------------------------------------------


print("실습 4: squeeze() 함수")
a0 = np.array([[1, 2, 3], [4, 5, 6]])       # 가장 필수적인 정보: (2, 3)
# a0.shape=(2, 3), a0=
# [[1 2 3]
#  [4 5 6]]
# after squeezing: sq.shape(2, 3)

a1 = np.array([[[1, 2, 3], [4, 5, 6]]])     # 가장 필수적인 정보: (2, 3)
# a1.shape=(1, 2, 3), a1=
# [[[1 2 3]
#   [4 5 6]]]
# after squeezing: sq.shape(2, 3)

a2 = np.array([[[[1], [4]]]])               # 가장 필수적인 정보: (2,)
# a2.shape=(1, 1, 2, 1), a2=
# [[[[1]
#    [4]]]]
# after squeezing: sq.shape(2,)

a3 = np.array([[[[1, 1]]]])                 # 가장 필수적인 정보: (2,)
# a3.shape=(1, 1, 1, 2), a3=
# [[[[1 1]]]]
# after squeezing: sq.shape(2,)

a4 = np.array([[[[5.0]]]])                  # 가장 필수적인 정보: (). 스칼라
# a4.shape=(1, 1, 1, 1), a4=
# [[[[5.]]]]
# after squeezing: sq.shape()
print("===  ", np.squeeze(a4), type(np.squeeze(a4)), 100+np.squeeze(a4))    # ===   5.0 <class 'numpy.ndarray'> 105.0


a5 = np.array([[3.0]])                      # 가장 필수적인 정보: (). 스칼라
for i, v in enumerate([a0, a1, a2, a3, a4, a5]):    # enumerate()는 인덱스, i와 값(v)를 반환한다.
    print(f'\na{i}.shape={v.shape}, a{i}=\n{v}')
    sq = np.squeeze(v)
    print(f'after squeezing: sq.shape{sq.shape}')

print("\nsqueeze details of last data, a5 ----- '")
print_att('sq')
exit(0)



