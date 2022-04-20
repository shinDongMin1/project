'''

A byte of python, 5장, 6장 해당 주제의 속성 예제

주석문:
1. 여러 줄로 구성된 주석문은 triple quotes(3개의 따옴표)로 표현한다.
    큰 따옴표(double quotation marks, ") 3개 혹은
    작은 따옴표(single quotation marks, ')를 3개를 사용하여 열고 닫습니다. 작은 따옴표는 첫번째 주석문에만 허용되는 듯...
2. 한 줄짜리 주석문은 #로 시작된다.

변수에 대해...
1. C언어의 경우
    C에서는 변수는 사용되기 전에 먼저 데이터 형이 선언되어야 한다.
    C에서는 변수의 자료형이 일단 정해지면 바뀌지 않는다. => hard typing
    기본적인 데이터 형: char, short, int, long, float, double, bool & signed/unsigned ==> dynamic typing

2. 파이썬 언어의 경우
    변수는 미리 선언하지 않는다. 값을 배정할 때 변수를 선언한다.
    선언된 변수의 데이터 형은 새로운 값을 재정할 때 그 데이터형으로 바뀐다.=> Dynamic Typing
    기본적인 데이터 형: int, float, str, bool
        - signed/unsigned 개념이 지원되지 않는다. char, short, long, double 없음.
        - 크기에 제한이 없다..
    그밖에 list, tuple, dictionary, set 등의 복합적인 데이터형이 지원된다.
    변수는 사실상 특정 데이터 형의 속성을 갖는 class로 선언된 object이다.
    따라서 데이터(object)에 대해 다양한 method를 지원하고 있다.

파이썬의 변수 살펴보기
1. 변수의 데이터 타입은 계속 바뀔 수 있다. => Dynamic Typing
    변수는 미리 타입을 선언해 둘 필요없다.
    변수에 값을 할당할 때 적정할 데이터 타입이 자동으로 결정된다.
    변수는 실제로는 class에 의해 선언된 객체(object)이다.
    변수에 새로운 값을 배정하면 그때 마다 데이터 타입이 바뀐다. => Dynamic Typing
2. 변수의 데이터 타입을 원하는 대로 바꾸어 사용할 수 있다.
    테이터 타입을 바꾸는 함수가 있다.
3. 기본 연산 살피기
    곱셈, 나눗셈, 몫/나머지, 지수승

'''


"""
# -------------------------------------------------------------------------------------
# 실습 1: Dynamic Typing
# 파이썬은 변수의 타입이 계속 바뀔 수 있는 dynamic typing(soft typing)을 사용한다.
# int, float, str, bool 등의 타입이 존재한다.
#   파이썬에는 long, signed/unsigned의 개념이 존재하지 않는다.
# -------------------------------------------------------------------------------------
"""
"""
a = 10.5
print(1, a, type(a))       # 10.5 <class 'float'>

a = 20
print(2, a, type(a))       # 20 <class 'int'>

# 정수에 대해 정수로 나누기를 해도 부동소수로 형변환이 된다. 소수점이 없더라도..
# Python 2.7에서는 형변환이 일어나지 않는다. 그냥 소수이하를 버리는 정수가 된다.
a /= 2                  # a = a/2
print(3, a, type(a))       # 10.0 <class 'float'>

# 정수에 대해 정수 곱하기를 행하면 부동소수로 형변환이 되지 않는다.
# 그러나 정수로 나누면 그 값이 정수로 표현할 수 있어도 부동소수가 된다. python 2.7에서는 형변환이 되지 않았음.
a = 10; a *= 3
b = a/3
print(4, a, type(a))       # 30 <class 'int'>
print(5, b, type(b))       # 10.0 <class 'float'>

# 정수에 대해 부동소수를 곱하면 부동소수가 된다.
a= 20; a *= 3.0
print(6, a, type(a))       # 60.0 <class 'float'>

# // 연산자 : 몫을 반환한다.
# % 연산자 : 나머지를 반환한다.
# **연산자 : 지수승
a = 5
a, b, c, d = a//3, a % 3, a ** 2, 5.0 ** 2   # <class 'int'> <class 'int'> <class 'int'> <class 'float'> 1 2 25 25.0
print(7, type(a), type(b), type(c), type(d),  a, b, c, d)

a = True                # or False
print(8, a, type(a))       # True <class 'bool'>

# 파이썬에서는 long 형이 없다. 그러나 int 형에 어떤 크기의 정수든지 담을 수 있다.

a = 9223372036854775807      # 64 bit signed long의 최대 크기, 9,223,372,036,854,775,807
a = 2 ** 63 -1
print(9, type(a), a)       # <class 'int'> 9223372036854775807

a = 2 ** 128
print(10, type(a), a)       # <class 'int'> 340282366920938463463374607431768211456

exit(0)
"""

