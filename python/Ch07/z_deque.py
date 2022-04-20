"""

collection module로 구현한 deque(Double Ended Queue, 데크) 지료형 및 해당 메소드 연습

dequeue(Double Ended Queue, 데크)란?
    양방향에서 데이터를 넣거나(append, leftappend) 빼는 것(pop, popleft)이 가능한 queue
        .append(item): 우측에 추가 하기
        .appendleft(item): 좌측에 추가하기
        .pop(): 우측에서 빼서 반환하기. 오른쪽의 끝값 가져오면서 deque에서 제거
        .popleft(): 좌측에서 빼서 반환하기. 왼쪽의 끝값 가져오면서 deque에서 제거
        그외 다수의 메소드를 지원한다.
    deque는 stack & queue는 물론 여타의 자료형을 대부분 지원한다.


"""
from collections import deque



#"""
# ----------------------------------------------------------------------------------
# 실습 1: stack 처럼 동작하기: Last In First Out
# push 방법: deque.append(item),  stack <---- item
# pop 방법:  item=deque.pop(),    stack -----> item
# ----------------------------------------------------------------------------------


st = deque()
print('type(st)=', type(st), '| st:', st)      # type(st)= <class 'collections.deque'> | st: deque([])

# 1) push 동작
for i in range(5):
    st.append(i)
    print('st:', st)

# 2) pop 동작
print('popped item=', st.pop(), '| st:', st)    # popped item= 4 | st: deque([0, 1, 2, 3])
print('popped item=', st.pop(), '| st:', st)    # popped item= 3 | st: deque([0, 1, 2])
print('popped item=', st.pop(), '| st:', st)    # popped item= 2 | st: deque([0, 1])
print('popped item=', st.pop(), '| st:', st)    # popped item= 1 | st: deque([0])
print('popped item=', st.pop(), '| st:', st)    # popped item= 0 | st: deque([])
#print('popped item=', st.pop(), '| st:', st)    # 오류 발생 종료. IndexError: pop from an empty deque

exit(0)

#"""


"""
# ----------------------------------------------------------------------------------
# 실습 2: queue 처럼 동작하기: First In First Out
# push 방법: list.appendleft(item),  ------> queue
# pop 방법:  item=list.pop(),                queue ------> item
# ----------------------------------------------------------------------------------


que = deque()
print('type(que)=', type(que), '\nque:', que)
# type(que)= <class 'collections.deque'>
# que: deque([])

# 1) push 동작
for i in range(5):
    que.appendleft(i)
    print('que:', que)

# 2) pop 동작
print('popped item=', que.pop(), '| que:', que)     # popped item= 0 | que: deque([4, 3, 2, 1])
print('popped item=', que.pop(), '| que:', que)     # popped item= 1 | que: deque([4, 3, 2])
print('popped item=', que.pop(), '| que:', que)     # popped item= 2 | que: deque([4, 3])
print('popped item=', que.pop(), '| que:', que)     # popped item= 3 | que: deque([4])
print('popped item=', que.pop(), '| que:', que)     # popped item= 4 | que: deque([])
#print('popped item=', que.pop(), '| que:', que)
# 수행오류. IndexError: pop from an empty deque

exit(0)
"""

# ----------------------------------------------------------------------------------
# 실습 3: deque의 여러 메소드 연습
# ----------------------------------------------------------------------------------

d = deque([1, 2, 'q'])
d.append('A')                   # 원소 1개만 오른 쪽에 추가.
d.append((8, 9))
d.appendleft('0')               # 원소 1개만 왼 쪽에 추가
print('1)', d)
# 1) deque(['0', 1, 2, 'q', 'A', (8, 9)])


# extend/extendleft: 여러 개의 원소를 추가한다.
# 넣을 원소들을 tuple, list의 형태로 하나의 자료형으로 만들어야 한다.
d.extend(('b', 13))     # deque의 오른 쪽에서 2개의 자료가 밀려 들어 감.
d.remove('q')
print('2)', d)
# 2) 2) deque(['0', 1, 2, 'A', (8, 9), 'b', 13])


d.extendleft([1, 2])    # 앞의 1부터 deque의 왼쪽으로 들어 감
print('3)', d)
# 3) deque([2, 1, '0', 1, 2, 'A', (8, 9), 'b', 13])

print('4)', d.pop(), d)
# 4) 13 deque([2, 1, '0', 1, 2, 'A', (8, 9), 'b'])

print('5)', d.popleft(), d)
# 5) 2 deque([1, '0', 1, 2, 'A', (8, 9), 'b'])


print('\n-----------------------')

d = deque(range(5))
print('1)', d)
# 1) deque([0, 1, 2, 3, 4])

d.rotate(2)         # 오른쪽으로 회전
print('2)', d)
# 2) deque([3, 4, 0, 1, 2])

d.rotate(-1)        # 왼쪽으로 회전
print('3)', d)
# 3) deque([4, 0, 1, 2, 3])

print('\n-----------------------')

d = deque(i for i in range(8))
print('1)', d, '| len(d)=', len(d))
# 1) deque([0, 1, 2, 3, 4, 5, 6, 7]) | len(d)= 8
d = deque(maxlen=5)                         # 최대 길이 제한이 있는 deque를 선언
print('2)', d, '| len(d)=', len(d))
# 2) deque([], maxlen=5) | len(d)= 0
d.extend([1, 2, 3, 4, 5, 6])      # 최대 길이가 5이므로 앞의(왼쪽) 것 하나를 버린다.
print('3)', d, '| len(d)=', len(d))
# 3) deque([2, 3, 4, 5, 6], maxlen=5) | len(d)= 5
d.append('A')                   # 오른 쪽에서 추가하므로 왼쪽에 있는 원소가 소멸된다.
print('4)', d, '| len(d)=', len(d))
# 4) deque([3, 4, 5, 6, 'A'], maxlen=5) | len(d)= 5
d.appendleft('0')               # 왼쪽에서 추가하므로 오른 쪽의 원소가 소멸된다.
print('5)', d, '| len(d)=', len(d))
# 5) deque(['0', 3, 4, 5, 6], maxlen=5) | len(d)= 5
d.extend([i for i in range(8)])     # 8개를 선언하였기 때문에 3개는 앞에 선언된 순으로 없어진다.
print('6)', d, '| len(d)=', len(d))
# 6) deque([3, 4, 5, 6, 7], maxlen=5) | len(d)= 5
d.reverse()
print('7)', d, '| len(d)=', len(d))
# 7) deque([7, 6, 5, 4, 3], maxlen=5) | len(d)= 5





# {} 자료를 추가하면 어떻게 되는지 분석이 아직 안되었음.
#d.extend({3, 2, 1})     # 작은 값부터 deque의 오른 쪽으로 들어감.
#d.extendleft({5, 6, 7})
#d.extendleft({-5, -6, -7})
#d.extendleft({-1, -2, -3})     # 집합 원소들의 순서에 대해서는 잘 분석이 안됨.






