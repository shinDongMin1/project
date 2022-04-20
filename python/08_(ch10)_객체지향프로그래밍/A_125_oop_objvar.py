"""
검토용 미션

현재 코딩은 같은 이름(name)의 객체를 생성해도 로봇의 수를 1 증가시킨다.
또한, 다른 이름을 가진 객체의 반환 값이 같아도 로봇의 수를 1 증가시킨다.

droid1 = Robot("R2-D2")
droid1 = Robot("R2-D2")
=> 이렇게 하면 로봇이 2대가 되는 문제가 있다. 이것을 해결해 보자.

droid1 = Robot("R2-D2")
droid2 = Robot("R2-D2")
=> 이렇게 해서 로봇이 2대가 되는 것은 괜찮다.
    R2-D2가 2대로 출력되게 하면 된다.




이를 다음 방식으로 개선하는 코드를 작성해 보자.
=========>

기능 1)
    클래스 변수를 전체 로봇의 생성 수량을 파악하는 population 외에
    생성하는 로봇의 모델을 클래스 변수에 기록하게 한다.
    객체를 생성할 때마다 같은 모델의 수량을 클래스 변수에 기록한다.
    메인 루틴에서 여러 종류의 로봇을 생성할 때마다 기종과 해당 기종의 수량 및 총 수량을 화면에 출력하게 한다.

기능 2)
    로봇을 폐기시킬 때 해당 기종의 모델의 수를 클래스 변수에서 삭제할 수 있는 방안을 수립한다.
    (힌트: special method __del__)
    메인 루틴에서 여러 종류의 로봇을 생성, 폐기하면서 기종과 수량이 올바르게 관리되는지 점검한다.

"""

class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0      # 클래스 변수

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print(f"(Initializing {self.name})")

        # When this person is created, the robot
        # adds to the population

        Robot.population += 1       # Robot()의 인스턴스를 생성할 때마다 인구를 증가시킨다.

    def die(self):
        """I am dying."""
        print(f"{self.name} is being destroyed!")

        Robot.population -= 1

        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")


    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print(f"Greetings, my masters call me {self.name}.")

    @classmethod        # 객체를 생성하지 않고, 클래스의 변수를 접근한다.
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))

#droid1 = Robot('R2-D2')
droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
