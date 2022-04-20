"""
class initializer, __init__
     Initializer는 클래스로부터 객체를 만들 때, 인스턴스 변수를 초기화하거나 객체의 초기상태를 만들기 위한 동작을 수행한다.
    다른 객체지향 언어에서는 생성자(constructor)와 유사한 역할을 수행한다.
    instance variable : 객체를 생성할 때마다 따로 만들어진다.
"""


#"""


class Person:
    # self는 객체 자신을 참조한다.
    def __init__(self, ame='JH'):
        self.name = ame

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Swaroop')   # ame='Swaroop'로 입력.
# 자동 호출되는 __init__ 함수에서 self.name 변수가 초기화 된다.
p.say_hi()

Person('Tom').say_hi()  # 위의 2줄을 한줄로 표시한 것.
Person().say_hi()   # 역시 1줄로 표시한 것. 단, ame는 default 값 사용.

p = Person('홍길동')   # p 객체를 생성한다.
Person.say_hi(p)    # p 객체를 self 객체에 넘긴다.

print(p.name)   # instance variable 출력

exit()


#"""


class Person:
    def __init__(self, name1='JH'):
        self.name = name1  # name = instance variable.

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Swaroop')
p.say_hi()
Person().say_hi()   # => p2 = Person(); p2.say_hi()
Person.say_hi(p)    # Class.method(self, argv1,..)
Person('Kim').say_hi()
print(p.name)

