
# ---------------------------------------------------
# 실습 1: 외부 모듈의  class를 import 하여 활용한다.
# ---------------------------------------------------
from inheritance1 import Person
#from inheritance2 import Employee  # 이것도 OK
from inheritance2 import *

taylor = Person('Taylor', 24, 'male')

e1 = Employee('Jane', 20, 'female', 300, '20190104')
e1.do_work()
e1.about_me()

exit()



# ---------------------------------------------------
# 실습 2: 외부 모듈 없이 자체의 자식, 부모 함수로 구성한 프로그램
# ---------------------------------------------------

class Person(object):                       # 부모 클래스 Person 선언. (object)빼고 선언해도 됨.
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self):                     # 메서드 선언
        print("저의 이름은", self.name, "이고요, 제 나이는", str(self.age), "살입니다.")


class Employee(Person):                                             # 부모 클래스 Person으로부터 상속
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender)                         # 부모 객체 사용
        self.salary = salary
        self.hire_date = hire_date                                  # 속성값 추가

    def do_work(self):                                              # 새로운 메서드 추가
        #print("열심히 일을 한다.")
        print(f'{self.name} works hard.')

    def about_me(self):                                             # 부모 클래스 함수 재정의
        super().about_me()                                          # 부모 클래스 함수 사용
        #print("제 급여는", self.salary, "만원이고, 제 입사일은", self.hire_date, "입니다.")
        return f'제 급여는 {self.salary} 만원이고, 제 입사일은 {self.hire_date} 입니다.'


taylor = Person('Taylor', 24, 'male')

e1 = Employee('Jane', 20, 'female', 300, '20190104')
e1.do_work()
#e1.about_me()
print(e1.about_me())