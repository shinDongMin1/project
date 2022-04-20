"""

람다 함수는 입력파라미터와 수행표현식만 제시하는 1줄 짜리 anonymous function이다.
(함수의 이름은 안 밝히고,) argument만 전달하면 실제 수행되는 루틴은 expression이다.
표현 식 =>  lambda arguments: expression


"""


# 이름 없는 함수의 수행 결과를 출력한다.
# 그 함수는 입력받은 데이터를 1 증가시켜 반환하는 동작을 수행한다.

print((lambda x: x + 1)(2))  # (lambda x: x + 1)=>함수이름, (2)=> 인자=2
# arguments=x, expression=x+1
# (lambda x: x + 1)(2) = lambda 2: 2 + 1
#                      = 2 + 1

add_one = lambda x: x + 1   # 함수이름을 add_one으로 명시하였다고 생각할 수 있음.
print(add_one(2))

# 2개의 인자를 갖는 람다 함수를 full_name으로 정의한다.
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))
#'Full name: Guido Van Rossum'