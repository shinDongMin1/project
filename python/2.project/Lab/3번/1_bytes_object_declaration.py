"""
byte object를 선언하기

    <class 'bytes'> 형 자료의 데이터를 해석하고 활용하는 방법에 대해 학습한다.
    이 자료형은 파일의 바이너리로 읽어올 때 반환받는 데이터 형이다.
    이 자료형은 출력할 때는 바이트 단위로 그 16진수 값을 출력하는데 ASCII 문자에 대해서는 해당 문자로 치환하여 출력한다.

참조 링크
# https://www.w3resource.com/python/python-bytes.php#:~:text=Bytes%20and%20bytearray%20objects%20contain,use%20the%20bytearray()%20function.


"""




# ----------- binary value를 선언하기.
code8 = 0b1000_0001
#code8 = 0x81       # 위와 같음.
print('1. binary representation:', type(code8), code8, f'{code8:#b}', f'{code8:#05x}' )
# <class 'int'> 129 0b10000001 0x081


# ----------- int를 이진수로 표현된 스트링으로 변환하기
str_code8 = bin(code8)
#str_code8 = f'{code8:#b}'   # 위와 같음.
print('2. int to string:', type(str_code8), str_code8, f'{code8:#16b}')
# <class 'str'> 0b10000001       0b10000001


# ----------- bytes object의 선언(1) - b''을 이용해 정의
a = b'\x00\01\x41\x30'      # b'\x00\x01A0'
# 바이트 오브젝트를 출력하면 바이트 단위로 출력한다.
# 이중 데이터가 8비트 ASCII 영역의 문자로 변환할 수 있는 코드는 해당 ASCII 문자로 변환해서 프린트한다.
# 나머지 8비트 데이터에 대해서는 \x 이후 16진수로 출력한다.
print("3. bytes object definition with b'':", type(a), len(a), a)
# <class 'bytes'> 4 b'\x00\x01A0'


# ----------- bytes object의 선언(2) - bytes() 함수를 이용해 정의.
# 정수로 구성된 [] 리스트를 지정하여 정의한다.
# 0~ff까지의 값에 대한 unicode character을 보인다.
b256 = bytes([v for v in range(256)])   # 0~255까지의 256바이트의 바이트 오브젝트를 선언
print("4. bytes object with bytes() function:", type(b256), len(b256))
# <class 'bytes'> 256
print(b256)
# b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#


# ----------- bytes object의 선언(3) - bytes() 함수를 이용해 정의.
# 스트링을 제공하여 정의
b = '\x00\x01A0'
c = '\x00\01\x41\x30'
bb = bytes(b, encoding='utf8')
cc = bytes(c, encoding='utf-8')
print("5.1 bytes object from string:", type(bb), len(bb), bb)
# <class 'bytes'> 4 b'\x00\x01A0'
print("5.2 bytes object from string:", type(cc), len(cc), cc)
# <class 'bytes'> 4 b'\x00\x01A0'


# ----------- bytes object의 선언(4) - bytes() 함수를 이용해 정의.
# ndarray를 제공하여 정의
import numpy as np
b = np.array([0, 1, 0x41, 0x00], np.uint8)
print("6.1 b:", type(b), b.shape, b.itemsize, b.size, ' dtype=', b.dtype)
# 6.1 b: <class 'numpy.ndarray'> (4,) 1 4  dtype= uint8

bb = bytes(b)
print("6.2 bytes object from ndarray:", type(bb), len(bb), bb)
# 6.2 bytes object from ndarray: <class 'bytes'> 4 b'\x00\x01A\x00'
