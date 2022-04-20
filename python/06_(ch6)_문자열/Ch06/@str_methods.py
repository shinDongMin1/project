"""

스트링 메소드의 참고 자료

파이썬 스트링 메소드
    https://www.w3schools.com/python/python_ref_string.asp
Python - Strings. 조금 더 다양하고 구체적인 정보를 볼 수 있음(40여개의 method)
   https://www.tutorialspoint.com/python/python_strings.htm

"""
a = 'Hello world'
print("len(a)=", len(a))           # This is a intrinsic python function.

print("1) 문자열의 대소 문자 바꾸기 및 문자열 출현 회수 세기")
print("a.upper()=", a.upper())  # a.upper()= HELLO WORLD
print("a.lower()=", a.lower())  # a.lower()= hello world
print("a.title()=", a.title())  # a.title()= Hello World.# 각 단어의 앞글자만 대문자로 변환

b = 'abc bcd efg abc'.capitalize()  # 스트링의 첫 글자만 대문자로 변환. Abc bcd efg abc

# 문자의 출현 횟수 반환
print("b.count('abc')=", b.count('abc'))    # b.count('abc')= 1. 대소문자 가림
print("b.count('bc')=", b.count('bc'))      # b.count('bc')= 3. 스트링의 중간에 있어도 반영함.
str = "012345012345...."    # 문자열을 검색하여 발견한 회수를 반환한다.
print(str.count('.'), str.count('0'), str.count('5.'))  # 4 2 1


print("\n2) 문자열 찾아 위치 반환하기")
b = 'abc bcd efg abc'

# find(str, start, end): 부분 문자열 str의 최초 위치 (첫 글자의 인덱스)를 반환. 왼쪽부터 검색.
#   찾을 문자열이 몇 번째 있는지 반환. 0번부터 시작. 처음 만난 문자열의 위치만 반환한다.
#   못 찾으면 -1을 반환한다. 유사한 함수인 index()는 못찾으면 오류 발생하여 종료한다.
#   start와 end에는 검색을 윈하는 첫 인덱스, 마지막 인덱스를 지정.
#   지정하지 않을 경우, start의 default 값은 0, end의 default의 값은 제일 마지막 인덱스.

print("b.find('abc')=", b.find('abc'))      # b.find('abc')= 0
print("b.find('cd')=", b.find('cd'))        # b.find('cd')= 5
print("b.find('bc')=", b.find('bc'))        # b.find('bc')= 1
print("b.find('g')=", b.find('g'))          # b.find('g')= 10
print("b.find('abcd')=", b.find('abcd'))    # b.find('abcd')= -1. 없음.

# index(str, beg=0, end=len(string))
#   Same as find(), but raises an exception if str not found.
print("b.index('cd')=", b.index('cd'))  # 추가: b.index('cd')= 5
#print("b.index('abcd')=", b.index('abcd'))      # 발견되지 못해 exception 발생. 수행중지

# rindex( str, beg=0, end=len(string))  뒤에서부터 찾되 index 번호는 앞에서부터 센 것으로 반환한다.
#   Same as index(), but search backwards in string.
print("b.rindex('a')=", b.rindex('a'))  # 추가: b.index('a')= 12
print("b.rindex('efg')=", b.rindex('efg'))  # 추가: b.index('efg')= 8


print("\n3) 특정 문자로 시작하거나 특정 문자로 끝나는지의 여부 판단하기")

# 특정 문자열로 시작하는가?
print("'Hey'.startswith('He')=", 'Hey'.startswith('He'))    # 'Hey'.startswith('He')= True
print("'No'.startswith('n')=", 'No'.startswith('n'))        # 'No'.startswith('n')= False. 대소문자 구분
print("'Hey'.endswith('y')=", 'Hey'.endswith('y'))          # 'Hey'.endswith('y')= True
print("'Hey'.endswith('ey')=", 'Hey'.endswith('ey'))        # 'Hey'.endswith('ey')= True
print("'No'.endswith('n')=", 'No'.endswith('O'))            # 'No'.endswith('n')= False

print("\n4) 문자열의 정체 확인: 숫자, 대소문자")

# isdigit(): Returns true if string contains only digits and false otherwise.
print('12345'.isdigit())        # True. 숫자(양의 정수)이면 True
print('-12345'.isdigit(), '1.2'.isdigit())   # False False 음수, 부동소수는 안됨
print('abcdE'.islower())        # False. E 때문에 안됨
print('123'.isalpha(), 'abc'.isalpha())         # False True
print('+12'.isdecimal(), '123'.isdecimal())     # False True
# isnumeric(): Returns true if a unicode string contains only
#   numeric characters and false otherwise.
print('1.2'.isnumeric(), '-12'.isnumeric())     # False False


print("\n5) 스트링의 공백 제거")
c = '     Hi  '     # 좌측에 공백문자 5개, 우측에 2개.
# lstrip(): Removes all leading whitespace in string.
# rstrip(): Removes all trailing whitespace of string.
# strip([chars]): Performs both lstrip() and rstrip() on string.
print('###' + c.strip() + '???')    # 좌우측의 공백 문자를 제거 ###Hi???
print('###' + c.lstrip() + '???')   # 좌측 공백 문자 제거 ###Hi  ???
print('---' + c.rstrip() + '???')   # # 우측 공백 문자 제거 ---     Hi???

print("\n6) 문자열 특정 부분을 변경")
# replace(old, new [, max]): Replaces all occurrences of old in string
#   with new or at most max occurrences if max given.
print('aa\n\na a\na a\na'.replace('\n', ''))    # aaa aa aa 모두 바꾼다.
print('abc aabdab abc'.replace('ab', 'Z', 3))   # Zc aZdZ abc  최대 3개 바꾼다.

print("\n7) 스트링을 왼쪽 혹은 오른 쪽으로 정렬하기")
# ljust(width[, fillchar]): Returns a space-padded string with the original string
#   left-justified to a total of width columns.
str = "string example...."
print(str.ljust(30, '0'))   # string example....000000000000
print(str.rjust(30))        #             string example....


print("\n8) 문자열을 단어별로 나누거나 모으기")

# 공백을 기준으로 문자열을 분리하여 리스트로 반환
print('I am a boy.'.split())    # ['I', 'am', 'a', 'boy.']

time_stamp = "12:47:08"
a = time_stamp.split(':')       # :를 기준으로 문자열을 분리하여 list로 반환
print(a, type(a))               # ['12', '47', '08'] <class 'list'>
b = ':'.join(a)                 # :를 기준으로 리스트 자료를 문자열로 생성
print(b, type(b))               # 12:47:08 <class 'str'>

a = time_stamp.partition(':')
print(a, type(a))  # ('12', ':', '47:08') <class 'tuple'> 튜플로 반환한다.

# 참고: 문자열을 개별 문자로 나누기
a = list('I love U.')     # 스트링에 list() 함수를 씌우면 list를 생성함.
print(type(a), a)  # <class 'list'> ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'U', '.']

b = ''.join(a)      # 리스트 내의 원소를 모아서 스트링으로 만들기. ''
print(b, type(b))   # I love U. <class 'str'>

