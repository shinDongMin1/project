"""
실습 1: 두 행렬의 각 원소별 가감산 및 논리 연산 등..
실습 2 - 행렬의 원소의 min/max/sum/average를 numpy 함수로 구하기, 난수 어레이에 대한 기본 연산
실습 3 - linspace(start, stop, num): 시작점부터 종ㅛ지점까지를 num 단계로 나눈 ndarray를 반환한다.
        양쪽 단의 경계 값을 포함한다.
실습 4 - universal functions, exp, sqrt

"""

import numpy as np

# ---------------------------------------------------------------------------------------------
# print_n_att()
#   출력문의 번호를 먼저 프린트 한 후,
#   입력 파라미터 변수(ndarray)에 대한 정보를 출력한다.
#   입력 파라미터는 변수의 스트링을 취한다.
# ---------------------------------------------------------------------------------------------


def print_n_att(num, str_a):
    print()
    print(num)

    # str_a를 스트링으로 간주하고 실제 값을 evaluate 한다.
    a = eval(str_a)
    print(f"\n{str_a}={a}")

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


def print_simple(num, str_a):        # num = 실험 번호 스트링, str_a = 변수 스트링
    print()
    a = eval(str_a)
    print("{} {}={}".format(num, str_a, a))
    print("type({})={}".format(str_a, type(a)))
    print("{}.shape={}".format(str_a, a.shape), end='    ')
    print("{}.dtype={}".format(str_a, a.dtype))


def print_n(num, str_a):           # num=실험 번호, str_a = 객체를 지정하는 스트링
    print()
    a = eval(str_a)
    print("{}) {}={}".format(num, str_a, a))
    print("{}.shape={}".format(str_a, a.shape), end='    ')
    print(" {}.dtype={}".format(str_a, a.dtype))


#"""
#--------------------------------------------------------------------------
# 실습 1: 두 행렬의 각 원소별 가감산 및 논리 연산 등..
#--------------------------------------------------------------------------
a = np.array([20, 30, 40, 50])
b = np.arange(4, dtype=float)

print_simple('1)', 'a')
# 1) a=[20 30 40 50]
# type(a)=<class 'numpy.ndarray'>
# a.shape=(4,)    a.dtype=int32

print_simple('2)', 'b')
# 2) b=[0. 1. 2. 3.]
# type(b)=<class 'numpy.ndarray'>
# b.shape=(4,)    b.dtype=float64

c = a + b
print_n(3, 'c')
# 3) c=[20. 31. 42. 53.]
# c.shape=(4,)     c.dtype=float64

d = a ** 2      # element-wise square
print_n(4, 'd')
# 4) d=[ 400  900 1600 2500]
# d.shape=(4,)     d.dtype=int32

s = 10 * np.sin(a)      # scalar multiplication. np.sin()함수는 어레이의 각 요소에 대해 sin()을 취한 결과를 어레이로 반환한다.
print_n(5, 's')
# 5) s=[ 9.12945251 -9.88031624  7.4511316  -2.62374854]
# s.shape=(4,)     s.dtype=float64

v1 = a > 35       # greater than. a=[20 30 40 50]
# 어레이에 대한 로직 연산은 어레이로 구성된 bool 값을 반환한다. 결과 값 v1도 ndarray 자료형.
print_n_att('6) Grater than', 'v1')
print('a=', a)
# 6) Grater than
# v1=[False False  True  True]
# type(v1)=<class 'numpy.ndarray'>
# v1.shape=(4,)    v1.ndim=1
# v1.dtype=bool    v1.itemsize=1    v1.size=4


v2 = [1, 0, 1, 0]   # v2는 list
print('type(v2)=', type(v2), 'v2=', v2)
# type(v2)= <class 'list'>

v = v1 & v2     # Logical AND. v1=[False False  True  True]
# ndarray와 list간의 연산이 가능하다. 연산 결과는 ndarray, dtype=int32 이다.
print_n_att('7) v = v1 & v2', 'v')
# 7) v = v1 & v2
# v=[0 0 1 0]
# type(v)=<class 'numpy.ndarray'>
# v.shape=(4,)    v.ndim=1
# v.dtype=int32    v.itemsize=4    v.size=4

