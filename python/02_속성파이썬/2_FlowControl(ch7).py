"""

A byte of python, 7장 해당 주제의 속성 예제 - 흐름제어

흐름 제어
    1. if statement
    2. while statement
    3. for loop
    4. break statement
    5. continue statement
"""

"""
#---------------------------------------------------------------------------------------------------
# 실습 1 - if 문
# 동작설명    
#   임의로 입력한 수자가 5와 16 사이에 있는지 5보다 작은지, 16보다 큰지 판단하여 결과를 출력한다.
#   값을 입력할 때는 수행(Run)창에 enter와 함께 입력해야 한다.
# 미션: 
#   1. input() 함수의 반환 값이 스티링형인지 확인하시오.
#   2. 아래에서 출력을 f-string을 사용하여 formatting 하시오. 
#---------------------------------------------------------------------------------------------------
"""
"""
low = 5
high = 16

# input() 함수는 인자로 주어진 메시지를 출력한 후 키보드 입력을 받는다.
# 입력받은 수자는 string이다. 수치 비교를 위해서는 이를 int() 함수를 통해 정수로 변환해야 한다.
guess = int(input('Enter an integer : '))     
if (guess >= low) and (guess <= high):
    print(f'{low} <= guess <= {high}')
elif guess < low:
    print('guess < %d' % low)
elif guess > high:
    print('guess > %d' % high)  # {high}

exit(0)
"""

"""
#---------------------------------------------------------------------------------------------------
# 실습 2 - while 문
#     while 문은 제시된 조건이 참(True)일 경우 블록의 명령문들을 반복하여 실행한다.
#     거짓(False)이면 while 블록의 수행을 중지한다.
#     True와 False는 bool 타입의 속성을 가지며, 각각 숫자 로직 1과 로직 0의 값을 갖는다.
#     while 문에도 else 절이 따라올 수 있다.
#
# 동작: 숫자 알아맞히기 게임
#   컴퓨터가 미지 지정한 값을 사용자가 컴퓨터가 출력한 힌트를 바탕으로 그 값을 추정하여 맞힌다.
#   사용자가 추정한 값보다 큰 지, 작은 지 그 힌트를 제공한다. 맞추면 종료한다.
# 미션:
#   while running: 대신에 while running==1:을 사용했을 때 예상되는 결과는?
#---------------------------------------------------------------------------------------------------
"""
"""
number = 23
running = True
print('running=', running, '| type(running)=', type(running))   # running= True | type(running)= <class 'bool'>

while running:
#while running == 1:           # 위의 while running: 을 주석 처리하고 이 명령줄을 사용하면 예측되는 결과는?
    guess = int(input('Enter an integer : '))   # 키 입력을 스트링으로 받기 때문에 정수형 변환이 필요.
    if guess == number:
        print('Congratulations, you guessed it.')
        # this causes the while loop to stop
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
print('The while loop is over.')

exit(0)
"""


