def f():
    s = "I love London!"    # assignment가 수행되었으므로 s는 지역 변수이다.
    #s[0] = 'y'     # 오류 발생. immutable data sequence라서 시도조차 할 수가 없다.
                    # 만약 mutable data sequence라면, 전역변수를 유지할 수 있다.
    print(s)


s = "I love Paris!"
f()
# I love London!

print(s)
# I love Paris!