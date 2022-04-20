"""
프로그램이 하는일
    Red CMYK Color Model 웹페이지: http://www.flatuicolorpicker.com/
        본 페이지는 다양한 색상을 만들기 위해 CMYK 잉크를 얼만큼씩 섞어야 하는지를 보여준다..
    본 웹페이지의 지정한 색상을 만들기 위해 CMYK 잉크를 얼만큼 써야 하는지 알아보는 프로그래밍다.
    웹페이지에서 지정한 문자열에 대한 데이터를 추출하는 작업을 프로그램으로 구현한다.

1) urllib는 URL 작업을 위한 여러 모듈을 모은 패키지입니다.: 링크: https://docs.python.org/ko/3/library/urllib.html
    1) URL을 열고 읽기 위한 urllib.request
    2) urllib.request에 의해 발생하는 예외를 포함하는 urllib.error
    3) URL 구문 분석을 위한 urllib.parse
    4) robots.txt 파일을 구문 분석하기 위한 urllib.robotparser


2) urllib.request --- Extensible library for opening URLs. 링크: https://docs.python.org/ko/3/library/urllib.request.html#module-urllib.request
    The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world
        --- basic and digest authentication, redirections, cookies and more.

3) Python string methods- 예제와 함께 제공
    https://www.w3schools.com/python/python_ref_string.asp

4) Python urllib tutorial for Accessing the Internet
    https://pythonprogramming.net/urllib-tutorial-python-3/

5) Web Scraping
    https://en.wikipedia.org/wiki/Web_scraping
    https://jcdgods.tistory.com/317

"""


#"""
# -------------------------------------------------------------------------------------------
# 실습 0: URL로 지정된 사이트의 특정 페이지를 읽어 이를 text file로 저장한다.
# -------------------------------------------------------------------------------------------
import urllib.request
page = open('_page.txt', mode='wt', encoding='utf-8')
url = "http://www.flatuicolorpicker.com"    # red와 같음. 디폴트 red-cmyk-color-model

# 1) 지정된 url의 데이터를 가져오기 위한 핸들을 반환한다.
f = urllib.request.urlopen(url) # red와 같음
#f = urllib.request.urlopen(url + '/red-cmyk-color-model')    #위와 같음.

# 2) puple color의 CMYK 구성 비율을 알아보려면 다음 링크를 사용한다.
f = urllib.request.urlopen("http://www.flatuicolorpicker.com/purple-cmyk-color-model")

s = f.read().decode("utf-8")   # 페이지 전체를 읽는다.
print(s); page.write(s)             # 화면에 출력하고 저장한다.
page.close(); exit(0)
#"""


# -------------------------------------------------------------------------------------------
# 실습 1: 아래 URL에 올라있는 다양한 색상의 CMYK 칼라의 비율을 화면에 출력하고 파일에 저장한다.
#   http://www.flatuicolorpicker.com
# 저장되는 파일의 이름: _cmyk.txt
# 잉크젯/칼라 레이저 프린터의 잉크는 CMYK 4종류의 color 토너로 구성되어 있습니다.
# 본 예제는 다양한 색상이 만들어지기 위한 CMYK의 구성 성분을 %로 표시합니다.
# CMYK는 각각 Cyan/Magenta/Yellow/Black 색상을 의미합니다.
# -------------------------------------------------------------------------------------------

import urllib.request
a = open("_cmyk.txt", mode='w', encoding='utf-8')
a.close()

colors = ['red-cmyk-color-model', 'purple-cmyk-color-model', 'blue-cmyk-color-model', 'green-cmyk-color-model',
          'yellow-cmyk-color-model', 'orange-cmyk-color-model', 'grey-cmyk-color-model']
colors = ['red-cmyk-color-model', 'purple-cmyk-color-model']

for i in colors:
    a = open("_cmyk.txt", mode='a', encoding='utf-8')
    f = urllib.request.urlopen("http://www.flatuicolorpicker.com/%s" % i)
    print("\n%s connected" % i)
    s = str(f.read().decode("utf-8"))
    a.write("\n%s -------- \n" % i)
    while 1:
        if s.find('<div class="name"') != -1:        # 문자열이 없으면 -1을 반환한다.

            #  <div class="name" style="color:#ffffff"> Seance</div>
            # 먼저 <div class="name" 스트링을 찾고 다음으로 > 스트링을 찾아서 이곳에서 +1 되는 지점부터 </div>가 잇는 지점까지의 문자열이 새 색상이다.

            s = s[s.find('<div class="name"')+10:]   # 발견된 문자열의 10 글자 이후 부터 새로운 검색대상
            n_clr = s[s.find('>'):s.find('</div>')]  # 새로운 칼라 스트링의 끝에 있는 문자열</div>
            print(n_clr[1:], end=': ')
            a.write("%s: " % n_clr[1:])

            # data-clipboard-text="14%, 90%, 0%, 30%">      해당 색상의 CMYK의 비율
            s = s[s.find('data-clipboard-text='):]
            n_pcnt = s[s.find('"'):s.find('">')]     # 구성비는 " ">로 둘러 싸여 있다.
            print(n_pcnt[1:])
            a.write("%s:\n" % n_pcnt[1:])
        else:
            break
    a.close()
print("\nall done ------")



