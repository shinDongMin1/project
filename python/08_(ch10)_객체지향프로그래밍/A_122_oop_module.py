"""
    함수와는 달리 클래스는 선언만으로도 내부 루틴이 수행된다.
    ==> 메서드로 정의하려면 def 문으로 함수화 선언을 하면 자동 수행되지는 않는다.
"""


def animal():
    print("animal function")

class Water:
    pass
    #print("Water class")   # 모듈로 load되거나 메인루틴으로 수행할 때 모두 수행됨.

    def f1(self):
        print("function f1 in Water")

class Animal():
    id = "'member variable of Animal'"


if __name__ != "__main__":  # main 프로그램의 자격이면 수행한다.
    import os
    _ = os.getcwd()      # get Current Working Directory
    print("\n'A_122_oop_module.py' is being loaded as a module from:\n" + _)
else:  # import 되는 순간 수행된다..
    Animal()

    #print("testing...")              # 메인 프로그램의 자격으로 수행될 때 호출된다.
    #Water()
    #print("t...")
    #a = 3
    #animal()


