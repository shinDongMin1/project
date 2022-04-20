"""
    pip로 설치한 패키지의 파이썬 path 알아내기
    파이썬의 설치 위치와 패키지의 설치 위치를 출력한다.
    ['D:\\Work\\W_PYTHON\\Python\\Python_3.7.6',
    'D:\\Work\\W_PYTHON\\Python\\Python_3.7.6\\lib\\site-packages']

"""

import site
print(site.getsitepackages())

"""

    파이썬에서는 모듈, 패키지를 찾을 때 일단 현재 폴더에서 먼저 찾는다.
    실패하면 다음과 같이 sys모듈의 path변수(즉, sys.path)에 지정한 경로를 사용한다.

D:\Work\@@Python\LectureMaterials\09_(ch11)_모듈과 패키지\Ch11
D:\Work\@@Python
D:\Work\@@Python\LectureMaterials\my_modules
D:\Work\W_PYTHON\Python\Python_3.7.6\python37.zip
D:\Work\W_PYTHON\Python\Python_3.7.6\DLLs
D:\Work\W_PYTHON\Python\Python_3.7.6\lib
D:\Work\W_PYTHON\Python\Python_3.7.6
C:\Users\KJH\AppData\Roaming\Python\Python37\site-packages
D:\Work\W_PYTHON\Python\Python_3.7.6\lib\site-packages
D:\Work\W_PYTHON\Python\Python_3.7.6\lib\site-packages\pip-19.3.1-py3.7.egg
D:\Work\W_PYTHON\Python\Python_3.7.6\lib\site-packages\win32
D:\Work\W_PYTHON\Python\Python_3.7.6\lib\site-packages\win32\lib
D:\Work\W_PYTHON\Python\Python_3.7.6\lib\site-packages\Pythonwin


"""
import sys
print()
for v in sys.path:
    print(v)
