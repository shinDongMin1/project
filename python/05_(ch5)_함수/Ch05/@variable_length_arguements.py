"""
# --------------------------------------------------------------------------------------------------------
# 실험 1 - *로 전달된 파라미터
# asterisk로 표시된 파라미터(여기서는 tail) 이후로는 수를 제한하지 않고 전달할 수 있는 데
# 실제로는 튜플로 묶여 처리된다.
# --------------------------------------------------------------------------------------------------------

def print_tail(first,*tail):
    print(tail)

print_tail(1, 2, 3, 4)
# (2, 3, 4)

print_tail('A', 1, '3 4', 'B')
# (1, '3 4', 'B')

exit(0)
"""


# --------------------------------------------------------------------------------------------------------
# 실험 2: **로 전달된 파라미터
# If we declare a formal parameter prefixed with two asterisks, then it will be bound to
# a dictionary containing any keyword arguments in the actual parameters which do not
# correspond to any formal parameters.
# --------------------------------------------------------------------------------------------------------


def make_dictionary(max_length=10, **entries):
    print(f'\ntype(entries)={type(entries)}, max_length={max_length}, len(entries)={len(entries)}')
    return entries


a = make_dictionary(max_length=2, key1=5, key2=7, key3=9, key4=3, key5=9)
print('type(a)=', type(a), '| a=', a)
# type(entries)=<class 'dict'>, max_length=2, len(entries)=5
# type(a)= <class 'dict'> | a= {'key1': 5, 'key2': 7, 'key3': 9, 'key4': 3, 'key5': 9}

a = make_dictionary(1, key1=5, key2=7, key3=9)
print('type(a)=', type(a), '| a=', a)
# type(entries)=<class 'dict'>, max_length=1, len(entries)=3
# type(a)= <class 'dict'> | a= {'key1': 5, 'key2': 7, 'key3': 9}

a = make_dictionary(3, key1=5, key2=7, key3=9)
print('type(a)=', type(a), '| a=', a)
# type(entries)=<class 'dict'>, max_length=3, len(entries)=3
# type(a)= <class 'dict'> | a= {'key1': 5, 'key2': 7, 'key3': 9}

exit(0)



# --------------------------------------------------------------------------------------------------------
# 실험 3: **로 전달된 파라미터
# 정해진 수량의 파라미터(키:값) 쌍만 받아들이는 예제
# --------------------------------------------------------------------------------------------------------


def make_dictionary(max_length=10, **entries):
    return dict([(key, entries[key]) for i, key in enumerate(entries.keys()) if
    i < max_length])

a = make_dictionary(max_length=2, key1=5, key2=7, key3=9)
print('type(a)=', type(a), '| a=', a)
# type(a)= <class 'dict'> | a= {'key1': 5, 'key2': 7}

a = make_dictionary(1, key1=5, key2=7, key3=9)
print('type(a)=', type(a), '| a=', a)
# type(a)= <class 'dict'> | a= {'key1': 5}

a = make_dictionary(3, key1=5, key2=7, key3=9)
print('type(a)=', type(a), '| a=', a)
# type(a)= <class 'dict'> | a= {'key1': 5, 'key2': 7, 'key3': 9}