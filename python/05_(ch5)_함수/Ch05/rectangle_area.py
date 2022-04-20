def calculate_rectangle_area(x, y):
    return x * y


rectangle_x = 10
rectangle_y = 20
print("사각형 x의 길이:", rectangle_x)
print("사각형 y의 길이:", rectangle_y)

# 넓이를 구하는 함수 호출
print("\n사각형의 넓이:", calculate_rectangle_area(rectangle_x, rectangle_y))


# ------------------------------------------------------------------------------------------
# 추가 실습: 같은 이름으로 다신 선언하기
# 함수는 중복 선언이 가능하다.... 맨 나중에 선언한 함수가 유효하다.
# ------------------------------------------------------------------------------------------
def calculate_rectangle_area(x, y):
    return x + y


# 넓이를 구하는 함수 호출
print("\n사각형의 넓이:", calculate_rectangle_area(rectangle_x, rectangle_y))

print(type(calculate_rectangle_area))

# ------------------------------------------------------------------------------------------
# 파이썬에 내장된 함수도 선언 가능하다.
# ------------------------------------------------------------------------------------------


def print(x, y): #오버로딩 재정의
    return x + y


a = type(print)     # a = <class 'function'>
q = print(2, 3)     # q = 5가 반환되지만, 출력되는 것은 없다.
                     
del print           # 함수를 지운다. 이로서 내장 함수 정의가 살아난다.

print(type(print), a, q)    # <class 'builtin_function_or_method'> <class 'function'> 5



