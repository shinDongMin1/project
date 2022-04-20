# ----------------------------------------------------------------------------------
# list 자료로 구현한 queue.
# queue(First In First Out)의 구현: 먼저 들어간 것이 먼저 나온다.
# push 방법: list.append(item),             queue <----- item
# pop 방법:  item=list.pop(0), item <------ queue
# ----------------------------------------------------------------------------------


# 실습 1: 간단히 넣기와 빼기.
# 우측으로 넣고(append) 좌측에서 뽑아(pop(0)) 나간다.

queue =[]
print('1. queue:', queue)

queue.append('A')
print('2. queue:', queue)

queue.append('B')
print('3. queue:', queue)

queue.append('C')
print('4. queue:', queue)

print('5. popped value=', queue.pop(0), 'queue:', queue)
print('6. popped value=', queue.pop(0), 'queue:', queue)
print('7. popped value=', queue.pop(0), 'queue:', queue)


# 실습 2: 거의 유사한 동작

a = [1, 2, 3, 4, 5]
print(a.pop(0), a)      # 1 [2, 3, 4, 5]
print(a.pop(0), a)      # 2 [3, 4, 5]
print(a.pop(0), a)      # 3 [4, 5]
print(a.pop(0), a)      # 4 [5]
print(a.pop(0), a)      # 5 []
#print(a.pop(0), a)      # 오류 발생!! IndexError: pop from empty list
a.append(10)
a.append(20)
a.append(30)
print(a.pop(0), a)      # 10 [20, 30]
print(a.pop(0), a)      # 20 [30]
print(a.pop(0), a)      # 30 []





