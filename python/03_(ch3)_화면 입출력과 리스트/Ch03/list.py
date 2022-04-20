

"""
#----------------------------------------------------------------------------------------------------
# 실습 0: 리스트 자료 정의/ 리스트 자료형 확인/ 리스트 원소 갯수 확인
#----------------------------------------------------------------------------------------------------
color1 = ['red', 'green', 'blue']
print('color1=', color1, '| type(color1)=', type(color1), '| len(color1)=', len(color1))
# color1= ['red', 'green', 'blue'] | type(color1)= <class 'list'> | len(color1)= 3

color2 = ['orange', 'black', 'white']
print('color2=', color2, '| type(color2)=', type(color2), '| len(color2)=', len(color2))
# color2= ['orange', 'black', 'white'] | type(color2)= <class 'list'> | len(color2)= 3

color_sum = color1 + color2
print('color_sum=', color_sum, '| type(color_sum)=', type(color_sum), '| len(color_sum)=', len(color_sum))
# color_sum= ['red', 'green', 'blue', 'orange', 'black', 'white'] | type(color_sum)= <class 'list'> | len(color_sum)= 6

print('color1*2=', color1*2, '| type(color1*2)=', type(color1*2), '| len(color1*2)=', len(color1*2))
# color1*2= ['red', 'green', 'blue', 'red', 'green', 'blue'] | type(color1*2)= <class 'list'> | len(color1*2)= 6

print("'blue' in color1=", 'blue' in color1)
# 'blue' in color1= True

print("'blue' in color2=", 'blue' in color2)
# 'blue' in color2= False

exit(0)
"""

"""
#----------------------------------------------------------------------------------------------------
# 실습 1: 리스트제공되는 method. 객체에 적용되는 함수를 메소드라 한다. '객체.메소드()' 방식으로 사용된다.
# append() : 리스트의 맨 뒤에 원소를 추가. 1개만 붙일 수 있다.
# extend() : 리스트의 맨 뒤에 다른 리스트를 추가. 추가되는 리스트는 여러 개의 원소로 이루어져도 무방하다
#       리스트+리스트 : 리스트의 맨 뒤에 다른 리스트를 추가. 추가되는 리스트는 여러 개의 원소로 이루어져도 무방하다
# insert(인덱스, 값) : 리스트의 중간에 원소를 삽입. 리스트의 주어진 인덱스 번지에 주어진 값의 원소를 추가.
#           삽입 지점 이후 원소들은 뒤로 밀려난다.         
# remove() : 리스트에서 주어진 원소 값을 삭제. 이후 원소들은 앞으로 당겨진다.
#            2개 이상이면 첫 번째 것만 지운다. 없으면 오류 유발.
# pop() : 리스트 맨 뒤의 값이 삭제된다. 
# reverse() : 리스트 내의 원소 배열의 순서를 뒤집는다.
# sort() : 리스트 내의 원소들을 값의 크기순으로 나열한다. 원본 자체를 sorting한다. 메소드의 반환 값이 없다.
# del(): 특정 원소를 지정하여 삭제.
#----------------------------------------------------------------------------------------------------

color = ['red', 'green', 'blue']
color.append('white')       # 기존의 리스트에 1개의 원소를 추가.
print('1) color=', color, '| len(color)=', len(color), type(color))
# 1) color= ['red', 'green', 'blue', 'white'] | len(color)= 4 <class 'list'>

color = ['red', 'green', 'blue']
color.extend(['white', 'black'])    # 기존의 리스트에 다른 리스트(2개의 원소로 이루어진)를 추가
print('2) color=', color, '| len(color)=', len(color), type(color))
# 2) color= ['red', 'green', 'blue', 'white', 'black'] | len(color)= 5 <class 'list'>

color = ['red', 'green', 'blue']
color.append(['white', 'black'])    # 기존의 리스트에 1개의 원소(2개의 원소로 이루어진 리스트)를 추가
print('3) color=', color, '| len(color)=', len(color), type(color))
# 3) color= ['red', 'green', 'blue', ['white', 'black']] | len(color)= 4 <class 'list'>

color = ['red', 'green', 'blue']
color += ['white', 'black']         # 기존의 리스트에 다른 리스트(2개의 원소로 이루어진)를 추가
print('4) color=', color, '| len(color)=', len(color), type(color))
# 4) color= ['red', 'green', 'blue', 'white', 'black'] | len(color)= 5 <class 'list'>

color = ['red', 'green', 'blue']
color.insert(1, 'white')            # index 1번에 'white' 삽입
print('5) color=', color, '| len(color)=', len(color), type(color))
# 5) color= ['red', 'white', 'green', 'blue'] | len(color)= 4 <class 'list'>

color = ['red', 'green', 'blue', 'green']
color.remove('green')            # 'green'을 찾아 삭제. 2개 이상이면 첫 번째 것만 지운다. 없으면 오류 유발.
print('6) color=', color, '| len(color)=', len(color), type(color))
# 6) color= ['red', 'blue', 'green'] | len(color)= 3 <class 'list'>

color = ['red', 'green', 'blue']
color[-1] = 'white'     # 맨 끝의 원소 값을 'white'로 바꾼다.
print('7) color=', color, '| len(color)=', len(color), type(color))
# 7) color= ['red', 'green', 'white'] | len(color)= 3 <class 'list'>

color = ['red', 'green', 'blue']
del color[1:]       # 번위를 지정하여 원소를 지운다
print('8) color=', color, '| len(color)=', len(color), type(color))
# 8) color= ['red'] | len(color)= 1 <class 'list'>

color = ['red', 'green', 'blue']
color.pop()         # 맨 마지막 원소를 지운다
print('9) color=', color, '| len(color)=', len(color), type(color))
# 9) color= ['red', 'green'] | len(color)= 2 <class 'list'>

color = ['red', 'green', 'blue']
color.reverse()         # 리스트의 나열 순서를 뒤집는다.
print('10) color=', color, '| len(color)=', len(color), type(color))
# 10) color= ['blue', 'green', 'red'] | len(color)= 3 <class 'list'>

a = [3, 5, 1, 10, 0, 6, 3]
b = a.sort() # 객체 자체의 데이터를 바꾼다. 원소값의 순서대로 나열한다.
print('11a) b=', b, type(b))    # 메소드의 반환 값이 없으니 오해하지 말자.
# b= None <class 'NoneType'>

print('11b) a=', a, '| len(a)=', len(a), type(a))
# a= [0, 1, 3, 3, 5, 6, 10] | len(a)= 7 <class 'list'>

exit(0)
"""


