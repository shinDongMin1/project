from collections import defaultdict

# lambda: 0는 return 0로 이해한다.
# 즉, 어떤 파라미터가 들어오더라도 0을 반환한다는 것이다.
d = defaultdict(lambda: 0)  # Default 값을 0으로 설정

print(d["first"])       # 0
print(d[3])             # 0
print(type(d), len(d))
# <class 'collections.defaultdict'> 2

d = defaultdict()
print(type(d), len(d))
# <class 'collections.defaultdict'> 0

print(d[3])     # 수행 오류 발생. KeyError: 3
# 초기화를 미리 행해두지 않으면 defaultdict라 해도 접근 오류가 발생한다.