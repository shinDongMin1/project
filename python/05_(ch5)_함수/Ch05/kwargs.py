def kwargs_test(**kwargs):
    print(type(kwargs), kwargs)       # 사전사료형이다.
    # <class 'dict'> {'first': 3, 'second': 4, 'third': 5}

    print("First value is {first}".format(**kwargs))
    print("Second value is {second}".format(**kwargs))
    print("Third value is {third}".format(**kwargs))

kwargs_test(first = 3, second = 4, third = 5)
# key=value 들로 구성된 사전자료로 함수가 호출된다.
