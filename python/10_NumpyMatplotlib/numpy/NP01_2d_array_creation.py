"""
개요:
    2차원 매트릭스를 정의하고, 그 매트릭스가 갖는 속성을 멤버변수를 통해 확인

    아래 1)~6) 사례에서는 numpy.array() 함수에서 제공하는 매트릭스 정의 방법과 함수를 소개하고 있습니다.
        numpy.array() 함수로 선언한 변수는 ndarray class입니다.
        이 class가 제공하는 멤버변수는 다음과 같습니다.
            # shape: 행렬의 모양(행x열)을 지정하는 멤버변수
            # ndim: 행렬의 차원을 지정하는 멤버변수
            # dtype: 행렬의 원소의 데이터형을 지정하는 멤버변수. 행렬은 모두 같은 데이터형으로 구성된다.
            # itemsize: 한 원소를 표현하기 위해 필요한 데이터의 바이트 수
            # size: array에 들어 있는 총 원소의 수

* Advanced Topics: 이 예제는 모든 Numpy의 모든 연습을 마친 다음에 도전해 보기 바랍니다.

참조 링크:
    numpy, matplotlib 한국어 문서 링크
        https://wikidocs.net/14569

    numpy 매뉴얼 다운로드 - PDF로 다운로드 받을 수 있음.
        https://numpy.org/doc/


#--------------------------------------------------------------------------
# 도움말 출력 - np.info() 함수
# info 함수는 ()안의 object 혹은 string에 관한 정보를 출력한다.
# 주의
# 1) 본 실험은 python console에서 실행하는 것이 더 바람직합니다.
# 2) 도움말이 길기 때문에 처음 사용할 때는 한 두가지만 해보기를 권장합니다.
# numpy에서 지원하는 함수, 메소드의 용법을 참조할 때는 아래 on-line 매뉴얼을 참조하자.
#   https://docs.scipy.org/doc/numpy/genindex.html
#--------------------------------------------------------------------------

np.info()               # info() 함수의 용법에 대한 도움말을 출력한다.
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html
np.info(np.array)       # array()함수의 용법을 출력한다.
np.info('zeros')        # zeros 함수의 용법을 출력한다. 스트링으로도 조회할 수 있다.
np.info(np.zeros)       # 위와 같이 zeros() 함수의 용법을 출력한다.
#help(np.zeros)         # 비교대상. 파이썬 고유의 Doc String(소스의 서두에 있는 따옴표 3개의 쌍으로 둘러싼 문장)을 출력한다.
np.info(np.reshape)     # reshape() 함수의 용법을 출력한다.

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
    print(f"\n{str_a}={a}")

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
    print(f"{str_a}.size={a.size}\n")


# --------------------------------------------------------------------------------------------------
# NxM Array Creation - numpy.array 함수를 이용하여 ndarray 타입의 2차원 어레이를 생성한다.
# 아래 예제에서는 NxM 어레이를 선언하고 함수를 사용하여 그 속성을 출력한다. N=row, M=column
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html?highlight=array#numpy.array
#
# numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
#   object : tuple, list 모두 가능하다. 한 어레이 선언에서 섞어 쓸 수 있다.
#       예) a = numpy.array(tuple) 혹은 a = numpy.array(list)
#       a = np.array(1,2,3,4)    # WRONG
#       => 올바른 방법 a = np.array((1,2,3,4)) 혹은 a = np.array( [1,2,3,4] )
#   dtype : 모든 원소는 같은 데이형 형으로 선언된다. 
#           제공되지 않으면 모든 원소를 수용할 수 있는 가능한 가장 작은 크기의 데이터 형으로 정의된다. 
#           하지만, 원소마다 데이터형이 서로 다르면 원소 중 가장 큰 데이터 형으로 통일된다.  
# --------------------------------------------------------------------------------------------------


#"""
# 1) 2x3 array 선언 => 어레이 선언은 차원을 증가시킬 때마다 []로 둘러싼다.
#obj1 = (((1, 2, 3), (4, 5, 6)))  # 2 x 3 array. 2차원.    불필요한 ()는 무시된다.
#obj1 = [[[1, 2, 3], [4, 5, 6]]]  # 1 x 2 x 3 array. 3차원. 그러나 []는 무시되지 않는다.
#obj1 = ((1, 2, 3), (4, 5, 6))  # 2 x 3 array. 2차원.
#obj1 = [(1, 2, 3), (4, 5, 6)]  # 2 x 3 array. 2차원.
#obj1 = ((1, 2, 3), [4, 5, 6])  # 2 x 3 array. 2차원.
obj1 = [[1, 2, 3], [4, 5, 6]]  # 2 x 3 array. 2차원. 1차원짜리 2개를 모아서 2차원으로 확장한 것으로 해석하자.....

a = np.array(obj1)  # array() 함수로 선언 => ndarray 생성
print_att('a')