v3 = [True, False, True, False]   # v1=[False False  True  True]
v = v1 & v3     # Logical AND. ndarray와 list간의 연산이 가능하다. 연산 결과는 ndarray, dtype=bool 이다.
print_n_att('8) v = v1 & v3', 'v')
# 8) v = v1 & v3
# v=[False False  True False]
# type(v)=<class 'numpy.ndarray'>
# v.shape=(4,)    v.ndim=1
# v.dtype=bool    v.itemsize=1    v.size=4

v = v1 | v3     # Logical OR. ndarray와 list간의 연산이 가능하다. 연산 결과는 bool 이다.
print_n_att('9) v = v1 | v3', 'v')
# 9) v = v1 | v3
# v=[ True False  True  True]
# type(v)=<class 'numpy.ndarray'>
# v.shape=(4,)    v.ndim=1
# v.dtype=bool    v.itemsize=1    v.size=4

# array_equal - 두 어레이가 모두 같은 값을 갖고 있는지 확인하는 함수
a = np.array([1, 2, 3, 4])
b = np.array([1.0, 2.0, 3.0, 4.0])
c = np.array([1.0, 2.0, 3.0, 4.01])
ab = np.array_equal(a, b)
print("\n10) array_equal(a, b)=", ab)
# array_equal(a, b)= True

ac = np.array_equal(a, c)
print("\n11) array_equal(a, c)=", ac)
# array_equal(a, c)= False

exit(0)
#"""



"""
#--------------------------------------------------------------------------
# 실습 2 - 행렬의 원소의 min/max/sum/average 구하기, 난수 어레이에 대한 기본 연산
#
# 참고: random 메소드 검색 방법
#       https://docs.scipy.org/doc/numpy/reference/routines.html 에서 random을 검색
#       검색된 메소드가 맨 위에 올라온다.
#
# average()
#   https://docs.scipy.org/doc/numpy/reference/generated/numpy.average.html?highlight=average#numpy.average
#--------------------------------------------------------------------------
b = np.random.random((100, 100))     # 0~1까지의 균일한 분포를 갖는 난수를 발생하여  100 x 100 어레이에 배정한다.
print_n(0, 'b') # ㅠsms 100 x 100의 어레이
# b.shape=(100, 100)     b.dtype=float64

print('1) b.max =', b.max(), ' np.amax(b)=', np.amax(b))    # max value. 10000개의 원소 중에 가장 큰 값.
print('2) b.min =', b.min(), ' np.amin(b)=', np.amin(b))    # min value. 10000개의 원소 중에 가장 작은 값.
print('3) b.sum =', b.sum(), ' np.sum(b)=', np.sum(b))  # sum value. 10000개의 원소들의 평균 값. 균일 분포이므로 5000에 가까운 값을 갖는다.
print('4) b.sum/b.size =', b.sum()/b.size)      # avg value. b.size는 원소의 개수.
print('5) np.average(b) =', np.average(b))      # avg value. 원소가 많을 수록 0.5 근처의 값을 가진다.

a = np.ones((2, 6), dtype=int)
a *= 3      # a = a*3
print_n('\n6', 'a')
# 6) a=[[3 3 3 3 3 3]
#  [3 3 3 3 3 3]]
# a.shape=(2, 6)     a.dtype=int32


b = np.random.random((2, 6))     # 0~1까지의 균일한 분포를 갖는 난수를 발생하여 어레이에 배정한다.
print_n('7', 'b')
# 7) b=[[0.82678395 0.17724314 0.77842821 0.57034831 0.99443973 0.33542468]
#  [0.95118171 0.49611969 0.89826231 0.08730827 0.7700454  0.3618515 ]]
# b.shape=(2, 6)     b.dtype=float64


b += a
print_n('8', 'b')
# 8) b=[[3.82678395 3.17724314 3.77842821 3.57034831 3.99443973 3.33542468]
#  [3.95118171 3.49611969 3.89826231 3.08730827 3.7700454  3.3618515 ]]
# b.shape=(2, 6)     b.dtype=float64


#a += b     # Error!!! b is not automatically converted to integer type
a = a + b   # 이것은 이상 없음.
print_n('9', 'a')
# 9) a=[[6.99100543 6.34942707 6.93232202 6.98464507 6.72567318 6.68008706]
#  [6.94506372 6.60858167 6.50497092 6.95599134 6.51161018 6.82064767]]
# a.shape=(2, 6)     a.dtype=float64

exit(0)
"""



