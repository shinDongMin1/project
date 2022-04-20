
# ---------------------------------------------------------------------------
# 몸체가 없는 간단한 클래스를 선언하고 그 클래스를 이용하여 객체를 생성해 본다.
# ---------------------------------------------------------------------------
class Person:
    pass  # An empty block


person = Person()   # 인스턴스 person 생성
print("person=", person)
print("type(person)=", type(person))


from A_122_oop_module import Animal

ani = Animal()
print("\nani=", ani)
print("type(ani)=", type(ani))
print("ani.id=", ani.id)

exit()

prsn2 = Person()
print("prsn2=", prsn2)
print("type(prsn)=", type(prsn2))

b = 3       # 사실상의 instantiation -> int 클래스를 가진 object 생성
print("type(b)=", type(b))  # type(b)= <class 'int'>
print()

person.a = 5     # 클래스 내에 변수를 새로 할당하는 것과 같다.
print("prsn.a=", person.a)
print("type(prsn.a)=", type(person.a))

exit()
#"""


"""
# Pycharm에서 아래 루틴을 수행하려면 현재의 directory를 바꾸어야 한다.
import os
print(os.getcwd())
cur_dir = 'D:\\Work\\W_DIP_CV\\Algorithms_PPTs\\jh_basics\\a_byte_of_python'
os.chdir(cur_dir)
#os.chdir('c:')
print(os.getcwd())
"""


"""
#if Animal is None:
#    del Animal
from A_122_oop_module import Animal

object_p = Animal()
print("object_p=", object_p)
print("type(object_p)=", type(object_p))
"""