# ===> 출력 결과
# a=[[1 2 3]
#  [4 5 6]]
# type(a)=<class 'numpy.ndarray'>   numpy로 선언한 객체는 ndarray 클래스이다.
# a.shape=(2, 3)        row x col
# a.ndim=2              2 dimension
# a.dtype=int32         각 요소의 데이터 타입. ndarray의 모든 원소(element)는 같은 데이터형
# a.itemsize=4          한 원소를 표현하는데 소요되는 바이트
# a.size=6              총 원소의 수
#exit(0)

# 2) indexing or slicing - list/tuple에서 사용하던 기법이 그대로 사용된다.
print(a[0][2])  # =[0,2] => 3
print(a[0, 2])  # =[0][2] => 3
print(a[1, 1])  # => 5
print(a[1, :-1])  # 1번 row, 처음부터 끝-1까지   => [4 5]
print(a[1, 0:])  # 1번 row, 처음부터 끝까지     => [4 5 6]
print(a[0, -1:])  # 0번 row, 끝부터 끝까지       => [3]
print(a[0, :])  # 0번 row, 모두               => [1 2 3]
print(a[0])  # 0번 row, 모두               => [1 2 3]
print(a[:, 0])  # 0번 col, 모두               => [1 4]

# 3) 데이터 타입을 지정하여 선언
b = np.array(obj1, dtype=float)  # 내부 요소를 float type으로 강제 배정한다.
b = np.array(obj1, dtype='uint8')
b = np.array(obj1, dtype='float32')
b = np.array(obj1, dtype=np.uint64)
b = np.array(obj1, dtype=np.uint8)
print_att('b')

# ===> 출력 결과(dtype=float)
# b=[[1. 2. 3.]
#  [4. 5. 6.]]
# type(b)=<class 'numpy.ndarray'>
# b.shape=(2, 3)
# b.ndim=2
# b.dtype=float64
# b.itemsize=8          float로 표현하면 double형의 데이터로 8바이트가 소요된다.
# b.size=6


# 4) 내부 원소 중 하나라도 부동소수가 있을 경우
obj2 = ([1.5, 2, 3], (4, 5, 6))  # c.dtype=float64
c = np.array(obj2)  # 내부 요소를 float type로 강제 배정한다.
print_att('c')

# ===> 출력 결과
# c=[[1.5 2.  3. ]
#  [4.  5.  6. ]]
# type(c)=<class 'numpy.ndarray'>
# c.shape=(2, 3)
# c.ndim=2
# c.dtype=float64
# c.itemsize=8
# c.size=6


# 5) 3x2 array 선언
#parm = (((1, 2), (3, 4), (5, 6)))
parm = [[1, 2], [3, 4], [5, 6]]
d = np.array(parm)
print_att('d')

# ===> 출력 결과
# d=[[1 2]
#  [3 4]
#  [5 6]]
# type(d)=<class 'numpy.ndarray'>
# d.shape=(3, 2)
# d.ndim=2
# d.dtype=int32
# d.itemsize=4
# d.size=6


# 6) transpose of a matrix -행과 열을 서로 교환한 변환
e = d.transpose()
#e = e.T
print_att('e')

# ===> 출력 결과
# e=[[1 2]
#  [3 4]
#  [5 6]]
# type(e)=<class 'numpy.ndarray'>
# e.shape=(3, 2)
# e.ndim=2
# e.dtype=int32
# e.itemsize=4
# e.size=6

exit(0)
#"""


# ---------------------------------------------------------------------------------------------
# advanced topics: 입문자는 pass 해도 좋습니다.
# ndarray의 각 요소(numeric value)는 모두 같은 타입이어야 하는 것으로 알려져 있다.
# 그래서, 여러 형(type)으로 정의되면 그들을 모두 담을 수 있는 제일 포괄적인 형으로 정의된다.
# 실험에 의하면 int와 float를 같이 쓰면 float형으로 정의된다.
#
# 위 서술이 일반적인 데이터형에 대해서는 맞는 이야기인데,
# 지나치게 자리를 많이 차지하는 데이터형에 대해서는 그렇지 않은 것으로 판단된다.
# 이 경우 dtype=object로 반환하고, 원소에 따라 데이터형을 다르게 배정한다.
# ---------------------------------------------------------------------------------------------

# 실험 1: 어레이의 모든 원소가 signed 64 bit의 정수로 나타내진 경우
# 2**63-1는 8바이트로 표시할 수 있는 signed int의 최대 값이다.
print("실험 1: 어레이의 모든 원소가 signed 64 bit의 정수로 나타내진 경우")
parm = ((1, 2**63-1), (3, -(2**63-1)))       #  -9223372036854775807
a = np.array(parm)
print_att('a')
# 1=[[                   1  9223372036854775807]
#  [                   3 -9223372036854775807]]
# type(a)=<class 'numpy.ndarray'>
# a.shape=(2, 2)
# a.ndim=2
# a.dtype=int64
# a.itemsize=8
# a.size=4

