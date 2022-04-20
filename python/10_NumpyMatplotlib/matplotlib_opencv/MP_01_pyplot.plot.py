"""
# pyplot.plot() 함수로 그림 그리기
# pyplot.plot( x, y, fmt, kwargs) 파라미터 제어기법을 보인다.

# https://matplotlib.org/  -> 여기서 plot을 검색하여 적당한 것을 찾는다.
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html?highlight=plot#matplotlib.pyplot.plot

"""

import matplotlib.pyplot as plt


#"""
#---------------------------------------------------------------------------------
# 실습 1
# fig. 1: (x, y) 평면에서 y 값만 지정해서 그림 그리기
# fig. 2: fmt 부분을 지정하여 선의 색상과 속성을 제어하기
#---------------------------------------------------------------------------------

# fig. 1 ------
y = [1.6, 3.7, 2.4]
# y 값이 3개의 요소이면 x축 데이터도 3개로 본다. x=[0, 1, 2]로 정해진다.

plt.plot(y)             # y 값이 3개의 요소이면 x축 데이터도 3개로 본다. x=[0, 1, 2]로 정해진다.
plt.grid('on')          # grid를 표시한다. plt.grid() eh 'on'과 같은 효과
plt.show()              # 창을 닫아야 다음 줄로 넘어간다.

# fig. 2 ------
plt.figure()        # 새로운 창을 연다
fmt = 'go-'         # 데이터가 있는 부분을 'g'(green) 색상의 'o'로 표시한다. 선의 모습은 '-'이다.
plt.plot(y, fmt)
plt.grid('off')     # grid를 제거한다.
plt.show()          # 실제 그림들은 이 명령에 의해 화면에 출력된다. Non Interactive mode(default)의 특징.
# show()순간에서 대기하고 있음. 다음으로 넘어가려면 두 개의 창을 모두 닫아야 한다.
print("Windows were closed...")
exit(0)
#"""


"""
#---------------------------------------------------------------------------------
# 단계 2
# (x, y) 평면에서 x와 y 값 모두 지정해서 그림 그리기
# fmt 대신에 keyword argument를 사용해서 그림의 속성을 제어한다.
# fig. 1: 라인의 3가지 속성을 지정하고, 그리드를 그린다.
# fig. 2: 그림에 포함된 여러 속성에 대한 다양한 제어 기법을 보인다.
#---------------------------------------------------------------------------------
import numpy as np

# fig. 1 ------
N = 5
x = range(N); print('x=', x); print('x=', list(x))

#  20~50을 N개의 간격으로 나눈다.
y = np.linspace(20, 50, N)      # (start, stop, num). start, stop까지 모두 포함
print('y=', y)

# keyword args를 지정하여 선의 특성을 지정한다.
plt.plot(x, y, linestyle='--', linewidth=0.5, color='g', marker='x')

# grid()안에 인자가 있으면 grid(True)로 간주하여 그리드 출력.
plt.grid(color='b', linestyle='--', linewidth=0.5)


# fig. 2 ------
# 윈도를 새로 열고, 그 윈도의 타이틀 바 제목을 지정한다.
plt.figure(num='Title Bar : Sine Waves')

# 삼각함수의 시간(t)와 곡선 값(y)의 관계식
# Y = A * sin(2 * pi * f * t + shift)   # A=amplitude(진폭), f=frequency, shift=phase shift(위상차)

step = 0.1
x = np.arange(-np.pi, np.pi+step, step)     # arange(start, stop, step) => [-pi, +pi]
y = np.sin(2 * x)   # 2*pi 이면 한 주기가 완성된다. -2*pi ~ + 2*pi 범위이므로 2개의 주기가 완성된다.
plt.plot(x, y, linestyle='-', linewidth=0.5, color='m', label='sin(2x)')      # m=magenta

y = 0.5 * np.sin(4*x)           # amplitude(진폭) = 0.5
plt.plot(x, y, linestyle='--', color='b', label='0.5sin(4x)')

plt.grid(True)      # =grid(). =grid('on'). True default. 그리드를 그린다.
plt.ylim(top=1, bottom=-1)              # y축의 최소, 최대값을 지정한다.
plt.xlim(left=-np.pi, right=np.pi)      # x축의 최소, 최대값을 지정한다.
plt.xlabel('x variable, time')          # x축의 레이블을 보인다.
plt.ylabel('y variable, amplitude')     # y축의 레이블을 보인다.
plt.title('sin(2x) and 0.5sin(4x)')      # 그림의 제목을 보인다.
plt.legend()
plt.show()      # 실제 그림은 이 명령에 의해 화면에 출력된다. Non Interactive mode의 특징.
exit(0)
"""


