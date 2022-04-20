
# 실습 0: 교과서 원본 실험
for looper in range(5):
    print("hello")


# 실습 1: range() 함수와 sequence 자료형(iterable)에 대하여...

# range() 함수는 자체의 자료형으로 취급된다.
a = range(5)
print(f'a = range(5): type(a)={type(a)}, a={a}')
# a = range(5): type(a)=<class 'range'>, a=range(0, 5)

# range 자료형은 list나 tuple로 바꿀 수 있다.
# sequence 자료형: <class 'range'>, <class 'list'>, <class 'tuple'>, <class 'string'>
# sequence 자료형은 모두 iterable_object이다.
# 따라서 "for k in iterable_object" 구문에 사용될 수 있다.

l = list(a)
print(f'l = list(a): type(l)={type(l)}, len(l)={len(l)}, l={l}')
# l = list(a): type(l)=<class 'list'>, len(l)=5, l=[0, 1, 2, 3, 4]

t = tuple(a)
print(f't = list(a): type(t)={type(t)}, len(t)={len(t)}, t={t}')
# t = list(a): type(t)=<class 'tuple'>, len(t)=5, t=(0, 1, 2, 3, 4)
