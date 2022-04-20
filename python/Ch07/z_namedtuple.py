# ----------------------------------------------------------------------------------------------------------------
# 실습 1: namedtuple 컬렉션 모듈 활용하기
# ----------------------------------------------------------------------------------------------------------------

# --- 1. index로 요소 접근하기
print('\n1. access by tuple index ---------------------------------')
bob = ('Bob', 30, 'male')
print('1) Representation:', bob)

jane = ('Jane', 29, 'female')
print('2) Field by index:', jane[0])     # index로 접근

print('3) Fields by index:')
for p in [bob, jane]:
    #print('%s is a %d year old %s' % p)
    print(f'{p[0]} is a {p[1]} year old {p[2]}')


# --- 2. 컬렉션 모듈로 해결하기. 이름으로 접근
print('\n2. access by tuple name ---------------------------------')
import collections

# namedtuple: 튜플 자료를 index로 접근하지 않고 항목에 붙은 이름으로 접근할 수 있게 한다.
Person = collections.namedtuple('Person', 'name age gender')
print('1) Type of Person:', type(Person), '\n| Person=', Person)

bob = Person(name='Bob', age=30, gender='male')
print('2)', type(bob))
print('3) bob=', bob.name, bob.age, bob.gender)

jane = Person(name='Jane', age=29, gender='female')
her = Person('Suji', 26, 'female')
print('4) her=', her.name, her.age, her.gender)

print('\n5) Fields by index:')
for p in [bob, jane, her]:
    print('%s is a %d year old %s' % p)

print('\n6) Access by name:')
for p in [bob, jane, her]:
    print(f'{p.name} is a {p.age} year old {p.gender}')
