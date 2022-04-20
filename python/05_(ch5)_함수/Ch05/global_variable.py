def f():
    global s        # 함수 내에서 global 변수를 선언하는 방법
    s = "I love London!"
    print(s)


s = "I love Paris!"
f()
# I love London!

print(s)
# I love London!
