"""

orderedDict() 자료형 연습
    일반 dict 자료는 수행할 때마다 내부 자료의 순서가 바뀔 수 있지만
    OrderedDict은 일단 저장해 놓으면 내부 자료의 순서가 바뀌지 않는다.

"""




# -------------------------------------------------------------------------------------------------------
# 교재 원본
# 본 예제를 분석하기 전에 z_prcatice_sorted.py 프로그램을 통해 sorted() 함수의 용법을 익힌 후에 검토하기 바랍니다.
# -------------------------------------------------------------------------------------------------------

def sort_by_key(t):     # (key, value) 중에서 index 0라 함은 key가 소팅의 판단기준이 된다.
    return t[0]         # 즉, x, y, z, l이 소팅의 기준이 된다.

from collections import OrderedDict         #OrderedDict 모듈 선언

d = dict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

print(d)
# {'x': 100, 'y': 200, 'z': 300, 'l': 500}

for k, v in OrderedDict(sorted(d.items(), key=sort_by_key)).items():
    print(k, v)
# l 500
# x 100
# y 200
# z 300
