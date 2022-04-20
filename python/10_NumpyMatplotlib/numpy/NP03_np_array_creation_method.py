"""
 Numpy의 ndarray 자료 생성 함수
   numpy에서 제공하는 함수 - 원하는 차원과 원소 값으로 ndarray를 생성한다.
    zeros : Return a new array setting values to zero.
    ones :  Return a new array setting values to one.03_
    empty : Return a new uninitialized array.
    full : Return a new array of given shape filled with value.
    full_like : Return a new array with shape of input filled with value.
    empty_like : Return an empty array with shape and type of input.
    ones_like : Return an array of ones with shape and type of input.
    zeros_like : Return an array of zeros with shape and type of input.

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

    # 한 원소를 표현하기 위해 필요한 데이터의 바이트 수
    print(f"{str_a}.itemsize={a.itemsize}")

    # array에 들어 있는 총 원소의 수
    print(f"{str_a}.size={a.size}\n")



# ---------------------------------------------------------------------------------------------
# 1) np.zeros((n,m)) 함수: 내부 원소 값이 모두 0인 n x m의 매트릭스 생성.
# ..................................
# zeros(shape, dtype=numpy.float64, order='C')
#   지정된 shape의 배열을 생성하고, 모든 요소를 0으로 초기화한다.
#   order='C' : Whether to store multi-dimensional data in row-major (C-style)
#               or column-major (Fortran-style) order in memory.
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html?highlight=zeros#numpy.zeros
# ---------------------------------------------------------------------------------------------

print("1) np.zeros((n,m)) 메소드: 내부 원소 값이 모두 0인 n x m의 매트릭스 생성.")
#Z = np.zeros((2,3))    # 내부 원소가 모두 0인 2x3 행렬 생성
Z = np.zeros([2, 3], dtype=np.int16)
print_att('Z')

# ===========> 출력 결과
# Z=[[0 0 0]
#  [0 0 0]]
# type(Z)=<class 'numpy.ndarray'>
# Z.shape=(2, 3)
# Z.ndim=2
# Z.dtype=int16
# Z.itemsize=2
# Z.size=6


# ---------------------------------------------------------------------------------------------
# 2) np.ones((n,m)) 함수: 내부 원소 값이 모두 1인 n x m의 매트릭스 생성.
# ..................................
# np.ones(shape, dtype=numpy.float64, order='C')
#   지정된 shape의 배열을 생성하고, 모든 요소를 1로 초기화한다.
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.ones.html?highlight=ones#numpy.ones
# ---------------------------------------------------------------------------------------------

print("2) np.ones((n,m)) 메소드: 내부 원소 값이 모두 1인 n x m의 매트릭스 생성.")
O = np.ones((3, 4), dtype=np.uint8)     # 내부 원소가 모두 1인 3x4 행렬 생성
print_att('O')

# ===========> 출력 결과
# O=[[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]
# type(O)=<class 'numpy.ndarray'>
# O.shape=(3, 4)
# O.ndim=2
# O.dtype=uint8
# O.itemsize=1
# O.size=12

print("2b) np.ones((n, )) 메소드: 내부 원소 값이 모두 1인 1차원 매트릭스 생성.")
Ob = np.ones((3, ), dtype=np.uint8)     # 내부 원소가 모두 1인 3x4 행렬 생성
print_att('Ob')
# 2b) np.ones((n, )) 메소드: 내부 원소 값이 모두 1인 1차원 매트릭스 생성.
# Ob=[1 1 1]
# type(Ob)=<class 'numpy.ndarray'>
# Ob.shape=(3,)
# Ob.ndim=1
# Ob.dtype=uint8
# Ob.itemsize=1
# Ob.size=3


# ---------------------------------------------------------------------------------------------
# 3) np.empty((n, m)) 함수: 내부 원소가 초기화되지 않은 n x m 행렬 생성
# ..................................
# empty(shape, dtype=numpy.float64, order='C')
#   지정된 shape의 배열을 생성한다. 
#   요소의 초기화 과정이 없어 배열 생성이 빠르다. 쓰레기 데이터 값 그대로 어레이가 선언된다.
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.empty.html?highlight=empty
# ---------------------------------------------------------------------------------------------

print("3) np.empty((n, m)) 메소드: 내부 원소가 초기화되지 않은 n x m 행렬 생성")
# 내부 원소가 초기화되지 않은 2x3 행렬 생성
E = np.empty((2, 3))   # uninitialized, output may vary
print_att('E')

# ===========> 출력 결과
# E=[[3.33772792e-307 4.22786102e-307 3.44899350e-307]
#  [2.44774252e-307 3.44900708e-307 4.05133830e-322]]
# type(E)=<class 'numpy.ndarray'>
# E.shape=(2, 3)
# E.ndim=2
# E.dtype=float64
# E.itemsize=8
# E.size=6


# ---------------------------------------------------------------------------------------------
# 4) np.full((n, m), value) 함수: 내부 원소 값을 value로 지정하여 n x m 행렬 생성
# ..................................
# full(shape, fill_value, dtype=None, order='C')
#   Return a new array of given shape and type, filled with fill_value.
#   The default, None, means np.array(fill_value).dtype.
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.full.html#numpy.full
# ---------------------------------------------------------------------------------------------
print("4) np.full((n, m), value) 메소드: 내부 원소 값을 value로 지정하여 n x m 행렬 생성")
F = np.full((2, 2), 10)       # 초기화하는 값으로 생성되는 데이터 타입이 정의된다.
print_att('F')

# ===========> 출력 결과
# F=[[10 10]
#  [10 10]]
# type(F)=<class 'numpy.ndarray'>
# F.shape=(2, 2)
# F.ndim=2
# F.dtype=int32
# F.itemsize=4
# F.size=4


# ---------------------------------------------------------------------------------------------
# 5) np.full_like(array, value) 함수: 샘플(사례)로 제시된 array와 같은 타입(크기, 데이터 타입)의
#   새로운 어레이를 생성하면서 특정값, value로 초기화를 행한다.
# ..................................
# full_like(a, fill_value, dtype=None, order='K', subok=True)
# Return a full array with the same shape and type as a given array.
# ---------------------------------------------------------------------------------------------
print("5) np.full_like(array, value) 메소드: 샘플(사례)로 제시된 array와 같은 타입(크기, 데이터 타입)의 새로운 어레이 반환")
x = np.arange(6, dtype=int)
print('\nnp.arange(6, dtype=int)=>', x)         # np.arange(6, dtype=int)=> [0 1 2 3 4 5]
L = np.full_like(x, 1.2)        # x와 같은 타입(크기, 데이터 타입)의 어레이를 선언하되 초기 값은 1이다.
print_att('L')

# ===========> 출력 결과
# L=[1 1 1 1 1 1]           # 초깃값을 1.2로 지정하였지만 int형이므로 1로 되었음을 유의.
# type(L)=<class 'numpy.ndarray'>
# L.shape=(6,)
# L.ndim=1
# L.dtype=int32
# L.itemsize=4
# L.size=6

L2 = np.full_like(x, 2.7)     # X가 int이므로 2.7도 정수로 간주된다.
print_att('L2')

# ===========> 출력 결과
# L2=[2 2 2 2 2 2]
# type(L2)=<class 'numpy.ndarray'>
# L2.shape=(6,)
# L2.ndim=1
# L2.dtype=int32
# L2.itemsize=4
# L2.size=6

x = np.arange(6, dtype=float)       #  이것을 사용하면 L3가 정상 생성될 것이다.
L3 = np.full_like(x, 2.1)
print_att('L3')

# ===========> 출력 결과
# L3=[2.1 2.1 2.1 2.1 2.1 2.1]
# type(L3)=<class 'numpy.ndarray'>
# L3.shape=(6,)
# L3.ndim=1
# L3.dtype=float64
# L3.itemsize=8
# L3.size=6



# ---------------------------------------------------------------------------------------------
# 6) np.empty_like(array) 함수: 샘플(사례)로 제시된 array와 같은 타입(크기, 데이터 타입)의
#   새로운 어레이를 생성하면서 초기화는 행하지 않는다.
# ---------------------------------------------------------------------------------------------
print("6) np.empty_like(array) 메소드: array와 같은 타입(크기, 데이터 타입)의 최기화하지 않은 새로운 어레이 반환")
xx = np.ones((2, 3))
L4a = np.empty_like(xx, dtype='uint8')
print_att('L4a')

L4b = np.empty_like(xx, dtype='float')
print_att('L4b')

exit(0)
