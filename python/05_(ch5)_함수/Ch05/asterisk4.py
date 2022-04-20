def asterisk_test_2(*args):
    x, y, *z = args
    return x, y, z

print(asterisk_test_2(3, 4, 5, 10, 20))



def asterisk_test_3(*args):
    a, *z = args
    return a, z

print(asterisk_test_3(3, 4, 5, 10, 20))
