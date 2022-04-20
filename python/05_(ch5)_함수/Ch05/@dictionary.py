"""
사전형 자료 사전학습


Dictionary 자료형은 { .. }로 표현되며, 내부 구성요소는 key: value로 구성된다.
    Dic = {Key1:Value1, Key2:Value2, Key3:Value3, ...}
    student = {1: 'Tom', 2: 'Nancy', 3:'Jane' }
딕셔너리 타입은 immutable한 키(key)와 mutable한 값(value)으로 구성된 원소가 순서가 없이 나열된 집합이다.
순서가 없기 때문에 인덱스로는 접근할 수 없고, 키로 접근한다.

"""

#"""
# -----------------------------------------------------------------------------------------------------------
# 실습 1 - 사전 자료의 정의
# 사전 자료는 '키:값'으로 구성된 원소를 컴마로 나열하고, {중괄호}로 둘러쌓아 정의한다.
# 사전형 자료를 액세스 할 때는 '자료형_이름[key]'을 이용해 value를 액세스한다.
# value는 바꿀 수 있지만 key는 바꿀 수 없다.
# -----------------------------------------------------------------------------------------------------------

# 1) key=정수, value='string'인 사전 자료의 사례
student = {1: 'Tom', 2: 'Nancy', 3: 'Jane' }
print(type(student))        # => <class 'dict'>
print(student[2])           # => Nancy. 인덱스로 key 값이 사용된다.
student[2] = 'JH'           # value can be mutable. value 요소는 바꿀 수 있다.
print(student[2])           # JH
#print(type(student[4]), student[4])     # => 오류!!! 수행 중지. KeyError: 4

# 2) key='string', value=정수인 사전 자료의 사례
food = {'carrot': 2000, 'egg': 500 }
print(type(food))           # <class 'dict'>
print(food['egg'])          # => 500

# 3) key, value  자료형이 여러 가지인 사례
things = {10: 345, 'abc': 'efg', 3.14: 3, 'qwe': [1, 2, 'a'] }
print(things[10])           # 345
print(things['abc'])        # efg
print(things[3.14])         # 3
print(things['qwe'])        # [1, 2, 'a']

# 4) value의 자료 형이 사전자료인 사례
dic_super = {'a': student, '1': food, 5.1: things}
print(dic_super['a'])           # => {1: 'Tom', 2: 'JH', 3: 'Jane'}
print(dic_super['1'])           # => {'carrot': 2000, 'egg': 500}
print(dic_super[5.1]['qwe'])    # [1, 2, 'a']

exit(0)
#"""



# -----------------------------------------------------------------------------------------------------------
# 실습 2 - 사전 자료의 정의
# 사전 자료를 value 원소로 갖는 사전 사료를 분석한다.
# -----------------------------------------------------------------------------------------------------------


items = {'pen': 500, 'food': {'carrot': 2000, 'egg': 500 }, 'student': {1: 'Tom', 2: 'Nancy', 3:'Jane' },
         'subjet': ['math', 'English', 'science'] }
print(type(items), '\n', items)         # <class 'dict'>

# dict() = 빈 dictionary를 선언하는 함수
print(dict(), type(dict()))          # {} <class 'dict'>

# key들만 반환하는 메소드 keys()
print(items.keys())         # dict_keys(['pen', 'food', 'student', 'subjet'])
print(list(items.keys()))   # ['pen', 'food', 'student', 'subjet']

# value만 반환하는 메소드 values()
print(items.values())
# dict_values([500, {'carrot': 2000, 'egg': 500}, {1: 'Tom', 2: 'Nancy', 3: 'Jane'}, ['math', 'English', 'science']])
print(list(items.values()))
# [500, {'carrot': 2000, 'egg': 500}, {1: 'Tom', 2: 'Nancy', 3: 'Jane'}, ['math', 'English', 'science']]

# key:value를 tuple로 묶어 반환하는 메소드 items()
print(list(items.items()))
# [('pen', 500), ('food', {'carrot': 2000, 'egg': 500}), ('student', {1: 'Tom', 2: 'Nancy', 3: 'Jane'}), ('subjet', ['math', 'English', 'science'])]


print()
print('key:', '---type(value)------ value------')
for key in items:
    value = items[key]
    print(key, ':', type(value), value)
    if type(value) is type(dict()):
        print('             sub item=', key)
        for k in value:
            print('             sub key=', k,': sub value=', value[k])

