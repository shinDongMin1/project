from collections import defaultdict
d = defaultdict(tuple)      # 초깃값이 tuple로 선언된 defaultdict의 선언
print(type(d), d)       # <class 'collections.defaultdict'> defaultdict(<class 'tuple'>, {})

d = defaultdict(float)      # 초깃값이 float로 선언된 defaultdict의 선언
print(type(d), d)       # <class 'collections.defaultdict'> defaultdict(<class 'float'>, {})



# 다음 리스트에서 칼라별 수량의 합산을 구하시오.
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)       # 초깃값이 list로 선언된 defaultdict의 선언
print(type(d), d)
# <class 'collections.defaultdict'> defaultdict(<class 'list'>, {})

for k, v in s:
    d[k].append(v)      # key=k 자료의 value로서 list에 대해 v를 추가한다.

print(d)
# defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})

t = {}
for k, v in d.items():
    t[k] = sum(v)
print(t)
# {'yellow': 4, 'blue': 6, 'red': 1}

print(d.items())
#[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]


exit(0)









"""
from collections import defaultdict

# 다음 리스트에서 칼라별 수량의 합산을 구하시오.
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
print(type(d), d)
# <class 'collections.defaultdict'> defaultdict(<class 'list'>, {})

for k, v in s:
    d[k].append(v)

print(d.items())
#[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
print(d)

exit(0)
"""







"""
# 3. defaultdict 사용
from operator import itemgetter
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

t = defaultdict(int)
for k, v in s:
    t[k] += v

print(sorted(t.items(), key=itemgetter(1)))

# 출력 결과
#[('red', 1), ('yellow', 4), ('blue', 6)]
"""
