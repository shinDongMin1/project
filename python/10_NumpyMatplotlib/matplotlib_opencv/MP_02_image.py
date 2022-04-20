"""
영상 파일 출력하기
미션
    1. 화면 4, 5, 6에 지정된 영상을 도시하시오.
    2. 원본 영상의 평균값을 계산하시오.
    3. threshold를 기준으로 부울 논리 연산을 통해  binary 영상을 만들어 도시하시오.
    4. 지정된 영상을 가로, 세로 1/2로 만들어 출력하시오.

맨 처음 열리는 2장의 사진은 아무 키나 입력하면 다음 루틴으로 진행한다.
다음 열리는 두 개의 창은 순차적으로 닫아야 다음 루틴으로 진행합니다.
이후 마지막 창에서는 아무 버튼을 누르면 종료합니다.

"""

import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import cv2 as cv

fileName = "lenna.tif"


# ---------------------------------------------------------------------------------------------------
# 1 단계: OLpenCV 함수로 영상을 처리한다.
# ---------------------------------------------------------------------------------------------------

# openCV에서 제공하는 함수를 통해 영상을 img_cv 어레이로 읽어들인다.
img_cv = cv.imread(fileName)    # BGR 순으로 배열..
print(f'type={type(img_cv)}, ndim={img_cv.ndim}, shape={img_cv.shape}, dtype={img_cv.dtype}')

img_cv2 = cv.imread(fileName, 0)    # mono로 읽어들인다.
print(f'type={type(img_cv2)}, ndim={img_cv2.ndim}, shape={img_cv2.shape}, dtype={img_cv2.dtype}')

# 창을 열어 영상을 출력한다.
cv.imshow('Step 1: OpenCV color', img_cv)
cv.imshow('Step 1: OpenCV mono', img_cv2)
print("아무키나 입력하세요....")
cv.waitKey()    # 키 입력을 무한정 기디린다. 아무키나 입력하면 다음 루틴으로 진행한다.
cv.destroyAllWindows()      # 창을 닫는다.



# ---------------------------------------------------------------------------------------------------
# 2단계: matplotlib 함수로 영상을 처리한다.
# ---------------------------------------------------------------------------------------------------

# matplotlib에서 제공하는 함수를 통해 영상을 img_plt 어레이로 읽어들인다.
img_plt = img.imread(fileName)
print(f'type={type(img_plt)}, ndim={img_plt.ndim}, shape={img_plt.shape}, dtype={img_plt.dtype}')

# figure(): 새로운 창을 생성. num은 창의 이름 혹은 번호(number)를 지정한다.
plt.figure(figsize=(15, 8), num='Step 2: Test')

# suptitle(): 창의 하위 제목을 지정한다.
plt.suptitle("Step 2: Simple Image Processing Examples", fontsize=14, fontweight='bold')

plt.subplot(231)            # 2x3 배열의 subplt 창에서 1번째 창 지정
plt.imshow(img_plt)
plt.title('original')       # 해당 창의 타이틀
# 1번 창에는 (x, y) 축의 픽셀 좌표가 출력됨.

plt.subplot(2, 3, 2)        # 2 x 3 배열의 subplt 창에서 2번째 창을 지정하는 다른 방법
rev = 255 - img_plt         # 영상 데이터는 0~255의 범위. 이 경우 반전(역상) 영상이 만들어진다.
plt.imshow(rev)
plt.title('reverse')
plt.xticks([]), plt.yticks([])
# 2번 창에는 (x, y) 축의 픽셀 좌표가 출력되지는 않으나 테두리는 남아 있음.

plt.subplot(233)
data = np.zeros((120, 120, 3), dtype=np.uint8)
data[0:40, :, 0] = 255      # Red
data[40:80, :, 1] = 255      # Green
data[80:, :, 2] = 255      # Blue
plt.imshow(data)            # 3채널 영상
plt.title('Color in RGB(3ch.)')
plt.axis('off')        # 영상의 경계가 보이지 않는다.
#plt.xticks([]), plt.yticks([])       # 영상의 경계가 보인다.

plt.subplot(234)
data = np.zeros((100, 100), dtype=np.uint8)
data[50:100, :] = 255

# 다음 명령어의 주석을 해제하면 어떤 결과가 나오는지 관찰 바란다.
#plt.gray()     # figure 내의 모든 서브창에 대해 gray colormap을 쓰게 만든다.

plt.imshow(data)    #plt.imshow(data, cmap='gray')
plt.title('B/W BOX in 1ch')
#plt.axis('off')        # 영상의 경계가 보이지 않아 불편
plt.xticks([]), plt.yticks([])      # 영상의 경계가 보인다.

