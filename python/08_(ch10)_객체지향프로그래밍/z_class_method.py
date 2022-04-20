
"""
# ---------------------------------------------------------------------------------
# 실습 1: 클래스 메서드
# 클래스 이름으로 호출하는 메서드 중 클래스 변수를 접근하는 메서드를  클래스 메서드라 한다.
# ---------------------------------------------------------------------------------


class Person:
    count = 0    # 클래스 속성의 변수

    def __init__(self):
        Person.count += 1

    @classmethod        # 호출방식: Person.print_count()
    def print_count(cls):
        print('{0}명 등록되었습니다.'.format(cls.count))    # cls로 클래스 속성에 접근

    # 클래스변수는 인스탄스 메서드에서도 접근 가능하다.
    # 호출방식: instance.print_count_with_inst()
    def print_count_with_inst(self):
        print(Person.count)

james = Person()
maria = Person()
Person.print_count()    # 2명 등록되었습니다.
Person.count = 4
Person.print_count()    # 4명 등록되었습니다.
maria.print_count_with_inst()
#Person.print_instance()     # instance를 제공하지 않아서 안됨.


#print('more')
#james.print_count()
#maria = Person()
#maria.print_count()

exit(0)
"""

"""
# ---------------------------------------------------------------------------------
# 실습 2 - 클래스 메서드와 비공개 클래스 변수의 활용
# 비공개 클래스 속성 변수(__count)를 사용하여 클래스 외부의 접근을 차단하기
# ---------------------------------------------------------------------------------

class Person:
    __count = 0     # 비공개(private) 클래스 속성 변수

    def __init__(self):
        Person.__count += 1

    @classmethod    # 아래 메서드는 클래스 이름으로 호출할 수 있다.
    def print_count(cls):   # cls.__count = Person.__count
        print('{0}명 등록되었습니다.'.format(cls.__count))


james = Person()
maria = Person()
Person.print_count()    # 2명 등록되었습니다.

# 비공개 클래스 속성의 변수를 외부에서 액세스 할 수 없다.
#Person.__count = 4      # 1) 새 변수를 선언한 것과 같음. 적용 안됨.

# 1)의 문장의 수행 여부에 따라 2)번 문장의 수행여부가 달라진다.
# 1)을 수행하면 정상 수행. => 4를 출력한다.
# 1)을 주석 처리하면 오류 발생(type object 'Person' has no attribute '__count')
print('Person.__count=', Person.__count)    # 2) 클래스변수의 값을 출력

Person.print_count()    # 2명 등록되었습니다.

exit(0)
"""


# ---------------------------------------------------------------------------------
# 실습 3 - 인스턴스 생성해주는 함수 cls()
# class method에서 호출하면 인스턴스를 생성해 반환해 줄 수 있다.
# ---------------------------------------------------------------------------------

class Person:
    __count = 0     # 비공개 클래스 속성

    def __init__(self):
        Person.__count += 1
        #print('Person.__count=', Person.__count)

    @classmethod
    def print_count(cls):   # cls로 클래스 속성에 접근
        print('{0}명 등록되었습니다.'.format(cls.__count))
        #print('{0}명 등록되었습니다.'.format(Person.__count))

    @classmethod
    def create(cls):
        print('create method is called.')
        p = cls()    # cls()로 인스턴스 생성
        return p

    def pr_count(self):
        print('Person.__count=', Person.__count)


james = Person()    # __count = 1
maria = Person()    # __count = 2
jh = Person.create()    # instance jh 생성
Person.print_count()    # 3명 등록되었습니다.
jh.pr_count()           # Person.__count= 3

exit()





#"""
# ---------------------------------------------------------------------------------
# 실습 4 - 인스턴스 생성해주는 함수 cls()
# class method에서 호출하면 인스턴스를 생성해 반환해 줄 수 있다.
# ---------------------------------------------------------------------------------

class Person:
    __count = 0     # 비공개 클래스 속성
    id = 'person class'

    def __init__(self):
        Person.__count += 1
        print('Person.__count=', Person.__count)

    @classmethod
    def print_count(cls):
        print('{0}명 등록되었습니다.'.format(cls.__count))    # cls로 클래스 속성에 접근
        #print('{0}명 등록되었습니다.'.format(Person.__count))

    @classmethod
    def create(cls):
        print('create method is called.')
        p = cls()    # cls()로 인스턴스 생성
        return p

james = Person()
maria = Person()
jh = Person.create()
Person.print_count()    # 3명 등록되었습니다.


print(jh.id)
Person.id = 'New'
print(Person.id)
james.id = 'james'
print(james.id)
print(jh.id)
#"""



