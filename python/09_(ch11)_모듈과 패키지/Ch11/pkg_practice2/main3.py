
import calcpkg.geometry2 as gm  # 'calcpkg.geometry2' 출력됨

print(gm.triangle_area(30, 40))  # geometry 모듈의 triangle_area 함수 사용
print(gm.rectangle_area(30, 40))  # geometry 모듈의 rectangle_area 함수 사용

import calcpkg.geometry2    # 한번 더 로드하였으나 메시지는 출력되지 않음
print(calcpkg.geometry2.triangle_area(30, 40))  # geometry2 모듈의 triangle_area 함수 사용
print(calcpkg.geometry2.rectangle_area(30, 40))  # geometry2 모듈의 rectangle_area 함수 사용



# add_path.py를 수행하여 경로를 추가하고 나면 수행가능합니다.
# 디버깅 미 완료: 현재 만족하게 동작하지 않습니다.!!!!!
# 모듈/패키지의 경로 추가하기

import sys
print(sys.path)     # 현재 설치된 경로 보이기

# 경로 추가하기
sys.path.append('D:\\pkg_practice3\\calcpkg3')
sys.path.append('D:\\calcpkg3')
print(sys.path)     # 현재 설치된 경로 보이기

import calcpkg.geometry2 as gm  # 'calcpkg.geometry2' 출력됨

print(gm.triangle_area(30, 40))  # geometry 모듈의 triangle_area 함수 사용
print(gm.rectangle_area(30, 40))  # geometry 모듈의 rectangle_area 함수 사용

