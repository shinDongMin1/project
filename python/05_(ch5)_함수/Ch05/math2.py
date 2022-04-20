import math

# 2차 방정식, a * x**2 + b * x + c = 0의 근의 공식
#  x= (-b + math.sqrt(b ** 2 - (4 * a * c)) ) / (2 * a),
#  x= (-b - math.sqrt(b ** 2 - (4 * a * c)) ) / (2 * a)
def get_result_quadratic_equation(a, b, c):
    values = []
    values.append((-b + math.sqrt(b ** 2 - (4 * a * c)) ) / (2 * a))
    values.append((-b - math.sqrt(b ** 2 - (4 * a * c)) ) / (2 * a))
    return values

print(get_result_quadratic_equation(1,-2,1))            # (a, b. c)