plt.subplot(235)        # red channel의 값만 보인다. 그런데 color map은 지정하지 않았다.
#plt.imshow(img_plt[:, :, 0])        # cmap= false color, pseudo color. 미지정
#plt.imshow(img_plt[..., 0])     # 위의 표현은 이렇게 바꾸어 쓸 수도 있다.
plt.imshow(img_plt[..., 0], cmap='jet')     # 큰 값은 뜨거운 색, 작은 값은 차가운 색으로 표현한다.

plt.title('1 ch: channel 0, Red')       # RGB 배열
plt.xticks([]), plt.yticks([])      # 영상의 경계가 보인다.

plt.subplot(236)
plt.imshow(img_plt[:, :, 0], cmap='gray')       # 흑백 계조 칼라맵을 사용한다.
plt.title('1 ch: channel 0, red')
plt.xticks([]), plt.yticks([])
print("현재 열린 창을 닫아야 다음 루틴으로 진행합니다....")
plt.show()


# ---------------------------------------------------------------------------------------------------
# 단계 3: OpenCV로 읽은 영상을 matplotlib.plt로 화면에 출력한다.
# ---------------------------------------------------------------------------------------------------
fig = plt.figure(num=2)
fig.patch.set_facecolor('silver')       # 화면 바탕 색상을 정한다.

# suptitle(): 창의 하위 제목을 지정한다.
plt.suptitle("Step 3: OpenCV image handling", fontsize=14, fontweight='bold')

# OpenCV 함수로 읽은 영상 어레이를 출력한다.
plt.subplot(141)
plt.imshow(img_cv)              # 읽어들인 영상 배열은 BGR 순서인데, 출력하는 함수는 RGB라서 올바른 색상이 표현되지 않는다.
plt.title('img read by openCV')
plt.axis('off')

# OpenCV 함수로 읽은 영상 어레이를 출력하려면 BGR 배열을 RGB 배열로 바꾸어야 한다.
plt.subplot(142)
plt.imshow(img_cv[..., ::-1])     # 0~2번 채널 배열을 2~0번 채널로 재배열하여 출력한다. BGR -> RGB
plt.title('img read by openCV')
plt.axis('off')

gray = cv.cvtColor(img_cv, cv.COLOR_BGR2GRAY)   # gray로 변환한다.
plt.subplot(143)
plt.imshow(gray)
plt.title('gray with default cmap')
plt.axis('off')

plt.subplot(144)
plt.imshow(gray, cmap='gray')
plt.title("gray with cmap='gray'")
plt.axis('off')

print("현재 열린 창을 닫아야 다음 루틴으로 진행합니다....")
plt.show()

# ---------------------------------------------------------------------------------------------------
# 단계 4: 화면을 꽉 채워서 출력하기. 화면 저장하기.
# ---------------------------------------------------------------------------------------------------

fig = plt.figure(figsize=(15, 8), num='Step 4: 아무런 키나 입력하면 종료합니다.')
fig.patch.set_facecolor('blue')       # 화면 바탕 색상을 정한다.
fig.patch.set_alpha(0.3)        # Alpha, transparency: 0이면 투명, 1이면 완전 불투명.

plt.suptitle("pyplt Image, 아무런 키나 입력하면 종료합니다", fontsize=14, fontweight='bold')

plt.subplot(131)
plt.imshow(img_plt)
plt.title('original')
plt.axis('off')

plt.subplot(1, 3, 2)
rev = 255 - img_plt
plt.imshow(rev)
plt.title('reverse')
plt.axis('off')

plt.subplot(133)
plt.imshow(img_plt[:, :, 0], cmap='gray')
plt.title('channel 0')
plt.xticks([]), plt.yticks([])

# 아래 조정 작업 중에서 나중에 쓴 것이 설정을 overwrite함.
plt.tight_layout() # 가로, 세로 관점에서 빈틈을 줄여 그림의 크기를 키움
plt.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01) # 상하좌우 여백의 크기를 지정


# matplotlib에도 파일 저장함수가 있다. openCV는 imwrite(파일명, 어레이)
img.imsave('rev.jpg', rev)

# matplotlib는 영상 어레이뿐만 아니라 윈도 전체를 저장하는 기능을 지원한다.
fig = plt.gcf()
fig.savefig("result.png")
#fig.savefig("result.jpg")   # jpg는 안되는 듯. 오류 발생.

#plt.show()  # 이 함수를 사용하면 영상을 출력하고 창을 닫을 때 까지 대기한다.
# plt.show() 대신에 아래 함수를 쓰면 화면을 출력하고, 키입력 혹은 마우스 클릭을 대기한다.
print("아무런 키나 입력하면 종료합니다.")
plt.waitforbuttonpress()


# 참조 -----------------------
# plt.close()       # 현재 활성창을 닫는다.
# plt.close(fig)    # 핸들 'fig'로 창을 닫는다.
# plt.close(num)    # 숫자 'num'을 닫는다.
# plt.close(name)   # 이름이 'name'인 창을 닫는다.
# plt.close('all')    # 모든 창을 닫는다.


