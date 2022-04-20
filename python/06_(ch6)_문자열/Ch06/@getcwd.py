# 미션 및 과제를 위한 힌트 ----------------------------------

#"""
a = '2019-10-08  오전 02:32             3,892 str_methods.py'
b = a.split()
print(b)

b = '3,892'.replace(',', '')        # replace(old, new)
print(b)
#exit(0)
#"""

# os 모듈 연습 ----------------------------------------------
import os
cur_dir = os.getcwd()
print('current directory=', cur_dir)

# 윈도즈 콘솔창 및 파이참 터미널(수행창)의 기본 코드페이지는 949 이다.
# 이 페이지는 utf-8과 호환성이 없는 한글 체계를 가지고 있다.
# 따라서 utf8 로 한글을 출력할 시에는 깨지게 된다.
# "chcp 65001" 명령을 실행하여 화면 코드페이지를 utf8(65001) 로 바꾼다.
# 수행이 새로 시작될 때마다 다시 영문 모드로 설정되므로 매번 시행해야 한다.
# 다시 원래 코드 페이지로 돌아가려면 "chcp 949"를 수행한다.

os.system('chcp')           # 현재의 활성 코드 페이지 번호를 출력한다. 수행하면 한글이 깨져서 출력됨
os.system('chcp 65001')     # utf-8 기반의 한글이 출력되는 페이지 모드로 설정한다.
#os.system('dir')
#os.system('dir c:\\')       # \는 esc 문자이므로 한번 더 \를 써야 한다. "C:\"는 C의 root forlder이다.
#os.chdir("C:\\")            # \는 esc 문자이므로 한번 더 \를 써야 한다. "C:\"는 C의 root forlder이다.

os.system('dir > 한글.txt'); os.system('type 한글.txt')
#os.system('dir d:\ > 한글.txt'); os.system('type 한글.txt')

"""
한글.txt를 분석하여 다음 내용을 출력하시오.
확장자의 개수와 각 확장자에 따른 파일의 수를 출력하시오.
   확장자: 개수: 파일크기의 합: 
    py:24: 1000 
   exe: 2: 2002
   txt: 3:   10
   <abdc>
   <폴더1>
   총 확장자의 수=3, 폴더의 수=2, 총 파일의 수=29, 총 용량=3012        
"""

exit(0)