"""
#--------------------------------------------------------------------------
# 실습 3 - linspace(start, stop, num): 시작점부터 중지점까지를 num 단계로 나눈 ndarray를 반환한다.
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# Return evenly spaced numbers over a specified interval.
# Returns num evenly spaced samples, calculated over the interval [start, stop].
# If dtype is not given, infer the data type from the other input arguments.
# The endpoint of the interval can optionally be excluded.
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace
#--------------------------------------------------------------------------

print("참고: 간격 =", 2/(9-1) )
# 참고: 간격 = 0.25

# 0~2까지를 9개로 나눈 어레이를 반환한다.
# 양쪽 경계가 모두 포함된다.
x = np.linspace(start=0, stop=2, num=9)
print_simple('1)', 'x')
# 1) x=[0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ]
# type(x)=<class 'numpy.ndarray'>
# x.shape=(9,)    x.dtype=float64

for i in x:     # x는 ndarray이지만 sequence data이다.
    print(i, end=' ')
print()

from numpy import pi
b = np.linspace(0, pi, 5)                 # 0~pi까지를 5개로 나눈다.
print_simple('2)', 'b')
# 2) b=[0.         0.78539816 1.57079633 2.35619449 3.14159265]
# type(b)=<class 'numpy.ndarray'>
# b.shape=(5,)    b.dtype=float64

exit(0)
"""



#--------------------------------------------------------------------------
# 실습 4 - universal functions, exp, sqrt
# NumPy provides familiar mathematical functions such as sin, cos, and exp.
# In NumPy, these are called “universal functions”(ufunc).
# Within NumPy, these functions operate elementwise on an array, producing an array as output.
#--------------------------------------------------------------------------
B = np.arange(3.0)
B = [[1.0, 2], [3, 4]]
B = np.array(B)
print_n('1', 'B')
# 1) B=[[1. 2.]
#  [3. 4.]]
# B.shape=(2, 2)     B.dtype=float64


eB = np.exp(B)        # exponential
print_n('2', 'eB')
# 2) eB=[[ 2.71828183  7.3890561 ]
#  [20.08553692 54.59815003]]
# eB.shape=(2, 2)     eB.dtype=float64


sB = np.sqrt(B)       # square root
print_n('3', 'sB')
# 3) sB=[[1.         1.41421356]
#  [1.73205081 2.        ]]
# sB.shape=(2, 2)     sB.dtype=float64


A = np.array([[1, 2], [3, 4]])
print_n('4', 'A')
# 4) A=[[1 2]
#  [3 4]]
# A.shape=(2, 2)     A.dtype=int32

B = np.array([[1.0, 2], [3, 4]])
print_n('5', 'B')
# 5) B=[[1. 2.]
#  [3. 4.]]
# B.shape=(2, 2)     B.dtype=float64


ApB = np.add(A, B )
print_n('6', 'ApB')
# 6) ApB=[[2. 4.]
#  [6. 8.]]
# ApB.shape=(2, 2)     ApB.dtype=float64

AmB = A - B
print_n('7', 'AmB')
# 7) AmB=[[0. 0.]
#  [0. 0.]]
# AmB.shape=(2, 2)     AmB.dtype=float64

Asq = A ** 2          # 제곱
print_n('8', 'Asq')
# 8) Asq=[[ 1  4]
#  [ 9 16]]
# Asq.shape=(2, 2)     Asq.dtype=int32

exit(0)





