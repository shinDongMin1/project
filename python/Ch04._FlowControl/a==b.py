

"""
a = 100
b = 100
print(a == b)       # True
print(a is b)       # True

a = 300
b = 300
print(a == b)       # True
print(a is b)       # True. 교과서에는 이것이 False를 출력한다고 되어 있음. [-5, 256] 범위를 넘어섰기 때문에...


a = 30000000000000000000000000
b = 30000000000000000000000000
print(a == b)       # True
print(a is b)       # True

a = 3.12
b = 3.12
print(a is b)       # True
print(a == b)       # True
"""

"""
# Optimization in Python — the Interning Technique for Improved Performance
# https://levelup.gitconnected.com/optimization-in-python-the-interning-technique-for-improved-performance-3ff14d376176
rslt = all([i is j for i, j in list(zip(range(-5, 257, 1),  range(-5, 257, 1)))])
print(rslt)

rslt = any([i is j for i, j in list(zip(range(257, 1000, 1),  range(257, 1000, 1)))])
print(rslt)

rslt = any([i is j for i, j in list(zip(range(-5, 1000, 1),  range(-5, 1000, 1)))])
print(rslt)

rslt = any([i is j for i, j in list(zip(range(257, 258, 1),  range(257, 258, 1)))])
print(rslt)

a = 257
b = 257
print(a is b)       # True

rslt = any([i is j for i, j in list(zip(range(256, 258, 1),  range(256, 258, 1)))])
print(rslt)
"""

a, b, c, d = 10, int(10), int('10'), int('1010', 2)
print(a, b, c, d)
print(id(a), id(b), id(c), id(d))

aa = 'Python Programming'
bb = 'Python Programming'
print(aa is bb)
print(id(aa), id(bb))



print("Execution Time Comparison: with and without Interning")
def compare_with_eqality(n_times):
    str1 = "Python programming is easy and fun." * 200000
    str2 = "Python programming is easy and fun." * 200000
    for i in range(n_times):
        if str1 == str2:
            pass

def compare_with_identity(n_times):
    import sys
    str1 = sys.intern("Python programming is easy and fun." * 200000)
    str2 = sys.intern("Python programming is easy and fun." * 200000)
    for i in range(n_times):
        if str1 is str2:
            pass

from timeit import default_timer as timer

start = timer()
compare_with_eqality(10000)
end = timer()
print(f'Without interning, Time: {end - start}[sec.]')      # Time: 4.9851752[sec.]

start = timer()
compare_with_identity(10000)
end = timer()
print(f'With interning, Time: {end - start}[sec.]')      # Time: 0.011376900000000134[sec.]