"""
#---------------------------------------------------------------------------------------------------
# 실습 3 - for ~ in 문
#   for..in 문은 in에 지정된 열거형(Sequence) 객체의 각 항목을 하나씩 바꾸어가며 실행한다.
#---------------------------------------------------------------------------------------------------
"""
"""
print('\ntest 1: ', end='')
for v in [1, 2, 3, 4, 'AB']:
    print(v, end=' ')       # test 1: 1 2 3 4

# 열거형 자료가 따로 없고 단순히 회수 만을 지정하고 싶을 때는 range() 함수를 사용한다.
# 이 함수는 열거형 자료를 직접 반환하는 것은 아니지만(속도 문제 때문에)
# 유사한 효과를 발생하여 원하는 회수만큼 loop를 수행할 수 있게 한다.

# 파이썬에 내장된 range 함수는 이러한 숫자의 나열을 생성한다.
# 여기서는 range 함수에 두 개의 숫자[start, end)를 넣어 주었으며, 그러면 이 함수는 첫 번째 숫자(start) 이상,
# 그리고 두 번째 숫자(end) 미만까지의 숫자 목록(리스트)을 반환한다. 
#
# range(1,5) 는 리스트 [1, 2, 3, 4]를 반환하는 것과 같은 효과를 낸다.
# 즉, for i in range(1, 5) 는 for i in [1, 2, 3, 4] 와 같은 효과를 낸다.
# range(1, 5, 2) 는 2는 증분을 의미하므로 [1,3]을 반환하는 것과 같은 효과를 낸다.
# 즉 range(시작값, 끝값+1) 혹은 range(시작값, 끝값+1, 증분)의 형식을 갖는다고 할 수 있다.

print('\ntest 2: ', end='')
for i in range(1, 5):
    print(i, end=' ')       # test 1: 1 2 3 4

print()
for i in range(5):
    print(i, end=' ')       # 1 2 3 4


print('\ntest 3: ', end='')
for i in range(1, 10, 2):   # 초기값 1에서 10미만까지 2씩 증가시킨다.
    print(i, end=' ')       # test 3: 1 3 5 7 9

print('\ntest 4: ', end='')
for i in [1, 'Hello', 8, 'A', 0]:
    print(i, end='  ')      # test 4: 1  Hello  8  A  0 

# 실제로 range 함수가 리스트를 반환하는 것은 아니다.
# 리스트 데이터를 얻고자 하면 실제로는 range 함수에 list() 함수를 취해서 결과를 반환받아야 한다.
# range 객체를 그대로 사용하면 for 문에서 필요할 때마다 값을 i라는 변수가 바인딩해서 사용하게 되지만
# 리스트 객체로 변환하면 모든 범위의 값을 한 번에 리스트로 만들어서 저장하기 때문에 더 큰 메모리가 필요해진다.
# 메모리 절약, 속도 문제 때문에 단순 카운팅의 용도라면 list 객체보다는 range 객체를 쓰는 것이 합리적이다.

x = range(1, 5)
print('\ntest 5: ', x, type(x))     # test 5:  range(1, 5) <class 'range'>

xx = list(x)
print('test 6: ', xx, type(xx))     # test 6:  [1, 2, 3, 4] <class 'list'>

exit(0)
"""

"""
#---------------------------------------------------------------------------------------------------
# 실습 4 - break 문
#   break 문은 루프 문을 강제로 빠져나올 때,
#   즉 아직 루프 조건이 `False`가 되지 않았거나 열거형의 끝까지 루프가 도달하지 않았을 경우에
#   해당 루프 문의 실행을 강제로 정지시키고 싶을 때 사용된다.
#
#   만약 break 문을 써서 for 루프나 while 루프를 빠져나왔을 경우,
#   그 루프에 딸린 else 블록은 실행되지 않는다.

# 동작 설명(2번째 예제): 2중 loop로 구성되어 있다.
#   q를 입력하면 해당 loop를 종료하여 그 다음 2회 수행하는 loop를 수행한다.
#   결국 break 명령은 해당 loop만 종료시키는 것을 알 수 있다.
#---------------------------------------------------------------------------------------------------
"""
"""
# 이것보다는 아래의 예제가 더 좋을 것 같다.
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break           # 'quit'를 입력하여 이곳에 오면 while문을 빠져 나간다.
    else:
        print('Hey. I am here.')
    print('Length of the string is', len(s))
print('Done')
"""

"""
t = 0
while t < 2:        # 2회의 inner loop를 수행한다. 즉 q를 2번 맞추면 종료한다.
    while True:
        s = input('Enter something : ')
        if s == 'q':
            break           # 'q'를 입력하여 이곳에 오면 내부의 첫번 째 while문을 빠져 나간다.
        else:
           print('..Wrong.')
    t += 1
    print(f'Right! t={t}')
print('Done')
exit(0)
"""


"""
#---------------------------------------------------------------------------------------------------
# 실습 5 - continue 문
#   continue 문은 현재 실행중인 루프 블록의 나머지 명령문들을 실행하지 않고
#   곧바로 다음 루프로 넘어가도록 한다.
# 동작설명:
#   임의의 문자열을 입력받는다.
#   그 문자열의 길이가 3 미만이면 Too small 문자열을 출력한 후 루프 블록의 나머지 명령문들을 실행하지 않고
#   새로운 루프를 시작한다.
#---------------------------------------------------------------------------------------------------

while True:
    s = input('Enter something : ')     # 키입력을 스트링으로 받는다.
    if s == 'quit':
        break                           # looping을 중지.
    if len(s) < 3:                      # 입력받은 문자열의 길이가 3글자 미만인지 점검.
        #continue                       # 이곳에 continue문을 넣으면 어떻게 되는지 예측하시오.
        print('Too small')
        continue
    print('Input is of sufficient length')
print('Done')

"""