"""
#----------------------------------------------------------------------------------------------------
# 실습 2: packing & unpacking
#----------------------------------------------------------------------------------------------------
t = [1, 2, 3]
print('1) t=', t, '| len(t)=', len(t), type(t))
# 1) t= [1, 2, 3] | len(t)= 3 <class 'list'>

a, b, c = t
print('a=', a, '| type(a)=', type(a))
print('b=', b, '| type(b)=', type(b))
print('c=', c, '| type(c)=', type(c))
# a= 1 | type(a)= <class 'int'>
# b= 2 | type(b)= <class 'int'>
# c= 3 | type(c)= <class 'int'>

t = [1, [2,5], 3]
print('\n2) t=', t, '| len(t)=', len(t), type(t))
# 2) t= [1, [2, 5], 3] | len(t)= 3 <class 'list'>

a, b, c = t
print('a=', a, '| type(a)=', type(a))
print('b=', b, '| type(b)=', type(b))
print('c=', c, '| type(c)=', type(c))
# a= 1 | type(a)= <class 'int'>
# b= [2, 5] | type(b)= <class 'list'>
# c= 3 | type(c)= <class 'int'>

exit(0)
"""

"""
#----------------------------------------------------------------------------------------------------
# 실습 3: 2차원 리스트 - 그다지 필요성이 있다고 생각되지는 않음.
# 주의!!! : 리스트 자료형을 2차원의 개념으로 확장할 수 있지만 행렬 연산 등에 활용하지 못하는 한계가 있다.
# 다차원 데이터는 Numpy 모듈을 사용하는 것이 합리적이다.
# 여기서는 간단한 2차원 배열을 만들고, 그 원소를 액세스할 수 있는 정도의 수준만 익히도록 한다.
#----------------------------------------------------------------------------------------------------
# 2x3 리스트 생성
a = [1, 2, 3]
print('a=', a, '| type(a)=', type(a), len(a))
# a= [1, 2, 3] | type(a)= <class 'list'> 3

b = [4, 5, 6]
print('b=', b, '| type(b)=', type(b), len(b))
# b= [4, 5, 6] | type(b)= <class 'list'> 3

c = [a, b]      # c는 각각 1x3로 이루어진 row vector가 2개의 행으로 이루어진 것으로 볼 수 있다.
print('c=', c, '| type(c)=', type(c), len(c))
# c= [[1, 2, 3], [4, 5, 6]] | type(c)= <class 'list'> 2


print(c[0][0:2])        # [1, 2]
print(c[0][:])          # [1, 2, 3]
print(c[:][0])          # [1, 2, 3] 기대와는 다름??. 2차원 리스트 자료형에 슬라이싱 연산이 올바르게 수행되지 않는다.

# 아래와 같이 표현해야 올바른 슬라이싱이되는 것을 확인할 수 있었다.
print([x[0] for x in c])
print([x[1] for x in c])
print([x[2] for x in c])

# https://stackoverflow.com/questions/17277100/python-slicing-a-multi-dimensional-array
# Suppose I had a=[[1,2,3],[4,5,6],[7,8,9]] then a[0][:]=[1, 2, 3]
# but strangely enough a[:][0] is still [1,2,3].
# I would say that this should be [1,4,7]
# => 답변
# That's not that strange actually.
# Those two expressions are basically "Take the first element of a and return a copy of it"
# and "Copy a and return the first element of the copy".
# The fix is [x[0] for x in a], or, if you're working with numpy, a[:, 0]

exit(0)

print(c[0][0])
print(c[0][1])
print(c[0][2])
print(c[0])
# 1
# 2
# 3
# [1, 2, 3]

print(c[1][0])
print(c[1][1])
print(c[1][2])
print(c[1])
# 4
# 5
# 6
# [4, 5, 6]

exit(0)
"""


#----------------------------------------------------------------------------------------------------
# 미션 : 다음과 같이 그 원소 값이 정의된 2차원, 3x4 리스트 a를 정의하시오.
# 9 0 -1 -2  
# 1 2 3 4 
# 5 6 7 8 
# a가 정의되고 다음 루틴을 수행하면 주석문(#)에 적시된 값이 출력되어야 함.
#----------------------------------------------------------------------------------------------------

x = [9, 0, -1, -2]
y = [1, 2, 3, 4]
z = [5, 6, 7, 8]

a = [[9, 0, -1, -2], [1, 2, 3, 4], [5, 6, 7, 8]]

print(a[0][-1])     # = -2
print([b[0] for b in a])
print(a[0][0])      # = 9
print(a[1][0])      # = 1
print(a[1][1])      # = 2
print(a[2][1])      # = 6
print(a[2][-1])     # = 8



