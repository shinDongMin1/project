"""

사전형 자료 연습

"""

"""
# ---------------------------------------------------------------------------------------------------------------
# 실습 0: 사전형 자료 생성
# ---------------------------------------------------------------------------------------------------------------

a = {1:'A', 2:'C'}; print(1, type(a), a)
a = dict(a1='A', a2='C'); print(2, type(a), a)  # 1='A'. 2='B'은 안됨.
a = dict(zip([1, 3], [6, 9])); print(3, type(a), a)
a = dict([(1, 'A'), ('B', 7)]); print(4, type(a), a)

for i, j in zip([1, 3], [6, 9]):
    print(i, j)

exit()
"""



#"""
# ---------------------------------------------------------------------------------------------------------------
# 실습 1: 사전형 자료 생성 및 조작 연습
# dict 자료 생성 -> dict 자료로 key list와 value list로 분리된 list 생성 -> 2개의 list로 dict 자료 복원
# ---------------------------------------------------------------------------------------------------------------
#code = {'America': 1, 'Korea': 82, 'China': 86}

# 사전형 자료 code를 생성한다.
code = {100: 'KT', 101: 'LG', 106: 'SK', 112: 'Crime', 119: 'Emergency'}
print('1) code: ', type(code), '|', code)
# 1) code:  <class 'dict'> | {100: 'KT', 101: 'LG', 106: 'SK', 112: 'Crime', 119: 'Emergency'}

# keys() 메소드로 사전형 자료에서 key 원소를 리스트 형태를 반환받는다.
d_keys = code.keys()
print('2) code.keys(): ', type(d_keys), d_keys)
# 2) code.keys():  <class 'dict_keys'> dict_keys([100, 101, 106, 112, 119])

# 리스트 자료로 변환한다.
a = list(d_keys)

# values() 메소드로 사전형 자료에서 value 원소를 리스트 형태를 반환받는다.
d_values = code.values()
print('3) code.values: ', type(d_values), d_values)
# 3) code.values:  <class 'dict_values'> dict_values(['KT', 'LG', 'SK', 'Crime', 'Emergency'])

# 리스트 자료로 변환한다.
b = list(d_values)

# key와 value로 이루어진 2개의 list로 부터 사전형 자료를 복원한다.
code_2 = dict(zip(a, b))
print('4) dict(zip(a, b)): ', type(code_2), '|', code_2)
# 4) dict(zip(a, b)):  <class 'dict'> | {100: 'KT', 101: 'LG', 106: 'SK', 112: 'Crime', 119: 'Emergency'}

# items() 메소드로 사전형 자료로 부터 dict_items 자료를 반환받는다.
d_items = code.items()
print('5) code.items: ', type(d_items), '|', d_items)
# 5) code.items:  <class 'dict_items'> | dict_items([(100, 'KT'), (101, 'LG'), (106, 'SK'), (112, 'Crime'), (119, 'Emergency')])

# dict_items 자료를 list 자료로 변환한다.
print('6) list(code.items): ', type(list(code.items())), '|', list(code.items()))
# 6) list(code.items):  <class 'list'> | [(100, 'KT'), (101, 'LG'), (106, 'SK'), (112, 'Crime'), (119, 'Emergency')]

# 번외: 사전형 자료를 list로 변환하면 key만 반환한다.
# value를 리스트로 반환 받으려면? : list(code.values())
print(list(code))
# [100, 101, 106, 112, 119]

print(list(code.values()))
# ['KT', 'LG', 'SK', 'Crime', 'Emergency']

#"""

# 사전형 자료 code를 생성한다.
code = {100: 'KT', 101: 'LG', 106: 'SK', 112: 'Crime', 119: 'Emergency'}
print('1) code: ', type(code), '|', code)

# keys() 메소드로 사전형 자료에서 key 원소를 리스트 형태를 반환받는다.
d_keys = code.keys()
print('2) code.keys(): ', type(d_keys), d_keys)

# 리스트 자료로 변환한다.
a = list(d_keys)

# values() 메소드로 사전형 자료에서 value 원소를 리스트 형태를 반환받는다.
d_values = code.values()
print('3) code.values: ', type(d_values), d_values)

# 리스트 자료로 변환한다.
b = list(d_values)

# key와 value로 이루어진 2개의 list로 부터 사전형 자료를 복원한다.
code_2 = dict(zip(a, b))
print('4) dict(zip(a, b)): ', type(code_2), '|', code_2)

# items() 메소드로 사전형 자료로 부터 dict_items 자료를 반환받는다.
d_items = code.items()
print('5) code.items: ', type(d_items), '|', d_items)

# dict_items 자료를 list 자료로 변환한다.
print('6) list(code.items): ', type(list(code.items())), '|', list(code.items()))

# 번외: 사전형 자료를 list로 변환하면 key만 반환한다.
# value를 리스트로 반환 받으려면? : list(code.values())
print(list(code))
# [100, 101, 106, 112, 119]

print(list(code.values()))
# ['KT', 'LG', 'SK', 'Crime', 'Emergency']
