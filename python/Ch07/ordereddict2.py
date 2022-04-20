"""

An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted.
A regular dict doesn't track the insertion order, and iterating it gives the values in an arbitrary order.
... By contrast, the order the items are inserted is remembered by OrderedDict.

"""



from collections import OrderedDict         #OrderedDict 모듈 선언

#
# OrderedDict로 선언한 사전형자료는 입력 순서를 기억하여 나열되는 것이 보장된다.
# 본 예제로는 그것을 증명하여 보여주지는 못하고 있다.

d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

print(d)        # 자료 순서가 바뀔 수 있다 함.
# OrderedDict([('x', 100), ('y', 200), ('z', 300), ('l', 500)])

for k, v in d.items():
    print(k, v)
# x 100
# y 200
# z 300
# l 500