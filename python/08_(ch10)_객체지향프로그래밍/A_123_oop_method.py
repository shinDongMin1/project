"""
    클래스와 그 클래스의 메서드를 선언하는 방법
"""


class Person:
    def say_hi(self):   # instance method는 self가 첫 번째 인자이다.
        print('Hello, how are you?')

    def say_this(self, msg):    # instance method는 self가 첫 번째 인자이다.
        print(msg)


p = Person()    # instance를 생성한다.
p.say_hi()      # instance의 메서드를 호출한다.
Person().say_hi()   # 클래스의 함수를 호출한다.
p.say_this('Good day to you!')  # msg 파라미터 패싱

