""""
튜플로 반환하는 함수의 반환값에 대해 고찰한다.

"""


def f1(a): return a, a * 2, a / 2
def f2(a): return [a, a * 2, a / 2]
def f3(a): return list((a, a * 2, a / 2))
def f4(a): return (a, )     # =return tuple((a, ))


ret = f1(10); print(1, type(ret), ret)
ret = f2(10); print(2, type(ret), ret)
ret = f3(10); print(3, type(ret), ret)
ret = f4(10); print(4, type(ret), ret)
a, b, c = f2(10); print(a, b, c)