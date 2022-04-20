"""
파이썬의 function arguments는 call by reference 방식으로 전달된다.
즉, 값을 담고 있는 객체를 함수에게 전달하는 것이 아니라, 그 객체의 주소만을 전달한다.
이 때문에 그 객체가 list와 같이 mutable type이면 함수안에서 그 객체를 변경함으로써
function arguments의 값을 바꿀 수도 있다.
mutable type 객체가 함수안에서 변경 가능하다고 해서 assignment 문에 의해 값을 변경할 수 있는 것은 아니다.
정수나 스트링 같은 immutable type의 객체는 함수 안에서 값을 수정할 수 없다.
"""

#"""
# -----------------------------------------------------------------------------------------------------------
# 실습 1 - mutable 타입으로 전달된 파라미터 객체를 함수에서 변경하는 사례
# 주의: 아래 함수는 반환 값이 없다.
# -----------------------------------------------------------------------------------------------------------


def spam(eggs):
    eggs.append(1)      # 기존 객체의 주소값에 [1] 추가
    eggs = [2, 3]       # 이 동작은 eggs 값을 변경하는 것이 아니라, 새로운 객체 생성하는 것이다. 이제는 local 변수가 되어 버렸다.
    # mutable type 객체가 함수안에서 변경 가능하다고 해서 assignment 문에 의해 값을 변경할 수 있는 것은 아니다.

ham = [0]       # 1개 원소의 리스트 선언
spam(ham)       # 함수 호출
print(ham)      # [0, 1]

#print(eggs)   # NameError: name 'eggs' is not defined
# eggs는 함수 안에서만 쓰이는 local 변수이다.
exit(0)

#"""


# -----------------------------------------------------------------------------------------------------------
# 실습 2 - mutable 타입으로 전달된 파라미터 객체를 함수에서 변경하는 다른 사례
# -----------------------------------------------------------------------------------------------------------

def appendItem(ilist, item):
    ilist.append(item) # Modifies ilist in a way visible to the caller

def replaceItems(ilist, newcontentlist):
    del ilist[:]                    # Modification visible to the caller
    ilist.extend(newcontentlist)    # Modification visible to the caller
    ilist = [5, 6]                  # No outside effect; lets the local ilist point to a new list object,
                                    # losing the reference to the list object passed as an argument
def clearSet(iset):
    iset.clear()

def tryToTouchAnInteger(iint):
    iint += 1                       # No outside effect; lets the local iint to point to a new int object,
                                    # losing the reference to the int object passed as an argument
    print("iint inside:", iint)     # 4 if iint was 3 on function entry

list1 = [1, 2]
appendItem(list1, 3)
print(list1)
# [1, 2, 3]

replaceItems(list1, [3, 4])
print(list1)
# [3, 4]

# 집합을 정의하는 함수 set()
# Build an unordered collection of unique elements.
# 집합 자료형은 mutable type이다.
# 메인에서 함수로 전달한 집합 객체를 함수에서 clear하였는데 이것이 메인에게까지 파급 효과를 갖고 있다.
set1 = set([1, 2])
print('type(set1)=', type(set1), ' | set1=', set1)
# type(set1)= <class 'set'>  | set1= {1, 2}

clearSet(set1 )
print(set1)                     # set([])
# set()

# 정수는 immutable이다. 함수에서 고쳤지만 그 값이 메인에게까지 효력을 미치지 못하고 있다.
int1 = 3
tryToTouchAnInteger(int1)
# iint inside: 4

print(int1)                     # 3
# 3

