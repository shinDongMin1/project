# 2차 방정식, a * x**2 + b * x + c = 0의 근의 공식
#  x= (-b + math.sqrt(b ** 2 - (4 * a * c)) ) / (2 * a),
#  x= (-b - math.sqrt(b ** 2 - (4 * a * c)) ) / (2 * a)

import math
a = 1; b = -2; c = 1

print((-b + math.sqrt(b ** 2 - (4 * a * c)) ) / (2 * a))
print((-b - math.sqrt(b ** 2 - (4 * a * c)) ) / (2 * a))
