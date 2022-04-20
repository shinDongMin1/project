"""
    This routine plays two roles.
     1) module that can be imported in the other program to support add/sub functions
     2) standalone program that can be executed independently
"""


def add(x, y): return x + y
def sub(x, y): return x - y


def main():
    x = 1; y = 2
    print(f"function based add/sub, x={x}, y={y}: x+y={add(x, y)}, x-y={sub(x, y)}")


if __name__ == "__main__": # main 프로그램의 자격인지 확인한다. 맞으면 True를 반납한다.
    main()              # 메인 프로그램의 자격으로 수행될 때 호출된다.
else:                   # import 되는 순간 수행된다..
    import os
    _dir = os.getcwd()      # get Current Working Directory
    print("'_md.py' is being loaded as a module from the following directory:\n" + _dir)
