
import calcpkg.geometry2 as gm  # 'calcpkg.geometry2' 출력됨

print(gm.triangle_area(30, 40))  # geometry 모듈의 triangle_area 함수 사용
print(gm.rectangle_area(30, 40))  # geometry 모듈의 rectangle_area 함수 사용

import calcpkg.geometry2    # 한번 더 로드하였으나 메시지는 출력되지 않음
print(calcpkg.geometry2.triangle_area(30, 40))  # geometry2 모듈의 triangle_area 함수 사용
print(calcpkg.geometry2.rectangle_area(30, 40))  # geometry2 모듈의 rectangle_area 함수 사용



