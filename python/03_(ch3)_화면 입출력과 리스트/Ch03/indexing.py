
"""
#----------------------------------------------------------------------------------------------------
# 실습 0: 교과서의 예제
#----------------------------------------------------------------------------------------------------
colors = ['red', 'blue', 'green']
print(colors[0])
print(colors[2])
print(len(colors))
"""

#----------------------------------------------------------------------------------------------------
# 실습 1: 스트링 자료외 정수, 부동소수, 다른 리스트를 원소로 갖는 리스트 지료형 연습
#----------------------------------------------------------------------------------------------------

colors = ['red', 'blue', 'green', 100, 3.14, [1, 'A', 2.0]]

# 리스트 자료형을 모두 출력
print('1) colors =', colors, '| type(colors)=', type(colors))
# 1) colors = ['red', 'blue', 'green', 100, 3.14, [1, 'A', 2.0]] | type(colors)= <class 'list'>

# 인덱싱 동작의 사례: []안에 인텍스 번호를 지정하여 특정 원소를 액세스(read) 한다.
print('2) colors[0] =', colors[0], '| type(colors[0])=', type(colors[0]))
# 2) colors[0] = red | type(colors[0])= <class 'str'>


# 인덱싱 동작의 사례: []안에 인텍스 번호를 지정하여 특정 원소를 액세스(read/write) 한다.
print('3a) colors[2] =', colors[2], '| type(colors[2])=', type(colors[2]))
# 3a) colors[2] = green | type(colors[2])= <class 'str'>
colors[2] = [1, 'Hello']        # 인텍스 번호([2]번)를 지정하여 액세스(write) 한다.
print('3b) colors[2] =', colors[2], '| type(colors[2])=', type(colors[2]))
# 3b) colors[2] = [1, 'Hello'] | type(colors[2])= <class 'list'>


# 인덱스가 -1이면 맨 마지막 원소를 지정한다.
print('4) colors[-1] =', colors[-1], '| type(colors[-1])=', type(colors[-1]))
# 4) colors[-1] = [1, 'A', 2.0] | type(colors[-1])= <class 'list'>

print('5) colors[-1][1] =', colors[-1][1], '| type(colors[-1][1])=', type(colors[-1][1]))
# 5) colors[-1][1] = A | type(colors[-1][1])= <class 'str'>
# 주의!!!: numpy에서 와는 달리 리스트 자료형에서는 a[1][2]를 a[1,2]로 쓸 수 없다.

print('6) len(colors)=', len(colors))
# 6) len(colors)= 6

print('7) len(colors[-1])=', len(colors[-1]))
# 7) len(colors[-1])= 3
