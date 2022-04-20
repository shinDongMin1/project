"""
time — Time access and conversions
    https://docs.python.org/3.8/library/time.html

    The epoch is the point where the time starts, and is platform dependent.
    For Unix, the epoch is January 1, 1970, 00:00:00 (UTC).
    To find out what the epoch is on a given platform, look at time.gmtime(0).

    UTC is Coordinated Universal Time (formerly known as Greenwich Mean Time, or GMT).
    DST is Daylight Saving Time, an adjustment of the timezone by (usually) one hour during part of the year.

"""

#"""
# -------------------------------------------------------------------------------------
# 실습 1: 현재의 시간 알아내기.
# 에포크(epoch): 시간의 기준점, 1970년 1월 1일 0시 0분 0초
# gmtime(), localtime()은 struct_time 타입의 객체를 반환한다.
# ascime()은 이를 스트링으로 변환한다.
# -------------------------------------------------------------------------------------
import time
a = time.gmtime(0)    # epoch,  midnight on January 1, 1970 UTC
print('\nEpoch time:', time.asctime(a)); print(a)
print('type(time.gmtime())=>', type(a))

b = time.gmtime()     # ()안에 시점 미지정. 현재의 UTC
print('\nCurrent UTC time:', time.asctime(b)); print(b)

c = time.localtime()  # 현재의 지역시간
print('\nCurrent local time:', time.asctime(c)); print(c)

exit(0)
#"""

# -------------------------------------------------------------------------------------
# 실습 2: 경과 시간 알아내기, 지정시간 대기하기
# 1) time.time(): UTC 시간을 기준으로 현재까지의 경과 시간[초, 부동소수] 반환
# 2) time.sleep(): 지정한 시간(초, 부동소수)만큼 대기
# -------------------------------------------------------------------------------------
import time
start = time.time()     # time(1st) 모듈의 time(2nd) 함수(class).
time.sleep(1)           # time 모듈의 sleep() 함수. 1[초] 동안 대기
end = time.time()       # 경과시간 계산
print('elapsed time=', end-start)        # 지연시간[초] 출력

# sleep() 함수에 대해서는 모듈이름(time)을 지정할 필요가 없다.
from time import sleep
start = time.time()
sleep(0.5)

# 모듈 time의 모든 함수에 대해 모듈 이름을 지정할 필요가 없다.
from time import *
end = time()
print('elapsed time=', end-start)        # 지연시간[초] 출력