"""
# -------------------------------------------------------------------------------------
# 실습 2: string(스트링) 변수
# 스트링 변수는 immutable(변경할 수 없는, 정적인) 자료구조이다. 스트링 변수의 내부 값은 수정할 수 없다.
# -------------------------------------------------------------------------------------
"""
"""
a = 'Hello'
print(1, type(a), a[0], a[1], a[2], a[-1], a[-2])
# 출력 결과 ===>1 <class 'str'> H e l o l
#a[0] = 's'  # 수행 오류. immutable(변경할 수 없는, 정적인) 자료구조

# string concatenation: +로 스트링 문자열을 연결
b = ' world'
c = a + b
print(2, type(c), len(c), c)
# 출력 결과 ===>2 <class 'str'> 11 Hello world

d = a * 2
print(3, type(d), len(d), d)
# 출력 결과 ===>3 <class 'str'> 10 HelloHello

a = "a" "b" "c""d"
print(4, type(a), len(a), a)
# 출력 결과 ===>4 <class 'str'> 4 abcd

exit(0)
"""


"""
# -------------------------------------------------------------------------------------
# 실습 3: Type Casting 함수
# 다음 변수들의 자료형을 관찰하고 그 형을 type casting 함수를 통해 바꾸어 보자.
# type casting : 입력 데이터의 자료형을 바꾸는 함수들. int(), float(), str()
# -------------------------------------------------------------------------------------
"""
"""
a = 15.9 + 4
print(a, type(a))   # 19.9 <class 'float'>
a = int(a)            # int() : 정수형으로 변환. 소수이하 버림에 유의
print(a, type(a))   # 19 <class 'int'>

a = float(a)        # float() : 부동소수로 변환
print(a, type(a))   # 19.0 <class 'float'>

# str() : 스트링으로 변환.
print("I own " + str(int(a)) + " apples.")    # I own 19 apples.
#print("I own", a, "apples.")    # I own 19 apples.
print("I own", int(a),  "apples.")
exit(0)
"""


