"""

private variable
    클래스 외부에서는 참조할 수 없는 변수. 클래스 내부에서만 활용되는 변수.
    __로 시작되는 변수명을 사용한다.
private method
    클래스 내부에서만 호출하는 함수. __로 시작되는 함수명을 사용한다.

public variable - 클래스 외부에서도 접근가능한 변수
public method - 클래스 외부에서도 호출 가능한 메서드

Method의 종류

1) instance method
    - 객체를 기반으로 호출하는 메서드. self를 함수의 파라미터로 전달받는다.

2) class method
    객체를 생성하지 않고 클래스를 기반으로 호출 가능한 메서드. 클래스 변수 액세스 가능.
    cls를 함수의 파라미터로 전달받는다.

3) static method
    객체를 생성하지 않고 클래스를 기반으로 호출 가능한 메서드. 클래스 변수 액세스 못함.

4) special method
    __init__, __doc__, __repr__, __del__

"""
class Rectangle:
    count = 3  # 클래스 변수

    def __init__(self, width, height):      # class initializer
        self.width = width
        self.height = height

        # private 변수 __area. 클래스 밖에서 접근 불가능
        self.__area = width * height

    # private method. instance method
    def __internalRun(self):
        pass

    def area(self):     # instance method
        area = self.width * self.height
        return area

    @classmethod            # class method-객체를 생성하지 않고 호출 가능한 메서드
    def get_count(cls):
        return cls.count

    @classmethod
    def put_count(cls, number):
        cls.count = number
        return number

    @staticmethod
    def is_square(rectWidth, rectHeight):
        return rectWidth == rectHeight


a = Rectangle(4, 5)       # 객체 생성

a.width = 2     # 인스턴스 변수를 수정함
print("a.width=", a.width)
print("a.height=", a.height)
print("a.area()=", a.area())        # 인스턴스 메소드 호출


print("a.count=", a.count)  # 이 값을 수정하지 않을 때만 클래스 변수가 정상으로 읽힘.
a.count = 30    # 클래스 변수를 수정하는 것이 아님. 그냥 변수를 하나 만드는 것과 같음.
a.abc = 1       # 객체에 인스턴스 변수를 하나 만드는 것과 같다.
print("a.abc=", a.abc)
print("a.count=", a.count)


print("Rectangle.get_count()=", Rectangle.get_count())      # 클래스 메소드 호출
Rectangle.count = 7     # class 변수를 수정
print("Rectangle.get_count()=", Rectangle.get_count())      # 클래스 메소드 호출
print("Rectangle.count =", Rectangle.count)     # 클래스 변수 읽기
print("a.count=", a.count)

print("Rectangle.put_count(34)=", Rectangle.put_count(34))  # 클래스 메소드 호출
print("Rectangle.count =", Rectangle.count)     # 클래스 변수 읽기


if Rectangle.is_square(5, 5):    # static method 호출
    print("Rect is square.")    # True


# 아래는 private 변수라서 접근이 불가능.
#print(Rectangle.__area)
#print(a.__area)