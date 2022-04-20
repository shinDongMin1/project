# 1. 모듈의 이름과 그가 지원하는 함수를 지명하여 호출한다.
import z_fah_converter
celsius = 21
fahrenheit = z_fah_converter.covert_c_to_f(celsius)
print("\n1) That's", fahrenheit, "degrees Fahrenheit.")
print(z_fah_converter.more())
del z_fah_converter     # 모듈 제거

# 2. from을 이용하여 특정함수/클래스만을 호출
from z_fah_converter import covert_c_to_f, more
fahrenheit = covert_c_to_f(celsius)
print("2) That's", fahrenheit, "degrees Fahrenheit.")
#print(z_fah_converter.more())       # 오류 발생
print(more())
del covert_c_to_f, more

# 3. as를 이용해 모듈의 이름을 alias를 바꾸어 간편하게 호출한다.
import z_fah_converter as fc
fahrenheit = fc.covert_c_to_f(celsius)
print("3) That's", fahrenheit, "degrees Fahrenheit.")
del fc

# 4. 모듈의 이름을 지정하지 않고 모듈 안의 모든 함수를 호출한다.
from z_fah_converter import *
fahrenheit = covert_c_to_f(celsius)
print("4) That's", fahrenheit, "degrees Fahrenheit.")
print(more())
#del *      # 오류.
del covert_c_to_f, more

# 5. from과 as를 이용해 함수의 이름을 alias를 바꾸어 호출.
from z_fah_converter import covert_c_to_f as cvt
fahrenheit = cvt(celsius)
print("5) That's", fahrenheit, "degrees Fahrenheit.")
del cvt

