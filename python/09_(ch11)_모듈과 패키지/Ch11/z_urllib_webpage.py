"""
urllib는 URL 작업을 위한 여러 모듈을 모은 패키지입니다.: 링크: https://docs.python.org/ko/3/library/urllib.html
    1) URL을 열고 읽기 위한 urllib.request
    2) urllib.request에 의해 발생하는 예외를 포함하는 urllib.error
    3) URL 구문 분석을 위한 urllib.parse
    4) robots.txt 파일을 구문 분석하기 위한 urllib.robotparser


urllib.request --- Extensible library for opening URLs. 링크: https://docs.python.org/ko/3/library/urllib.request.html#module-urllib.request
    The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world
        --- basic and digest authentication, redirections, cookies and more.

Python Urllib Module
    https://www.geeksforgeeks.org/python-urllib-module/

ulib3 모듈
    https://urllib3.readthedocs.io/en/latest/user-guide.html


requests 모듈
     https://requests.readthedocs.io/en/master/


Python urllib tutorial for Accessing the Internet
    https://pythonprogramming.net/urllib-tutorial-python-3/ 접근을 거부당할 경위 회피 테크닉 포함


"""


#"""
# ---------------------------------------------------------------------------
# 실험 1: urlopen()이 반환하는 context manager의 method들
# urlopen function always returns an object which can work as context manager,
# and has methods such as
#   geturl() — return the URL of the resource retrieved, commonly used to determine if a redirect was followed
#   info() — return the meta-information of the page, such as headers, in the form of an email.message_from_string() instance (see Quick Reference to HTTP Headers)
#   getcode() – return the HTTP status code of the response. 아래는 중요한 반환 값을 보인 것이다. 
#       200 (성공, Success): 서버에 요청한 페이지가 성공적으로 처리되었음을 의미
#       403 (금지, Forbidden): 권한이 없는 등의 이유로 서버에 요청한 페이지가 제공 거부되었음을 의미
#       404 (찾을 수 없음, Not Found): 서버에 요청한 페이지가 존재하지 않음을 의미
#       500 (내부 서버 오류, Internal Server Error): 서버의 오류로 페이지가 제공되지 않음을 의미
# 
# 
# ---------------------------------------------------------------------------
import urllib.request       # package.module
x = urllib.request.urlopen('https://www.google.com/')
print('url=', x.geturl())   # 접속한 URL를 반환. url= https://www.google.com/
print("\ninfo() -------------------------------")
print(x.info())             # URL에 연관된 메타 정보를 담은 매핑 객체를 반환
print("\ngetcode() -------------------------------")
print(x.getcode(), x.status)    # 응답의 http 상태 코드. 두 값이 같음. 200 200. (성공, Success)
print("\nread() -------------------------------")
txt = x.read()  # page문서를 바이트 코드로 다운
print('len(txt)=', len(txt))
print(txt)
exit(0)
#"""



"""
# ---------------------------------------------------------------------------
# 실험 2: Web page source 출력 및 파일 저장
# ---------------------------------------------------------------------------
import urllib.request       # package.module

# 1) 바이트 오브젝트를 decoding 안하고 출력. 
url = 'http://www.python.org/'
print('\n1) No decoding -------')
f = urllib.request.urlopen(url)
print(type(f))      # <class 'http.client.HTTPResponse'>
c = f.read(100)     # 100 byte 읽기
print('type(c)=', type(c))      # <class 'bytes'>
print('len(c)=', len(c))
print(c)

# 2) utf-8로 디코드하여 출력
print('\n2) utf-8 decoding -------')
f = urllib.request.urlopen(url)
c = f.read(100).decode('utf-8')
print('type(c)=', type(c))      # <class 'str'>
print(c)
exit(0)
"""


#"""
# ---------------------------------------------------------------------------
# 실험 3: Web page source의 파일 저장
# ---------------------------------------------------------------------------
import urllib.request       # package.module
url = 'https://en.wikipedia.org/wiki/BTS_(band)'
url = 'https://ko.wikipedia.org/wiki/%EB%B0%A9%ED%83%84%EC%86%8C%EB%85%84%EB%8B%A8'
#url = 'https://ce.skuniv.ac.kr/ce_professor'
#url = 'https://www.naver.com'

print('\n1) Saving web page in utf-8 text -------')
f = urllib.request.urlopen(url)
c = f.read().decode('utf-8')
print(type(c))      # <class 'str'>
f = open('_source1.html', mode='wt', encoding='utf-8')
print(type(f))      # <class '_io.TextIOWrapper'>
f.write(c)
f.close()

print('\n2) Saving web page in byte object -------')
req = urllib.request.Request(url)
bto = urllib.request.urlopen(req).read()   # byte object를 반환
print(type(bto))    # <class 'bytes'>
f = open('_source2.html', 'wb')
f.write(bto)
f.close()
exit(0)
#"""




# ---------------------------------------------------------------------------
# 참고: requests 모듈 활용
#       https://requests.readthedocs.io/en/master/
# Requests allows you to send HTTP/1.1 requests extremely easily.
# There’s no need to manually add query strings to your URLs,
# or to form-encode your POST data import requests
#
#       https://www.w3schools.com/python/module_requests.asp
#
# Web page source의 파일 저장
# ---------------------------------------------------------------------------
import requests
url = 'https://www.naver.com'
url = 'https://en.wikipedia.org/wiki/BTS_(band)'
url = 'https://ko.wikipedia.org/wiki/%EB%B0%A9%ED%83%84%EC%86%8C%EB%85%84%EB%8B%A8'
#url = 'https://ce.skuniv.ac.kr/ce_professor'

response = requests.get(url)
print(response.encoding)
f = open('_source3.html', 'w', encoding=response.encoding)
f.write(response.text)
f.close()
exit(0)


