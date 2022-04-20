# 컴맨드 창에서 pip로 설치한 패키지의 파이썬 path 알아내기
# python -m site --user-site
# ==> 실험 결과: 파이썬 설치 위치를 바꾸니까 실제로는 존재하지 않는 폴더를 보여주었다.

# 프로그램 상에서 pip로 설치한 패키지의 파이썬 path 알아내기
import site
print(site.getsitepackages())
# ['C:\\Python\\Python3.7.0', 'C:\\Python\\Python3.7.0\\lib\\site-packages']

# 모듈/패키지의 경로 추가하기
import sys
print(sys.path)     # 현재 설치된 경로 보이기
exit(0)

# 경로 추가하기
sys.path.append('D:\\pkg_practice3\\calcpkg')
print(sys.path)     # 현재 설치된 경로 보이기





