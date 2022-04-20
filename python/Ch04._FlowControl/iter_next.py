"""
목적:
    range() 함수를 사용한 "for ~ in range(N):" 구문이 어떤 방식으로 반복 수행하는지 그 동작과정을 분석한다.
    이 동작을 iter(), next() 함수를 사용하여 설명하고자 한다.

배경 설명:
    보통 for loop의 in에는 iterable objects가 쓰인다. = > "for ~ in iterable_object:"
    iterable_objects의 사례로는 list, tuple, string를 들 수 있는데 i 값에는 바로 이들 iterable_objects 원소 값이
    순차적으로 바뀌어 모든 원소를 소진할 때까지 loop문을 수행한다.
    iterable object로 range() 함수가 사용될 수 있는데 range() 함수의 반환 값은 <class 'range'>로서
    일반적으로 기대한 것처럼 이들이 list와 유사한 형태로 어떤 배열에 데이터를 모두 저장해 두고 있는 것은 아니다.

    "for k in iterable_object" 수행은 in 다음에 지정되는 obejct에 대해 iterator 생성하고 이후 loop를 반복할 때마다
        next(iterator)를 수행하여 반환하는 원소를 k에 반환하는 것으로 이루어진다. 끝이면 StopIteration exception을 발생시켜 정지한다.

결론:
    range() 함수는 지정한 회수를 loop를 수행하기 위해 사용된다.
    그러나 이 함수는 호출 당시 그 회수 만큼의 원소를 가진 iterable object를 바로 반환하지 않는다.
    이 동작을 원리적으로 설명한다면 다음과 같다.  "for k in range(N):" loop에 대해;

        1) iterator = iter(iterable_objects)    # iter(range()) 함수에 의해 iterator를 반환한다.
            iterable_objects로는 원래 list, tuple, string를 들 수 있다.
            iter() 함수는 "in ~" 에서 ~ 자리의 iterable_objects에게 자동으로 적용된다.
            아래의 next(iterator) 함수에서 이들의 실제 원소 값을 하나씩 반환할 수 있는 오브젝트(iterator)를 반환한다.
        2) element = next(iterator)     # 곧 이어 자동 호출되는 next(iterator)에 의해 loop를 수행하면서 새 원소를 k에 반환한다.
            자동으로 호출되는 next() 함수에 의해 호출될 때마다 iterable objects 안의 원소를 인덱스를 증가시켜 하나씩 반환한다.
            그런데 iterable_objects가 range(N)일 경우에는 k=0,.., N-1을 순차적으로 반환한다고 해석된다.

주의사항:
    그러나, 위 설명은 "for ~in" loop 동작을 이 동작과 관계된 함수(iter(), next())를 활용하여 해석한 것이다.
    for loop가 실제로 그렇게 함수를 호출하면서 수행될 것이라 생각되지는 않는다.
    그렇지만, 아마도, 유사한 동작을 더 효율적인 방법으로 수행할 것으로 추정하고 있다.

참고 링크:
    python iterable과 iterator의 의미
        https://bluese05.tistory.com/55

참고:
loop 문 학습에 추가로 공부해야 할 중요한 topic
    enumerate
    zip

"""




# -----------------------------------------------------------------------------------------------
# 실험 1: range() 함수에 의해 생성한 iterator 객체를 기반으로  반복 루프를 시행하는 모습을 관찰해 본다.
# -----------------------------------------------------------------------------------------------
print("\n1. iterator for 'range class': r = range(3) ...")
r = range(3)
print(f'r = range(3): type(r)={type(r)}, r = {r}')
# r = range(3): type(r)=<class 'range'>, r = range(0, 3)

ir = iter(range(3))         # iterator for 'range class'
print(f'ir = iter(range(3)): type(ir)={type(ir)}, ir = {ir}')
# ir = iter(range(3)): type(ir)=<class 'range_iterator'>, ir = <range_iterator object at 0x0000011AC82DE770>

print(f'next(ir)={next(ir)}')       # next(ir)=0
print(f'next(ir)={next(ir)}')       # next(ir)=1
print(f'next(ir)={next(ir)}')       # next(ir)=2

# print(f'next(ir)={next(ir)}')    # 더 이상 수행하면 StopIteration exception을 발생시켜 정지한다.
# 오류 메시지: Traceback (most recent call last):  ... StopIteration

#exit(0)

# -----------------------------------------------------------------------------------------------
# 실험 2: list 자료를 기반으로 생성한 iterator 객체를 기반으로 반복 루프를 시행하는 모습을 관찰해 본다.
# -----------------------------------------------------------------------------------------------
print("\n2. iterator for 'list class': l = list(range(3)) ...")
l = list(range(3))
print(f'l = list(range(3)): type(l)={type(l)}, l = {l}, len(l)={len(l)}')
# l = list(range(3)): type(l)=<class 'list'>, l = [0, 1, 2], len(l)=3

il = iter(list(range(3)))
print(f'il = iter(list(range(3))): type(il)={type(il)}, il = {il}')
# il = iter(list(range(3))): type(il)=<class 'list_iterator'>, il = <list_iterator object at 0x000002CAE7CBAC88>

print(f'next(il)={next(il)}')       # next(il)=0
print(f'next(il)={next(il)}')       # next(il)=1
print(f'next(il)={next(il)}')       # next(il)=2
#print(f'next(il)={next(il)}')      # 수행하면 StopIteration exception을 발생시켜 정지한다.

#print(next(x))

#exit(0)