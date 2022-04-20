def triangle_area(base, height):
    return base * height / 2

def rectangle_area(width, height):
    return width * height

# 본 파일을 모듈로 활용하는 메인 프로그램은 main2.py입니다. 
# 모듈자격으로 수행하면 모듈 이름이 출력된다.
# calcpkg.geometry2     <= __name__ = 'calcpkg.geometry2'
print(__name__)

# 메인 루틴의 자격으로 수행하면 다음 메시지가 출력된다.
# __main__          <= __name__ = '__main__'
# This is being executed as main status.
if __name__ == '__main__':
    print('This is being executed as main status.')


