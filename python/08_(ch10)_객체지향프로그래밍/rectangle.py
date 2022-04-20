

# ------------------------------------------------------
# 실습 1: 사각형 클래스를 정의하고, 면적을 계산하는 메소드
# ------------------------------------------------------

class Rectangle:
    count = 0   # class variable. public variable

    # special method. class initializer
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    # instance method
    def calcArea(self):
        area = self.width * self.height
        return area


rec = Rectangle(4, 5)
print(rec.calcArea(), rec.count)

rec2 = Rectangle(2, 4)
print(rec2.calcArea(), rec2.count)
exit()