#"""
#---------------------------------------------------------------------------------------
# 실험 3: sine wave
# 1. 프로그램의 기능
#     삼각 함수 신호를 파라미터의 변화에 따라 출력한다.
# 2. 프로그램의 목표
#     삼각함수의 형성에 필요한 주요 파라미터의 특성에 대해 이해한다.
#     - 진폭, 주파수, 위상차
# 3. 프로그램에서 점검 포인트
#     함수로 표현한 삼각함수를 파라미터를 바꾸어 가면 한 화면에 모두 그리기
#---------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# sine 함수의 모델링
#   f: 주파수, frequency[hz]
#   t: 시간, time[sec]
#   phase : 위상차, pahse[rad]
#   bias : 직류성분, DC component
def sineWave(A, f, t, phase, y_bias=0) :
    y = A *  np.sin(2 * np.pi * f * t + phase) + y_bias
    return(y)

start_t = 0; stop_t = 2;
t = np.arange(start_t, stop_t, 0.01, np.float32)

# 다수의 y 함수를 구성하기 위한 파라미터의 조합을 다음 순서로 나열한다.
#   [A, f, phase, y_bias, lbl]
#   A : Amplitude
#   f : frequency
#   lbl : legend()에서 쓰일 선의 이름

y_list = [ [1, 1, 0, 0, 'y1'], [0.5, 2, 0, 0, 'y2'], [0.5, 2, 0, -1, 'y3']]
#y_list = [ [1, 1, 0, 0, 'y1'], [1, 1, np.pi*2/3, 0, 'y2: +2pi/3']]
#y_list = [ [1, 1, 0, 0, 'y1'], [1, 1, np.pi*2/3, 0, 'y2: +2pi/3'], [1, 1, np.pi*2*2/3, 0, 'y3: +2*2pi/3']]

for A, f, phase, y_bias, lbl  in y_list:
    plt.plot(t, sineWave(A, f, t, phase, y_bias), label=lbl)
    print(lbl+": A=", A, ', f=', f, ' T=', 1/f, ', phase=', phase, ',y_bias=', y_bias)

plt.xlabel('time[sec.]'); plt.ylabel('Amplitude')
#plt.axis([start_t, stop_t, -y_lim, y_lim])     # x_min, x_max, y_min, y_max
plt.grid(color='b', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Sine Wave')
plt.show()
exit(0)
#"""




#---------------------------------------------------------------------------------------
# 4. 미션(실험 1에 해당) - 아래와 같은 가정용 전원의 파형을 도시하시오.
#     가정용 전원은 60[Hz] 주파수의 220V 전압으로 제공된다.
#         Herz는 파형의 초당 진동수를 말한다. 1초에 60번의 주기를 반복한다.
#         -110~+110V의 전압이 교번되어 최대 220V의 전압차를 낼 수 있다.
#     이를 그림으로 표현하고자 한다.
#     조건 : sin파로 모델링하기로 함. f0 주파수라면 sin(2*pi*f0*t)로 모델링할 수 있음.
#             여기서 t는 초[sec]
#     단계 1: 1초에 1회의 진동수를 갖는 -110~+110의 sine 파를 도시하시오.
#     단계 2: 위 파형에 추가하여 제시된 문제의 파형을 도시하시오.
#
#     참고 : Mathematics of AC voltages, https://en.wikipedia.org/wiki/Alternating_current
#             v(t) = V_peak * sin(wt). w=2*pi*f
#---------------------------------------------------------------------------------------
