# ----------------------------------------------------------------------------------
# list 자료형으로 구현한 stack.
# stack(Last In First Out)의 구현: 나중 들어간 것이 먼저 나온다.
# push 방법: list.append(item),  stack <---- item
# pop 방법:  item=list.pop(),    stack -----> item
# ----------------------------------------------------------------------------------


#"""
# --------------------------------------------------------------------
# 실습 0: 교재 원본
# --------------------------------------------------------------------
word = input("Input a word: ")
world_list = list(word)
print(world_list)

result = []
for _ in range(len(world_list)):
    result.append(world_list.pop())

print(result)
print(word[::-1])
exit(0)
#"""

# --------------------------------------------------------------------
# 실습 1: 스택 명시
# --------------------------------------------------------------------
word = input("Input a word: ")
stack = list(word)
print('stack:', stack)

result = []
for _ in range(len(stack)):
    value = stack.pop()     # popping
    print('popped value=', value, 'stack:', stack)
    result.append(value)

print('popped result:', result)
print(word[::-1])


