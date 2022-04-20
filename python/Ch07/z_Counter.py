from collections import Counter
# Counter는 열거형 자료의 원소의 갯수를 사전형 자료로 반환해 주는 함수이다.

# -------------------------------------------------------------------------------
# 실습 1: 문자열의 글자수 세기
# 리스트나 문자열과 같은 시퀀스 자료형 안의 요소 중 값이 같은 것이 몇 개 있는지 확인한다.
# -------------------------------------------------------------------------------
"""
#a = 'Seokyeong university'

a = 'gallahad'
text = list(a)
print('1)', text)

cnt = Counter(text)
print(f'2) {type(cnt)}\n{cnt}')
print('3)', cnt['e'], cnt['a'] )

d = dict(cnt)
print('4)', type(d), d)


exit(0)
"""



"""
# -------------------------------------------------------------------------------
# 실습 2: 1) dict 자료 혹은 2) keyword=수량 지정을 이용하여 필요 수량 만큼의 리스트 원소 생성하기
# -------------------------------------------------------------------------------

dic = {'eagle': 3, 'tiger': 1, 'horse': 2}
print(1, type(dic), dic)
# 1 <class 'dict'> {'eagle': 3, 'tiger': 1, 'horse': 2}

c = Counter(dic)                       # 1)  dict 자료 지정
# Counter({'eagle': 3, 'horse': 2, 'tiger': 1})

print(2, c)
# 2 Counter({'eagle': 3, 'horse': 2, 'tiger': 1})

a = list(c.elements())
print(3, a)
# 3 ['eagle', 'eagle', 'eagle', 'tiger', 'horse', 'horse']

c = Counter(cats=2, dogs=3)             # 2) keyword=수량 지정
print(4, c)
# 4 Counter({'dogs': 3, 'cats': 2})

a = list(c.elements())
print(5, a)
# 5 ['cats', 'cats', 'dogs', 'dogs', 'dogs']

exit(0)
"""



# -------------------------------------------------------------------------------
# 실습 3: 카운터 모듈의 사칙 연산
# -------------------------------------------------------------------------------

a = Counter(a=4, b=3, c=5, d=-5)
b = Counter(a=-1, b=2, c=0, d=4)
c = Counter(a=-9, b=2, c=-1, d=4)

print(1, a.subtract(b))     # None. 반환값 없음
print(2, 'a=', a)
# a= Counter({'a': 5, 'c': 5, 'b': 1, 'd': -9})

print(3, 'b+c=', b+c)
# b+c= Counter({'d': 8, 'b': 4})
# + 연산은 두 Counter 객체에 있는 각 요소를 더한 것.
# 수가 음수이면 원소에서 사라진다.

print(4, 'a+b=', a+b)
# a+b= Counter({'c': 5, 'a': 4, 'b': 3})
# 'd' 원소가 없어졌다? 음수이므로...

print(5, 'a & b=', a & b)
# a & b= Counter({'b': 1})






