"""

A byte of python, 8장 해당 주제의 속성 예제 - 함수

-- 함수의 정의법
1) 함수는 def 키워드를 통해 정의가 시작된다.
    def 뒤에는 함수의 식별자 이름을 입력하고,
    괄호 안에는 함수에서 사용될 입력 parameter(매개변수, 인자 혹은 arguments)의 목록을 열거한다.
2) 새로운 블록이 시작되는 다음 줄부터는 들여쓰기를 수행하며 이 함수에서 사용될 문장들을 작성한다.
3) 함수가 반환하는 값(result)이 있을 때에는 "return(result)", "return result, result2" 명령어를 통해 메인 루틴으로 전달한다.
4) 함수의 끝을 나타내는 표기법은 없다. def에서 들여쓰기가 끝나는 부분이 함수 정의의 끝이라 할 수 있다.

주의사항
1) 모든 함수는 호출하기 전에 선언되어 있어야 한다. 호출되는 명령문 아래에 선언되어 있으면 안됨.
2) 메인 루틴 수행에도 아직 호출하지 않은 새로운 함수를 선언할 수 있다.
3) 같은 이름의 함수도 재 선언하여 사용할 수 있다.

"""




"""
# -------------------------------------------------------------------------------------
# 실습 0: 파라미터가 없는 함수 선언 및 활용
#   아래 예제는 입력 파라미터도 없고 반환 값도 없는 단순한 함수의 사례이다.
#   메인 루틴 수행 중에 다른 함수 뿐만 아니라 같은 이름의 함수도 재 선언이 가능하다.
# -------------------------------------------------------------------------------------
"""
"""
def say_hello():
    # block belonging to the function
    print('Hello world.')
    return 'I am a robot.'
# End of function


# 함수를 호출한다. 함수 내부의 print 기능 때문에 문자열이 출력된다.
say_hello()             # Hello world.

# 함수를 호출하고 반환 받은 값을 출력한다.
print('**', say_hello())      # Hello world. / I am robot.


# 함수 정의는 메인 루틴 안에서 가능하다. 함수를 재정의하였다.
def say_hello():
    print('hello 2!')

# call the function again

say_hello()         # hello 2!
say_hello()         # hello 2!
exit(0)
"""


"""
# -------------------------------------------------------------------------------------
# 실습 1: 함수와 매개 변수
#
#
# 함수를 정의할 때 매개 변수를 지정할 수 있습니다.
# 매개 변수란 함수로 넘겨지는 값들을 말합니다.
#
# 1) 매개 변수의 값들은 함수가 호출되어질 때 넘겨받은 실제 값(real parameter)들로 채워지며
# 함수가 실행되는 시점에서는 이미 할당이 완료되어 있다는 점이 다릅니다.
# 이런 점에서 함수를 정의할 때 쓰이는 매개변수는 dummy parameter라 합니다.
#
# 2) 상황에 따라 함수를 선언할 때 파라미터를 전달받지 않을 때 사용하는 기본 값을 정의할 수 있습니다.
# -------------------------------------------------------------------------------------
"""
"""
# 1) 두 개의 입력 파라미터가 있는 함수. 인자 중에서 최대 값을 출력한다.
def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

# 함수를 호출하는 메인 루틴. directly pass literal values
print_max(3, 4)         # 4 is maximum

# pass variables as arguments
x = 5; y = 7; print_max(x, y)   # 7 is maximum

# 2) 파라미터의 디폴트 값을 갖고 있는 함수
def say(message, times=1):          # times 자리에 값이 전달되지 않으면 그 값은 1이 사용된다.   
    print(message * times)

# times=1 default로 사용된다.
say('Hello')                        # Hello

# 순서가 아니라 keyword로 파라미터를 지정할 수 있다.
say(times=5, message=' World')      #  World World World World World

say('Hey! ', 3)                     # Hey! Hey! Hey!

exit(0)
"""



