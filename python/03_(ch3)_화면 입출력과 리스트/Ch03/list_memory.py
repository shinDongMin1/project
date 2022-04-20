# == 와 is의 차이를 통해본 파이썬 변수(객체)의 메모리 관리 특징
# 1. == compares the values of the objects.
#       ==는 변수가 같은 Value(값)을 가지면 True
# 2. is compares the references of the objects.
#       is 는 == 와 달리 값을 비교하는게 아니라 실제 데이터를 가리키는 포인터가 같은지를 비교한다.
#
# id() 함수로 is 비교 결과를 예측하는 방법
# id(객체)의 반환 값은 그 객체의 유일한 정수 값을 반환한다.
# 객체의 id가 같으면 객체들이 같은 데이터 영역을 가리키고 있는 것으로 판단할 수 있다.

# 사례 1은 일부 자료에서는 다른 객체가 나오는 것으로 기술한 것들을 간혹 발견할 수 있었다.
# 파이썬이 버전이 바뀌면서 정책이 바뀐 것으로 추정된다.
a = 300000
b = 300000
print('\n1) a=', a, ', b=', b)

# 같은 값에 대해서는 일단 같은 주소를 가리킨다.
print('id(a)=', id(a), ', id(b)=', id(b))
print('a is b:', a is b, '  a == b:', a == b)
print('id(a)==id(b):', id(a) == id(b) )
# 1) a= 300000 , b= 300000
# id(a)= 2560332235600 , id(b)= 2560332235600
# a is b: True   a == b: True
# id(a)==id(b): True

a = 100
print('\n2) a=', a, ', b=', b)
print('id(a)=', id(a), ', id(b)=', id(b))
print('a is b:', a is b, '  a == b:', a == b)
print('id(a)==id(b):', id(a) == id(b) )
# 2) a= 100 , b= 300000
# id(a)= 140712281800048 , id(b)= 2560332235600
# a is b: False   a == b: False
# id(a)==id(b): False

a = [1, 2, 3]
b = a           # 데이터는 복사하지 않고 b의 데이터 포인터는 a와 같은 곳을 가리킨다.
print('\n3) a=', a, ', b=', b)
print('id(a)=', id(a), ', id(b)=', id(b))
print('a is b:', a is b, '  a == b:', a == b)
print('id(a)==id(b):', id(a) == id(b) )
# 3) a= [1, 2, 3] , b= [1, 2, 3]
# id(a)= 1427988959752 , id(b)= 1427988959752
# a is b: True   a == b: True
# id(a)==id(b): True


a[0] = 9        # a만 바꾸었는데 b도 바뀐다.
print('\n4) a=', a, ', b=', b)
print('id(a)=', id(a), ', id(b)=', id(b))
print('a is b:', a is b, '  a == b:', a == b)
print('id(a)==id(b):', id(a) == id(b) )
# 4) a= [9, 2, 3] , b= [9, 2, 3]
# id(a)= 1427988959752 , id(b)= 1427988959752
# a is b: True   a == b: True
# id(a)==id(b): True


a = [1, 2, 3]
#b = a[:]        # 데이터를 복사하여 자체의 데이터 영역을 갖는다. 따라서 포인터가 다른 곳을 가리킨다.
b = a.copy()
print('\n5) a=', a, ', b=', b)
print('id(a)=', id(a), ', id(b)=', id(b))
print('a is b:', a is b, '  a == b:', a == b)
print('id(a)==id(b):', id(a) == id(b) )
# 5) a= [1, 2, 3] , b= [1, 2, 3]
# id(a)= 1427988960264 , id(b)= 1427990431048
# a is b: False   a == b: True
# id(a)==id(b): False



a = -10
b = -10
print('\n6) a=', a, ', b=', b)
print('id(a)=', id(a), ', id(b)=', id(b))
print('a is b:', a is b, '  a == b:', a == b)
print('id(a)==id(b):', id(a) == id(b) )
# 6) a= -1 , b= 20
# id(a)= 140712281796816 , id(b)= 140712281797488
# a is b: False   a == b: False
# id(a)==id(b): False
