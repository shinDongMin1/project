"""
목적:
    for ~ in 구문에 in의 iterable object를 range(N) 함수를 쓰는 것과
        순차적인 N개의 원소로 이루어진 list 자료를 사용하는 것 중 어떤 것이 연산 속도 관점에서 유리한지 실험을 통해 검증한다.

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

참조 링크:
    python iterable과 iterator의 의미
        https://bluese05.tistory.com/55

참고:
loop 문 학습에 추가로 공부해야 할 중요한 topic
    enumerate
    zip

"""


# -----------------------------------------------------------------------------------------------
# 실험: loop speed comparison for list & range objects
# 같은 회수의 반복 loop를 시행함에 있어
# range()를 시용하는 것과 list 자료를 이용하는 것 중 어떤 것이 빠른지 살펴 보기로 한다.
# 결과: range_iterator 기반의 loop가 빠르다.
# -----------------------------------------------------------------------------------------------
print("\n3. loop speed comparison for list & range objects ... ")
import time

num = 100000000     # 1억. 총 40여초 이상의 소요 시간 발생... 최종적으로 실험하기를 권유
num = 1000000       # 1백만. 흐름을 살피기 위해 간단한 실험용으로 적절...
num = 10000         # 1만.  흐름을 살피기 위해 간단한 실험용으로 적절...
#num = 1000          # 1천.  정밀 시간 계측이 가능한지 의문스럽지만 시도해 봄. -> 오류: t1=0이라서 계측 불가.
#num = 100           # 정밀 시간 계측이 가능한지 의문스럽지만 시도해 봄. -> 오류: t1=0이라서 계측 불가.

# 1) range_iterator based loop
s = 0
start = time.time()         # PWR가 ON되고 경과된 현재의 시간을 초단위로 반환한다.
for i in range(num):
    s += (i % 10)           # %는 나머지(modulus) 연산자. 10으로 나누고 나머지를 반환한다.
end = time.time()
t1 = end-start
print(f'1) loop count={num}, range_iterator based loop: {t1}[sec], sum={s}')

# 2) list_iterator based loop
s = 0
start = time.time()
for i in list(range(num)):
    s += (i % 10)
end = time.time()
t2 = end-start
print(f'2) loop count={num}, list_iterator based loop: {t2}[sec], sum={s}')

s = 0
lst = list(range(num))      # list 자료로 만드는 시간을 제외해 본다.
start = time.time()
for i in lst:
    s += (i % 10)
end = time.time()
t3 = end-start
print(f'3) loop count={num}, list_iterator based loop: {t3}[sec], sum={s}')

s = 0
start = time.time()
lst = list(range(num))      # list 자료로 만드는 시간을 포함시킨다.
for i in lst:
    s += (i % 10)
end = time.time()
t4 = end-start
print(f'4) loop count={num}, list_iterator based loop: {t4}[sec], sum={s}')

print(f'Percentage: t2/t1={t2*100/t1:#.5f}, t3/t1={t3*100/t1:#.5f}, t4/t1={t4*100/t1:#.5f}')

# num = 1억일 때의 실험결과:
# 3. loop speed comparison for list & range objects ...
# 1) loop count=100000000, range_iterator based loop: 8.90019941329956[sec], sum=450000000
# 2) loop count=100000000, list_iterator based loop: 11.598949432373047[sec], sum=450000000
# 3) loop count=100000000, list_iterator based loop: 13.863930463790894[sec], sum=450000000
# 4) loop count=100000000, list_iterator based loop: 16.184712648391724[sec], sum=450000000
# Percentage: t2/t1=130.32235, t3/t1=155.77101, t4/t1=181.84663
# ====> 분석
# t1 방법이 가장 시간 소모가 적었다.
#   range() 함수가 in ~ 자리 있었기 때문에 가장 효율적인 next() 동작이 이루어졌을 것이라고 추정된다.
# t2 방법은 list 함수 안에 reange()를 넣은 것을 for loop의 in ~ 자리에 두었기 때문에
#   next() 동작이 그나마 효율적으로 작용했을 것으로 보인다.
# t3 방법은 list 자료를 만드는 시간을 제외했음에도 155%의 시간이 소요되었다.
#   list 자료에 대한 next() 동작이 자체가 시간이 많이 걸린다는 징표로 볼 수 있다.
# t4 방법은 list 자료를 사용하면서 + list 자료를 만드는 시간까지 더했더니 가장 오래 걸렸다.
#   증가된 약 30% 소요시간(181-155)은 list 자료를 만드는데 소요되었음을 알 수 있다.
# ===> 다음 요소의 값을 가져오는 next() 동작은 큰 용량의 자료에 매우 불리한다.


# num = 1백만일 때의 실험결과:
# 3. loop speed comparison for list & range objects ...
# 1) loop count=1000000, range_iterator based loop: 0.0867915153503418[sec], sum=4500000
# 2) loop count=1000000, list_iterator based loop: 0.10172796249389648[sec], sum=4500000
# 3) loop count=1000000, list_iterator based loop: 0.07976269721984863[sec], sum=4500000
# 4) loop count=1000000, list_iterator based loop: 0.12769412994384766[sec], sum=4500000
# Percentage: t2/t1=117.20957, t3/t1=91.90149, t4/t1=147.12743
# ===>
# t3 방법에 대한 집중 고찰:
#   다음 요소의 값을 가져오는 next() 동작은 작은 용량의 자료에 대해서는 그래도 크게 불리하지는 않다.
#   그러나 list를 만드는데 약 56%의 소요시간(147-91)이 필요하기 때문에 전체적으로 보면 불리하다.
#    아마도 자료 만드는 시간은 list의 용량이 적어지면 크게 줄어들 것으로 예상된다.


# num = 1만일 때의 실험결과:
# 3. loop speed comparison for list & range objects ...
# 1) loop count=10000, range_iterator based loop: 0.0009875297546386719[sec], sum=45000
# 2) loop count=10000, list_iterator based loop: 0.0009961128234863281[sec], sum=45000
# 3) loop count=10000, list_iterator based loop: 0.0010254383087158203[sec], sum=45000
# 4) loop count=10000, list_iterator based loop: 0.0009937286376953125[sec], sum=45000
# Percentage: t2/t1=100.86915, t3/t1=103.83873, t4/t1=100.62772
# ===> 현재 출력결과는 모두 t1보다는 많이 소요되었지만, 100%보다 적게 소요될 때도 있었음.
# 반복 실험해 볼 때마다 아래와 같이 다른 결과가 나옴. 아마도 시간계측 자체가 부정확할 가능성도 있어 보인다.
# Percentage: t2/t1=103.38272, t3/t1=0.00000, t4/t1=105.80247
# Percentage: t2/t1=102.46411, t3/t1=100.09569, t4/t1=100.21531
# Percentage: t2/t1=50.03588, t3/t1=0.00000, t4/t1=50.04784
# Percentage: t2/t1=100.07172, t3/t1=102.36672, t4/t1=97.56156

