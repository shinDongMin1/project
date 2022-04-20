"""

    byte object를 다른 자료형으로 변환
    한글 바이트 오브젝트 핸들링

"""

import numpy as np


# 1) bytes object를 ndarray로 변환(1) - 1개의 바이트 오브젝트
a = b'\x00\01\x41\x30'
print("1.1 a:", type(a), len(a), a)
# 1.1 a: <class 'bytes'> 4 b'\x00\x01A0'
# 변수 a는 4바이트 크기의 bytes object이다.

b = np.array(a)
print("1.2 b:", type(b), b.shape, b.itemsize, b.size, ' dtype=', b.dtype)
# 1.2 b: <class 'numpy.ndarray'> () 4 1  dtype= |S4
# 0차원, 4바이트 크기의 원소 1개를 가진 ndarray를 선언하였다.
# |S4 dtype에 대하여: 길이가 4인 스트링 값을 갖고 있다는 data type descriptor를 의미한다.
# The | pipe symbol is the byteorder flag;
# in this case there is no byte order flag needed, so it's set to |, meaning not applicable.


# 2) bytes object를 ndarray로 변환(2) - 여러개의 바이트 오브젝트
a = [b'\x00', b'\x01', b'A', b'0']      # 4개의 바이트 오브젝트를 리스트로 묶다.
b = np.array(a)     # ndarray로 변환
print("2.1 b:", type(b), b.shape, b.itemsize, b.size, ' dtype=', b.dtype)
# 2.1 b: <class 'numpy.ndarray'> (4,) 1 4  dtype= |S1
# 1차원, 1바이트 크기의 원소 4개를 가진 ndarray를 선언하였다.
# |S1 dtype에 대하여: 길이가 1인 스트링 값을 갖고 있다는 data type descriptor를 의미한다.

bb = bytes(b)
print("6.2 bytes object from ndarray:", type(bb), len(bb), bb)


# 3) bytes object를 list로 변환
d = b'01AB'                 # <class 'bytes'> 4 b'01AB' [48, 49, 65, 66]
#d = b'\x30\x31\x41\x42'     # <class 'bytes'> 4 b'01AB' [48, 49, 65, 66]
d = b'\x0a\x0d\xff'        # <class 'bytes'> 3 b'\n\r\xff' [10, 13, 255]
print('3. bytes to list:', type(d), len(d), d, list(d))
# <class 'bytes'> 3 b'\n\r\xff' [10, 13, 255]


# 4) 한글이 들어 있는 바이트 오브젝트의 핸들링
# '한'=\xed\x95\x9c 한글문자 '한'은 utf8로 인코딩된 3바이트의 유니코드로 구성된다.
str_obj = '한'             # 한글이 포함된 string
bt_obj = bytes(str_obj, encoding='utf8')      # string to bytes object
print("4.1 hanguel string to bytes :", type(bt_obj), len(bt_obj), bt_obj)
# <class 'bytes'> 3 b'\xed\x95\x9c'
print("4.2 bytes to hanguel string :", str(bt_obj, 'utf-8'))
# 한
print("4.3 bytes to hanguel string :", str(bt_obj))
# b'\xed\x95\x9c'
bt_obj = b'01a\xed\x95\x9cA'   # a bytes object.
print('4.4 bt_obj:', type(bt_obj), len(bt_obj), bt_obj, str(bt_obj, 'utf-8'))
# <class 'bytes'> 7 b'01a\xed\x95\x9cA' 01a한A
