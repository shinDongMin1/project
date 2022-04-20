"""

orderedDict() 자료형 연습
    일반 dict 자료는 수행할 때마다 내부 자료의 순서가 바뀔 수 있지만
    OrderedDict은 일단 저장해 놓으면 내부 자료의 순서가 바뀌지 않는다.

자료가 만들어지면 sorted() 함수를 통해 정렬해 놓으면 순서대로 정렬된 자료를 참조할 수 있다.

참고:
    일반 사전형(dict)은 내부의 자료값만 같으면 동일하다고 판단하지만,
    순서를 기억하는 사전형(OrderedDict)은 내부의 자료값 뿐만 아니라 입력된 순서까지 같아야 동일한 것으로 판단한다.

defaultdict is faster for larger data sets with more homogenous key sets
    (ie, how short the dict is after adding elements);
setdefault has an advantage with more heterogeneous key sets; ...
Python 3.6's dict is now ordered by insertion order (reducing the usefulness of OrderedDict)

"""

# -------------------------------------------------------------------------------------------------------
# 교재의 내용을 다소 변경
# -------------------------------------------------------------------------------------------------------

from collections import OrderedDict         #OrderedDict 모듈 선언

d = dict()
d['d'] = 100; d['c'] = 200; d['B'] = 300; d['a'] = 500
print(f'1.1) {type(d)}\n{d}')
# 1) <class 'dict'>
# {'d': 100, 'c': 200, 'B': 300, 'a': 500}

# (key, value) 중에서 index 0라 함은 key가 소팅의 판단기준이 된다.
sd = sorted(d.items(), key=lambda abc: abc[0])
print(f'2) {type(sd)}\n{sd}')
# 2) <class 'list'>
# [('B', 300), ('a', 500), ('c', 200), ('d', 100)]

od = OrderedDict(sd)
print(f'3) {type(od)}\n{od}')
# 3) <class 'collections.OrderedDict'>
# OrderedDict([('B', 300), ('a', 500), ('c', 200), ('d', 100)])

for k, v in od.items():
    print(k, v, end=' ')
# B 300 a 500 c 200 d 100
# 줄번호 33에서 abc[0] -> abc[1]으로
# 고쳐 적으면 정렬 기준은 value가 된다.
# d 100 c 200 B 300 a 500

