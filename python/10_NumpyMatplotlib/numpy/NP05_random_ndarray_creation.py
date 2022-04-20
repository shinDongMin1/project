"""
랜덤 넘버로 ndarray 만들기
난수를 발생하는 모듈은 1) 파이썬 내장 모듈, random과  2) numpy.random 모듈이 있다.
1) 파이썬 내장 모듈, random
    random.randint(0, 10)               # [0, 10]사이의 값 중 하나를 반환. 양단 값 포함 가능.
    random.randrange(1, 10)             # [1, 10)사이의 값 중 하나를 반환. 내장 모듈 random에만 있음.

2) numpy.random 모듈
    np.random.randint(0, 10)                    # [0, 10]사이의 값 중 하나를 반환. 양단 범위 모두 포함.
    np.random.randn(2, 3)                       # 2x3 랜덤값으로 채워진 어레이 반환
    np.random.uniform(20, 30, size=(4, 3))      # [20, 30)범위의 난수로 채워진 4x3 어레이 반환
                                                # [20, 30) => 20은 포함. 30는 불포함.

부동소수 배열을 print() 함술로 출력할 때 소수 이하 자릿수를 지정하는 함수
    np.set_printoptions(precision=2)        # numpy 배열의 정밀도를 소수 이하 2자리로 제한하여 출력하는 것으로 설정한다.
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




#--------------------------------------------------------------------------
#
# If you wanted to generate a sequence of random numbers,
# one way to achieve that would be with a Python list comprehension:
# https://realpython.com/python-random/
#
# The random.random() function returns a random float in the interval [0.0, 1.0).
#   The result will always be less than the right-hand endpoint (1.0).
#   This is also known as a semi-open range:
#--------------------------------------------------------------------------


import random       # 파이썬 내장 모듈

# random.randint() function. 정수 반환
#   This spans the full [x, y] interval and may include both endpoints:
a = random.randint(0, 10)                # [0, 10]사이의 값 중 하나를 반환. 양단 값 포함 가능. 아래 함수도 쓸 수 있음.
#a = np.random.randint(0, 10)           # numpy.random 모듈에도 있음. [1, 10]사이의 값 중 하나를 반환.
print('\n1. random.randint(0, 10)=>', a)   # 호출할 때마다 0~10의 값 중 하나를 반환
# 출력: 1. random.randint(0, 10)=> 4


# numpy.random.randn(d0, d1, ..., dn)
# 평균값 0, 편차 1인 가우시안 분포를 갖는 난수를 (d0, d1, ..., dn) shape의 행렬로 반환한다.
#a=random.randn(5)                      # 오류! random에는 없음.
a = np.random.randn(5)                    # numpy.random 모듈에만 있음. 원소가 5개인 1차원(5,) 배열의 난수를 반환한다.
print(f'\n2a. shape={a.shape}: np.random.randn(5)=\n', a)
# 출력: 2a. shape=(5,): np.random.randn(5)=
#  [ 1.68531706  1.59633446  0.56248542  0.07058926 -0.01983701]

a = np.random.randn(2, 3)   # 2 x 3 배열의 2차원 난수 어레이를 반환한다.
print(f'\n2b. shape={a.shape}: np.random.randn{a.shape}=\n', a)
# 출력: 2b. shape=(2, 3): np.random.randn(2, 3)=
#  [[-0.62483715 -0.20894444 -0.48421723]
#  [-1.36941948 -0.55069128 -0.15198591]]

# With random.randrange(), you can exclude the right-hand side of the interval,
#   meaning the generated number always lies within [x, y)
#   and will always be smaller than the right endpoint:
a = random.randrange(1, 10)               # 내장 모듈 random에만 있음.
#a=np.random.randrange(1, 10)           # 오류! numpy.random 모듈에는 없음.
print('\n3. random.randrange[1, 10)=>', a)
# 출력: 3. random.randrange[1, 10)=> 7



# 랜덤 값으로 채워진 지정된 크기의 ndarray를 생성하는 방법
# numpy.random.uniform(low=0.0, high=1.0, size=None)
#       Draw samples from a uniform distribution.
#       Samples are uniformly distributed over the half-open interval [low, high) (includes low, but excludes high).
#       In other words, any value within the given interval is equally likely to be drawn by uniform.
#       low와 high 사이의 난수를 균일하게 발생
a = np.random.uniform(20, 30, size=(4, 3))     # [20, 30) 사이의 값으로 구성된 4 x 3 배열 반환. numpy.random 모듈에만 있음.
#a = random.uniform(20, 30, size=(4, 3))       # 오류! random 모듈에는 없고 numpy.random 모듈에 있음
#np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
np.set_printoptions(precision=2)        # numpy 배열의 정밀도를 소수 이하 2자리로 제한하여 출력하는 것으로 설정한다.


# 임의의 어레이의 내부 원소 값을 지정한 정밀도로 출력하는 2가지 방법(a, b)
# 소수 이하 몇째자리까지 출력할 것인지 지정해 보았다.
print('\n4a. np.random.uniform(20, 30, size=(4, 3)) =\n', a)
# 출력: 4a. np.random.uniform(20, 30, size=(4, 3)) =
#  [[26.72 25.21 20.74]
#  [28.75 22.05 26.17]
#  [29.   20.64 20.63]
#  [25.51 26.51 29.15]]

print('\n4b. a=')       # loop문을 활용해서 자신이 지정한 정밀도로 내부 원소의 값을 출력해 본다.
for r in range(a.shape[0]):
    for c in range(a.shape[1]):
        print(f'{a[r, c]:#7.3f}', end='')
    print()
# 4b. a=
#  26.725 25.209 20.744
#  28.748 22.053 26.174
#  29.002 20.638 20.626
#  25.512 26.508 29.152

exit(0)

