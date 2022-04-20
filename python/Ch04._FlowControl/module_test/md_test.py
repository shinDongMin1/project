"""
    모듈 '_md'의 함수 add/sub를 이용하여 연산을 수행하는 메인 프로그램.
"""

import os
import _md as m
print(f"\n1) module location: \n{m.__file__}")
print(f"\n2) current directory: \n{os.getcwd()}")
x = 1; y = 2
print(f"\n3) imported module based functions: \
x+y={m.add(x, y)}, x-y={m.sub(x, y)}, where x={x}, y={y}")

