"""

"""


"""
#---------------------------------------------------------------------------------------
# 실험 1: gaussian function
# 가우시안 함수의 데이터를 반환하는 함수를 정의하고
# 이를 이용하여 다양한 시그마에 대한 함수 곡선을 색상을 바꾸어가며 그린다.
# 미션 : 'mission : legend를 붙이시오..' 창에 legend를 첨가하도록 수정하시오.
#---------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

N=30; step=0.1
r = np.arange(-N, N+step, step, np.float32)       # (start, stop, step)

def gaussian(r, sigma):
    return(np.exp(-r**2/(2*sigma**2)))

g = gaussian(r, sigma=9); plt.plot(r,g, label = 'sigma=8')
g = gaussian(r, sigma=3); plt.plot(r,g, label = 'sigma=2')
plt.legend()


# 미션: 아래 창의 그림에 legend를 출력되도록 프로그램을 수정하시오.
plt.figure(num='mission : legend를 붙이시오..')
for sigma, color in [(1, 1), (3, 2), (5, 3), (7, 4), (9, 5)]:
    plt.plot(r, gaussian(r, sigma), color)

plt.ylim(top=1, bottom=0)       # 왜 y값의 범위가 늘어나는지 모르겠음.?
plt.show()
exit(0)
"""


#---------------------------------------------------------------------------------------
# 실험 2: 2차원 gaussian function를 3차원으로 도시한다.
# matplotlib 설치와 함께 설치되는 Toolkit
#   https://matplotlib.org/api/toolkits/index.html?highlight=toolkit
# 이중 mpl_toolkits.mplot3d 메소드를 이용하여 3차원으로 도시한다.
#   https://matplotlib.org/api/toolkits/mplot3d.html#toolkit-mplot3d-api    --- API 모음
#---------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1 단계 ---------------------------------------------------------------------------
# 시그마와 적절한 디멘전의 크기를 정한다. 아래 값을 바꾸어 가면서 실험하세요.
sigma =3; N=7; step=1
#sigma =6; N=20; step=1

# 2 단계 ---------------------------------------------------------------------------
# x축, y축이 가질 수 있는 값을 나열한 어레이를 구하고 확인차 그 값을 출력한다.
X = np.arange(-N, N+step, step)
Y = np.arange(-N, N+step, step)
XX, YY = np.meshgrid(X, Y)

# 3 단계 ---------------------------------------------------------------------------
# 가우시안 함수를 정의하고 이를 이용하여 x, y 값을 대입하여 좌표 값에 따른 가우시안 함수 값(ZZ)를 구한다.


def gaussian2D(x,y, sigma):
    return(np.exp(-(x**2 + y**2)/(2*sigma**2)))


ZZ = gaussian2D(XX,YY, sigma)
print('ZZ.shape=', ZZ.shape)

if N <= 7:             # 크기가 적을 때만 값을 출력한다.
    # 원하는 정밀도로 출력하게 한다. >>> help(np.set_printoptions)
    np.set_printoptions(precision=2, floatmode='fixed');  # 소수점 이하 2째 자리까지 출력.
    print('XX.shape=',XX.shape); print(XX)
    print('YY.shape=',YY.shape); print(YY)
    # 소수점 이하 2째 자리까지 출력하되, 지수 형식을 쓰지 않는다.
    np.set_printoptions(precision=1, floatmode='fixed', suppress=True);
    print(ZZ)


# 4 단계 ---------------------------------------------------------------------------
# x, y값에 따른 ZZ의 값을 3차원으로 표시한다.

fig = plt.figure(num='2D Gaussain')
ax = Axes3D(fig)
ax.set_title("Gaussian: sigma=" + str(sigma))

# color map : https://matplotlib.org/gallery/color/colormap_reference.html
Perceptually_Uniform_Sequential =  ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
Miscellaneous = ['flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
            'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']
c_map = 'jet'
c_map = 'inferno'
c_map = 'magma'

ax.plot_surface(XX, YY, ZZ, rstride=1, cstride=1, cmap=c_map)
plt.show()
exit(0)


# 미션: 사진 정보를 높낮이 정보로 표현할 수 있을까?

