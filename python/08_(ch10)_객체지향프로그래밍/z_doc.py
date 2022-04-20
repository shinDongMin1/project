# doc string 사용법
# 다음과 같이 클래스와 메서드를 만들 때 :(콜론) 바로 다음 줄에 """ """(큰따옴표 세 개)
# 또는 ''' '''(작은따옴표 세 개)로 문자열을 입력한다.
#   https://dojang.io/mod/page/view.php?id=2378


class Person:
    #'''Doc: Person class'''
    '''
    Doc: Person class
    '''

    def greeting(self):
        #'''인사 메서드입니다.'''
        '''Doc. Greeting method'''
        print('Hello')


print(Person.__doc__)  # 사람 클래스입니다.
print(Person.greeting.__doc__)  # 인사 메서드입니다.

maria = Person()
print(maria.greeting.__doc__)  # 인사 메서드입니다.

#help(Person)
#help(Person.greeting)