"""
# -------------------------------------------------------------------------------------
# 실습 2: 지역변수
#
# 지역 변수가 사용되는 사례.
# 함수 안에서 변수를 선언하고 사용할 경우,
# 함수 밖에 있는 같은 이름의 변수들과 함수 안에 있는 변수들과는 서로 연관이 없습니다.
# 이러한 변수들을 함수의 지역(local) 변수라고 하며, 그 범위를 변수의 범위(scope)라고 부릅니다.
# 모든 변수들은 변수가 정의되는 시점에서의 블록을 스코프로 가지게 됩니다.
#
# 아래의 예제는 변수 x가 함수 안과 밖에서 사용되지만 이 둘은 scope가 달라 서로 관련이 없다.
#
# ---- 수행하기 전에 아래 프로그램은 출력 결과를 예측해보자.
# -------------------------------------------------------------------------------------
"""
"""
# func() 안의 범위를 갖는 지역변수, x
def func(x):
    print('In func(): x is', x)
    # 아래 x는 함수내에서 변수 값을 변경하지 않으면 전역변수로 인정된다.
    x = 2       # This is local variable.
    print('In func(): local x was changed to', x)

x = 50; func(x); print('In main: 1. x is ', x, '\n')
x=3.14; func(x); print('In main: 2. x is ', x)

exit(0)
"""

"""
# -------------------------------------------------------------------------------------
# 실습 3: 전역변수
# -------------------------------------------------------------------------------------
"""
"""
# 1) 메인에서 사용한 변수는 원칙적으로 전역변수이다.
#    함수 내에서 그 변수에 쓰기 동작을 수행하지 않으면 함수내에서도 전역변수로 인정된다.
print("\n1) Global variable defined in main routine")

def func():
    print('In func(): x is', x)
    # 아래 x는 함수내에서 변수 값을 변경하지 않으면 전역변수로 인정된다.
    #x = 2       # This is local variable.
    #print('In func(): local x was changed to', x)

x = 50; func(); print('In main: 1. x is ', x, '\n')
x=3.14; func(); print('In main: 2. x is ', x)

# 2) 함수 안에서 전역화하고 싶은 변수를 global로 선언한다.
# main에서 50으로 선언한 변수 값이 함수내에서 2로 바꾸어서 복귀하였는데
# 메인에서 그 변수를 확인하였더니 2로 바뀌었다.
print("\n2) Global variable defined inside a function")
def func():         # 입력 파라미터 없음.
    global x
    print('x was', x, 'when it was input to the function.')
    x = 2
    print('In function: global x was changed to ', x)
x = 50; func()
print('In main routine: global of x is', x, '\n')

exit(0)
"""


"""
# -------------------------------------------------------------------------------------
# 미션 : 여러 개의 반환 값을 갖는 함수의 사례를 직접 작성해 보자.
#   폭과 높이를 입력 받아 면적과 둘레를 반환하는 함수
#   return() 파라미터에 반환 값을 여러 개 지정할 수 있다.
# -------------------------------------------------------------------------------------
"""

def rect_para(width, height):
    return width * height, (width+height) * 2


w = 40; h = 10
a, p = rect_para(w, h)

print('area=', a, 'perimeter=', p)              # area= 400 perimeter= 100

ret_val = rect_para(w, h)
print(ret_val, type(ret_val))                   # (400, 100) <class 'tuple'>


# str tuple(바꿀수 없음) / list for i in rang(0,4) print(r'\n\r\t') print('', end='') input('입력 :')
'''
x = 10; y = 3
print(7, f'x + y = {x+y} | x * y = {x*y}')             # f-string 방식. 간결하고 읽기 편하다.
# 출력 결과 =>7 x + y = 13 | x * y = 30

print(8, 'x + y = %d | x * y = %d' % (x+y, x*y))        # %-formatting 방식
# 출력 결과 =>8 x + y = 13 | x * y = 30

print(9, 'x + y = {} | x * y = {}'.format(x+y, x*y))   # str.format 방식
# 출력 결과 =>9 x + y = 13 | x * y = 30

a.append('Hello')  뒤에붙임
a.insert(2, 'k')   [2]에 k입력
a.remove('k')      k삭제
a.pop()            맨뒤[]삭제 
a.reverse()        역순 a[-1::-1]
a[:] == a[0::1]
'''

