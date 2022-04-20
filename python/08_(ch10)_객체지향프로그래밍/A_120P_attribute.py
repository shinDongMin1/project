"""
attribute가 무엇을 의미하는지 알아보는 예제 프로그램

    attribute에는 메소드와 클래스에서 선언한 변수가 모두 포함된다.
    클래스 속성은 곧 인스턴스 속성이 된다.

hasattr(object, name)
    object가 주어진 name의 속성(attribute)을 갖고 있는지의 여부를 반환한다.
    만약 object에 name의 속성이 존재하면 True, 아니면 False를 반환한다.

클래스 속성과 인스턴스 속성의 차이
    클래스 속성 - class 안에서 할당하는 public(공개) 변수들((__init__) 밖에서 )
    인스턴스 속성 - `self'에 할당하는 변수들, 클래스 내의 메소드들
"""


class Animal:
    num_ani = 0      # 클래스 변수. public(공개), 클래스 속성은 곧 인스턴스 속성이 된다.
    __num_ani = 0    # 클래스 변수. private(비공개), 클래스 속성(x), 인스턴스 속성(x)

    # 이하 `self'에 소속된 변수들은 모두 해당 인스턴스의  속성이다.
    def __init__(self, name1, legs, wing):
        self.legs = legs
        self.name = name1
        self.wings = wing
        Animal.num_ani += 1

    # 메소드들은 클래스 속성이면서 인스턴스 속성이다.
    # self 소속변수는 instance 속성
    def run(self):
        pass

    def add(self, att):    # new_att는 인스탄스의 속성이다. 그러나 att는 속성이 아니다.
        self.new_att = att      # 클래스 속성(x), 인스턴스 속성(x). public variable(O).
        new_att2 = 'swim'       # 클래스 속성(x), 인스턴스 속성(x). public variable(x).


object_p= Animal('Cat', 4, 0)   # name, legs, wings

# hasattr(object, name)
#   The arguments are an object and a string.
#   The result is True if the string is the name of one of the object’s attributes,
#   name이 object의 attribute가 아니라면 False를 반환한다.

print('Instance Attribute --------------------')
for att_item in ['name', 'legs', 'wings', 'run', 'add', 'num_ani', '__num_ani', 'new_att', 'att', 'new_att2']:
    if hasattr(object_p, att_item):
        print(f"object_p has {att_item} instance attribute.")
    else:
        print(f"object_p has NO {att_item} instance attribute.")

print('\nClass Attribute --------------------')

for att_item in ['name', 'legs', 'wings', 'run', 'add', 'num_ani', '__num_ani', 'new_att', 'att', 'new_att2']:
    if hasattr(Animal, att_item):
        print(f"Animal has {att_item} class attribute.")
    else:
        print(f"Animal has NO {att_item} class attribute.")

print(Animal.num_ani)
object_p2 = Animal('Parrot', 2, 2)   # name, legs, wings
object_p2.add('fly')
print(Animal.num_ani)
print(object_p2.new_att)
object_p2.new_att = 'crawl'
print(object_p2.new_att)


print(getattr(object_p, 'run'))
print(getattr(object_p, 'num_ani'))
