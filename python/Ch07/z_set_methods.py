"""
set 데이터 구조
A set is an unordered collection with no duplicate elements.
Basic uses include membership testing and eliminating duplicate entries.
Set objects also support mathematical operations
    like union, intersection, difference, and symmetric difference.

set methods
    https://www.w3schools.com/python/python_ref_set.asp

"""

# 실습 1: set 로직 연산
a = {5, 2, 8}
print('1, intersection:', a.intersection({1, 3, 5}), a & {1, 3, 5})    # {5}
print('2, union:', a.union({1, 3, 5}), a | {1, 3, 5})                  # {1, 2, 3, 5, 8}
print('3, difference:', a.difference({1, 3, 5}), a - {1, 3, 5})        # {8, 2}

# 실습 2: set methods
b = a.add('9')    # 1개의 원소만 추가. 주의.!! 반환값 없음.
print('4, add:', a, b)      # {8, 2, '9', 5} None
b = a.update('B', 'A')      # 1개 이상의 원소를 추가. 주의.!! 반환값 없음.
print('5, update:', a, b)      # {2, 5, '8', 8, 'A', '9'} None
b = a.remove('9')           # 1개만 삭제 가능. 주의.!! 반환값 없음.
print('6, remove:', a, b)   # {2, 5, 8, 'A', 'B'} None
b = a.discard('B')     # 역시 1개만 삭제 가능. 주의.!! 반환값 없음.
print('7, discard:', a, b)   # {2, 5, 8, 'A'} None
b = a.clear()       # 모든 원소 삭제. 주의.!! 반환값 없음.
print('8, clear:', a, b)   # set{} None

exit()










# 실습 3: 스트링에 대한 set 로직 연산
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
# {'orange', 'banana', 'pear', 'apple'}

print('orange' in basket)                 # fast membership testing
#True

print('crabgrass' in basket)
#False

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

print(a)                                  # unique letters in a
# {'b', 'd', 'c', 'r', 'a'}

print(a - b)                              # letters in a but not in b
# {'r', 'b', 'd'}

print(a | b)                              # letters in a or b or both
# {'b', 'd', 'z', 'c', 'm', 'r', 'l', 'a'}

print(a & b)                              # letters in both a and b
# {'a', 'c'}

print(a ^ b)                              # letters in a or b but not both
# {'m', 'r', 'l', 'b', 'd', 'z'}

#a = {1, [1, 2]}     # TypeError: unhashable type: 'list'
