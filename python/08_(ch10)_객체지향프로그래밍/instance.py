"""
# --------------------------------------------------------------------------------------------
# 실습(1): 원본. 클래스의 선언과 기초적인 활용
# __init__ : 인스턴스를 만들 때 실행되는 함수
# __str__ : 인스턴스 자체를 출력 할 때의 형식을 지정해주는 함수
# --------------------------------------------------------------------------------------------


class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경한다: From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

    def __str__(self):  # 인스턴스 자체를 출력 할 때의 형식을 지정해주는 함수
        return "Hello, My name is %s. I play in %s in center." % (self.name, self.position)

# SoccerPlayer를 클래스를 이용하여 instance(객체)를 생성한다.
jinhyun = SoccerPlayer("Jinhyun", "MF", 10)

print("현재 선수의 등번호는:", jinhyun.back_number)
jinhyun.change_back_number(5)   # 객체의 메소드 호출.
print("현재 선수의 등번호는:", jinhyun.back_number)
print(jinhyun)

exit(0)
"""

# --------------------------------------------------------------------------------------------
# 실습(2): 아래와 같이 수정하였다.
# 1) __init__ 함수의 입력 파라미터에 default keyword를 지정하였다.
# 2) return self.back_number     반환 값이 있는 함수로 변경하였다.
# --------------------------------------------------------------------------------------------


class SoccerPlayer(object):
    def __init__(self, name='You', position='out', back_number=30):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경한다: From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

    def change_back_number2(self, new_number):
        print("선수의 등번호를 변경한다: From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number
        return self.back_number             # 2) 반환 값이 있는 함수로 변경하였다.


# SoccerPlayer를 클래스를 이용하여 instance(객체)를 생성한다.
you = SoccerPlayer(back_number=8)   # 1) 입력 파라미터 일부 미제공
print(you.name, you.position, you.back_number)

jinhyun = SoccerPlayer("Jinhyun", "MF")
print("현재 선수의 등번호는:", jinhyun.back_number)

print(jinhyun.change_back_number(11))   # None. 반환 값이 없는 메서드를 출력하였다.
print(jinhyun.change_back_number2(12))  # 12. 반환 값이 있다.
print("현재 선수의 등번호는:", jinhyun.back_number)