print(f"a[0, 0]={a[0, 0]}, type={type(a[0, 0])}")
print(f"a[0, 1]={a[0, 1]}, type={type(a[0, 1])}")
print(f"a[1, 0]={a[1, 0]}, type={type(a[1, 0])}")
print(f"a[1, 1]={a[1, 1]}, type={type(a[1, 1])}")
# a[0, 0]=1, type=<class 'numpy.int64'>
# a[0, 1]=9223372036854775807, type=<class 'numpy.int64'>
# a[1, 0]=3, type=<class 'numpy.int64'>
# a[1, 1]=-9223372036854775807, type=<class 'numpy.int64'>


# 실험 2: 서로 다른 형으로 어레이의 요소가 구성된 경우
# int64보다 더 큰 데이터는 8바이트의 object로 저장된다.
# 원래 python 자체가 64비트 이상의 정수형도 선언가능하며 이 경우토 type은 int이다.
print("\n\n실험 2: 서로 다른 형으로 어레이의 요소가 구성된 경우")
parm = ((1, 2**163), (3, 4.1))
a = np.array(parm)
print_att('a')
# a=[[1 11692013098647223345629478661730264157247460343808]
#  [3 4.1]]
# type(a)=<class 'numpy.ndarray'>
# a.shape=(2, 2)
# a.ndim=2
# a.dtype=object
# a.itemsize=8
# a.size=4

print(f"a[0, 0]={a[0, 0]}, type={type(a[0, 0])}")
print(f"a[0, 1]={a[0, 1]}, type={type(a[0, 1])}")
print(f"a[1, 0]={a[1, 0]}, type={type(a[1, 0])}")
print(f"a[1, 1]={a[1, 1]}, type={type(a[1, 1])}")
# a[0, 0]=1, type=<class 'int'>
# a[0, 1]=11692013098647223345629478661730264157247460343808, type=<class 'int'>
# a[1, 0]=3, type=<class 'int'>
# a[1, 1]=4.1, type=<class 'float'>

exit(0)




#--------------------------------------------------------------------------
# advanced topic: 3차원 배열. 칼라 영상 데이터 배열이 아래와 같은 3차원 배열로 이루어짐.
# 3차원 어레이에 대하여.... 입문자는 pass
# 값을 지정해서 3차원 어레이를 선언하는 방법은 2차원과는 달리 직관적이지 않다.
#--------------------------------------------------------------------------
# 3x4x3 => row x col x channel
# 3채널 4x3 영상 어레이...
obj = [[(1, 2, 3), (5, 6, 7), (40, 50, 60), (70, 80, 90)],        # (B,G,R) 4개의 가로 화소
        [(9, 10, 11), (13, 14, 15),(41, 51, 61), (71, 81, 91)],
        [(29, 220, 211), (213, 214, 215), (42, 52, 62), (72, 82, 92)]]

# 4채널 2x2 영상 어레이....
#obj = [[(1, 2, 3, 4), (5, 6, 7, 8)], [(9, 10, 11, 12), (13, 14, 15, 16)]]

img = np.array(obj)
print_att('img')
# type(img)=<class 'numpy.ndarray'>
# img.shape=(3, 4, 3)       row x column x channel
# img.ndim=3, img.dtype=int32, img.itemsize=4, img.size=36

print('\nBlue=\n', img[:, :, 0])        # channel 0 영상. OpenCV의 경우 Blue
# Blue=
#  [[  1   5  40  70]
#  [  9  13  41  71]
#  [ 29 213  42  72]]

print('\nGreen=\n', img[:, :, 1])       # channel 1 영상. OpenCV의 경우 Green
# Green=
#  [[  2   6  50  80]
#  [ 10  14  51  81]
#  [220 214  52  82]]

print('\nRed=\n', img[:, :, 2])         # channel 2 영상. OpenCV의 경우 Red
# Red=
#  [[  3   7  60  90]
#  [ 11  15  61  91]
#  [211 215  62  92]]

exit(0)



# -----------------------------------------------------------------------------------------------
# advanced topic: 3차원 배열을 다른 방법으로 분석해 본다.
# 3차원 어레이에 대하여.... 입문자는 pass
# 칼라 영상 데이터 배열이 아래와 같은 3차원으로 이런 식으로 이루어짐.
# -----------------------------------------------------------------------------------------------

d = np.arange(24).reshape(2, 4, 3)  # [row*column = 4*3] -> 이런 어레이가 2개. ndim= 3
print_att('d')
# d=[[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]
#   [ 9 10 11]]
#
#  [[12 13 14]
#   [15 16 17]
#   [18 19 20]
#   [21 22 23]]]
# type(d)=<class 'numpy.ndarray'>
# d.shape=(2, 4, 3)
# d.ndim=3
# d.dtype=int32
# d.itemsize=4
# d.size=24

print(d[:, :, 0])
print(d[:, :, 1])
print(d[:, :, 2])
