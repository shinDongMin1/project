"""

내장함수 sorted 함수 연습
       https://docs.python.org/ko/3/library/functions.html?highlight=sorted#sorted
 sorted(iterable, *, key=None, reverse=False)
   iterable 의 항목들로 새 정렬된 리스트를 돌려줍니다.
   키워드 인자로만 지정해야 하는 두 개의 선택적 인자가 있습니다.
       key 는 하나의 인자를 받는 함수를 지정하는데, iterable의 각 요소들로부터 비교 키를 추출하는 데 사용됩니다
           (예를 들어, key = str.lower). 기본값은 None 입니다 (요소를 직접 비교합니다).
       reverse 는 논리값입니다. True 로 설정되면, 각 비교가 뒤집힌 것처럼 리스트 요소들이 정렬됩니다.

"""


a = [3, 8, 2, 7, 3, 1]
a.sort()    # list에만 적용되는 sort 메소드. 반환값 없음.
print(a)    # [1, 2, 3, 3, 7, 8]

b = sorted([5, 2, 3, 1, 4])     # 파이썬 내장함수 sort
print(b)    # [1, 2, 3, 4, 5]

# 사전형 자료에 대해서는 키를 정렬한다.
c = sorted({9: 'D', 2: 'B', 7: 'B', 5: 'E', 4: 'A'})
print(type(c), c)   # <class 'list'> [2, 4, 5, 7, 9]

#print(str.lower('Hello, I am Jin'))
# hello, i am jin

# list.sort()와 sorted()는 모두 비교하기 전에
# 각 리스트 요소에 대해 호출할 함수를 지정하는 key 매개 변수를 가지고 있다.
# key 매개 변수의 값은 단일 인자를 취하고
# 정렬 목적으로 사용할 키를 반환하는 함수여야 한다.
# sorted(자료, key=Something) 함수는 호출되면
# 자료의 각 원소를 key에서 지정한 기준에 따라 소팅한다.
print(sorted("Hello, I am Jin".split(), key=str.lower))
# ['am', 'Hello,', 'I', 'Jin']  소문자 관점에서 정렬

# lambda 함수는 lambda arguments: expression 형식으로
# arguments를 받아 expression을 수행한다.
# 아래 사례에서는 sorted(자료, key=Something)에서 Something이 lamda 함수이다.
#   arguments로서 tuple 1세트를 전달받고,
#   expression에서는 그 튜플의 [2]번 원소를 반환한다.
# 이로서 소팅의 기준 key=튜플의 [2]번 원소가 되어 이를 소팅의 기준으로 삼게 된다.
student_tuples = [('john', 'A', 15), ('Jane', 'B', 12), ('dave', 'B', 10)]
a = sorted(student_tuples, key=lambda student: student[2])   # sort by age
print(a)  # [('dave', 'B', 10), ('Jane', 'B', 12), ('john', 'A', 15)]

a = sorted(student_tuples, key=lambda abc: abc[0])   # sort by name
print(a)  # [('Jane', 'B', 12), ('dave', 'B', 10), ('john', 'A', 15)]