"""
# -------------------------------------------------------------------------------------
# 실습 4: list 자료형 / indexing & slicing operation
# 리스트란 순서대로 정리된 항목들을 담고 있는 자료 구조이다.
# 리스트를 정의할 때는 대괄호 []를 이용해서 정의한다.
# 한번 리스트를 만들어 두면 여기에 새로운 항목을 추가하거나 삭제할 수 있다.
# 이 때 항목을 추가 및 삭제가 가능하다는 것을 비정적(mutable)이라고 한다.
# 리스트는 비정적 자료구조이다. 따라서 리스트 변수는 내부 항목을 변경할 수 있습니다.
#
# list 자료구조 요약
#   [ ]로 정의. 수정가능(mutable=변할 수 있는)
# -------------------------------------------------------------------------------------
"""
"""
a = [1, 2, 3]  # LIST 구조체라고 생각
print('01: ', a, type(a), len(a))   # 01:  [1, 2, 3] <class 'list'> 3

a[0] = 'A'          # indexing operation. []안에 인덱스 번호를 적는다.
print('02: ', a, type(a), len(a))   # 02:  ['A', 2, 3] <class 'list'> 3

a[-1] = 3.14        # indexing operation. []안의 인덱스가 -1이면 맨 마지막 인덱스 번호이다.
print('03: ', a, type(a), len(a))   # 03:  ['A', 2, 3.14] <class 'list'> 3

a *= 2
print('04: ', a, type(a), len(a))   # 04:  ['A', 2, 3.14, 'A', 2, 3.14] <class 'list'> 6

del a[0:4]  # slicing operation. 인덱스를 지정하여 삭제. 0~3 원소까지 삭제. [시작번호:끝번호+1]
print('05: ', a, type(a), len(a))   # 05:  [2, 3.14] <class 'list'> 2

a.append('Hello')       # 리스트 맨 마지막에 추가
print('06: ', a, type(a), len(a))   # 06:  [2, 3.14, 'Hello'] <class 'list'> 3

b = [4, 5]
a += b
print('07: ', a, type(a), len(a))   # 07:  [2, 3.14, 'Hello', 4, 5] <class 'list'> 5

a.insert(2, 'k')        # 2번째 위치에 'k' 삽입하기
print('08: ', a, type(a), len(a))   # 08:  [2, 3.14, 'k', 'Hello', 4, 5] <class 'list'> 6

a.remove('k')           # 값을 지정하여 삭제. 2개 이상이면 하나만 지운다. 없으면 오류를 발생한다.
print('09: ', a, type(a), len(a))   # 09:  [2, 3.14, 'Hello', 4, 5] <class 'list'> 5

a.pop()
print('10: ', a, type(a), len(a))   # 10:  [2, 3.14, 'Hello', 4] <class 'list'> 4

a.reverse()
print('11: ', a, type(a), len(a))   # 11:  [4, 'Hello', 3.14, 2] <class 'list'> 4

for i in range(len(a)):
    print(type(a[i]))               # <class 'int'> <class 'str'> <class 'float'> <class 'int'>
exit(0)
"""
"""

# -------------------------------------------------------------------------------------
# 실습 5: tuple 자료형 / indexing & slicing operation
# 튜플은 리스트와 비슷하지만, 리스트 클래스에 있는 여러가지 기능(method)이 없다.
# 또 튜플은 수정이 불가능하며, 그래서 주로 문자열과 같이 정적인(immutable, 변할 수 없는)객체들을 담을 때 사용된다.
# tuple과 str 자료형은 모두 immutable 자료형이다.
# 튜플에 저장된 값들은 수정이 불가능하기 때문에, 단순 값들의 목록을 다루는 구문이나
# 사용자 정의 함수에서 주로 사용된다.
# -------------------------------------------------------------------------------------
"""
"""
a = (1, 2, 3, 4, 5, 6, 7)
print('01: ', a, type(a), len(a))       # 01:  (1, 2, 3, 4, 5, 6, 7) <class 'tuple'> 7
#a[0] = 0

# 오류 동작 연습: immutable 자료형에 값을 배정하는 동작은 허용되지 않는다.
#a[0] = 0        # 0번째 원소의 값을 0으로 대치하고자 하나 오류 발생. tuple의 값을 수정할 수는 없다.

# tuple, list 데이터에 행할 수 있는 slicing operation 연습
# 인덱스 번호를 지정하여 특정 인덱스들을 모두 지명할 수 있다.
b = []           # empty list 생성. empty tuple에는 데이터를 담을 수 없다.
b[:] = a[:]     # slicing operation. : means 'for all indexes"
print('02: ', b, type(b), len(b))       # 02:  [1, 2, 3, 4, 5, 6, 7] <class 'list'> 7

c = []           # empty list 생성
c[:] = a[0:3]       # slicing operation. c[0:3] = a[0:3] 도 같은 결과. [시작:끝+1]
print('03: ', c, type(c), len(c))       # 03:  [1, 2, 3] <class 'list'> 3

d = []           # empty list 생성
d[:] = a[0::2]       #slicing operation. [시작:끝+1:increment] 끝+1 자리가 비워 있으면 자료의 끝까지 처리함을 의미한다.
print('04: ', d, type(d), len(d))       # 04:  [1, 3, 5, 7] <class 'list'> 4

e = []           # empty list 생성
e[:] = a[-1::-1]       #slicing operation. 마지막에서 시작해서 증분이 -1로 하여(거꾸로) 맨끝(실제로는 맨앞)까지 인덱싱한다.
print('05: ', e, type(e), len(e))       # 05:  [7, 6, 5, 4, 3, 2, 1] <class 'list'> 7

a = 'hello?'
print('06: ', a[0], type(a), len(a))    # 06:  h <class 'str'> 6
#a[0] = 'H'      # 수정 불가. str 자료형은 모두 immutable 자료형이다.

exit(0)
"""


"""
# -------------------------------------------------------------------------------------
# 실습 5: 5.2 리터럴 상수(literal constants) 혹은 줄여서 literals
#   리터럴 상수는 5 , 1.23 과 같은 숫자나, 'This is a string'
#   혹은 "It’s a string!"과 같은 문자열 등을 말합니다.
#   이것들을 리터럴 상수라고 불리우는 이유는 이것들이 프로그램 내에 직접 있는 그대로(literally)
#   지정되는 값들이기 때문입니다.
# -------------------------------------------------------------------------------------
"""
"""
a = 5     # a는 변수(int), 5는 literal constant.
print(type(a))

b = 1.23  # b는 변수(float), 1.23은 literal constant.
print(type(b))

a = 'Hello'   # a는 변수(str), 'Hello'는 literal constant.
print(type(a))
"""