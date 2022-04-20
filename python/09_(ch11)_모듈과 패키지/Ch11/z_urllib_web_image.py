"""
urllib는 URL 작업을 위한 여러 모듈을 모은 패키지입니다.: 링크: https://docs.python.org/ko/3/library/urllib.html
    1) URL을 열고 읽기 위한 urllib.request
    2) urllib.request에 의해 발생하는 예외를 포함하는 urllib.error
    3) URL 구문 분석을 위한 urllib.parse
    4) robots.txt 파일을 구문 분석하기 위한 urllib.robotparser


urllib.request --- Extensible library for opening URLs. 링크: https://docs.python.org/ko/3/library/urllib.request.html#module-urllib.request
    The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world
        --- basic and digest authentication, redirections, cookies and more.


Python urllib tutorial for Accessing the Internet
    https://pythonprogramming.net/urllib-tutorial-python-3/

"""


#"""
# ---------------------------------------------------------------------------
# 실험 1: Web 영상 파일 저장
# ---------------------------------------------------------------------------
import urllib.request       # package.module

# 1) URL를 지정하여 영상 다운로드 받아 파일로 저장 및 화면 출력
print('\n1. Saving image file as is -------')
url_img1 = 'https://www.udiscovermusic.com/wp-content/uploads/2019/05/BTS-Official-Press-Shot.jpg'
url_img2 = 'https://imgix.bustle.com/uploads/image/2019/1/4/05245351-b63e-48de-9d23-7638a29211c0-shutterstock_8135462o.jpg?w=1020&h=574&fit=crop&crop=faces&auto=format%2Ccompress&cs=srgb&q=70'
url_img3 = 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/autumn-in-the-white-mountains-of-new-hampshire-royalty-free-image-841380450-1531931081.jpg?crop=1.00xw:0.755xh;0,0.202xh&resize=1200:*'

img1 = urllib.request.urlopen(url_img1).read()
print('type(img1)=', type(img1))    # <class 'bytes'>
f1 = open('_image1.png', mode='wb')      # 파일 확장자로의 형식으로 저장되지는 않는 것으로 보인다.
print(type(f1))      # <class '_io.BufferedWriter'>
f1.write(img1)
f1.close()

# 2) URL를 지정하여 영상을 받아  파일로 저장하지 않고 화면에 출력
print('\n2. Showing image file as in url -------')
from skimage import io as skio      # io 모듈과 충돌하여 이름을 바꾸었다.
import matplotlib.pyplot as plt
from PIL import Image
import io       # 파이썬 내장 모듈


# with statement에 대한 설명
#   https://www.geeksforgeeks.org/with-statement-in-python/
#   파일 스트림 처리에 close 처리가 필요없는 장점이 있다.
# io.BytesIO에 대한 설명
#   https://docs.python.org/3/library/io.html

print('1) io.BytesIO: file make, PIL: file open, matplotlib: show')
with urllib.request.urlopen(url_img1) as url:
    f1 = io.BytesIO(url.read()) # io.BytesIO: byte 자료를 in memory 형태의 파일로 만든다.
img1 = Image.open(f1)       # 영상처리 전용 모듈 PIL의 함수
print("type(img1)=", type(img1))
plt.imshow(img1)
plt.axis('off')
#plt.show()     # 현재 상태에서 show()를 하면 창을 닫아야 다음 루틴으로 전개된다.

print('2) skimage: URL file open & save, matplotlib: show')
# skimage의 imread는 영상 파일 뿐만 아니라 URL 영상 파일도 읽는다.
img2 = skio.imread(url_img2)
print("type(img2)=", type(img2))
plt.figure()
plt.imshow(img2)
plt.axis('off')
skio.imsave('_image2.png', img2)    # 지정하는 형식으로 저장

print('3) skimage: URL file open, matplotlib: show & save')
plt.figure()
img3 = skio.imread(url_img3)
skio.imshow(img3); skio.show()
plt.imsave('_image3.bmp', img3)     # matplotlib로 저장.
#plt.show()  # waits until windows are close.
exit(0)


