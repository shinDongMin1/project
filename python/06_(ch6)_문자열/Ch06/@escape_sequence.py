"""
Python 3 Escape Sequences
    http://www.python-ds.com/python-3-escape-sequences
"""
# Backslash and newline ignored. \이후에는 주석문 불가. space도 안됨.
print("1. line1 \
line2 \
line3")     # 1. line1 line2 line3

# literal character. 문자 그대로 하라..
print("2. \\")     # 2. \     \ 이후에는 escape sequence가 아니라 문자 \이다.
print('3. \'')     # 3. '     \ 이후에는 따옴표 '가 아니라 문자 '이다.
print('4. \"')     # 4. "     \ 이후에는 따옴표 "가 아니라 문자 "이다.

# control character. 장치, 커저 제어 용도...

# \r: carriage return(CR)   커저를 그 줄 맨 앞으로 보내기.
# 2345는 남아있어야 하는데 파이썬에는 모두 지워진다.
print("5. Hello12345\rWorld!")   # World!

# \n: linefeed(LF)  줄 바꾸고, 맨 앞으로 커저를 보낸다.
print("6. Hello\nWorld!")   # 6. Hello
                            # World!
# \b: backspace
print("7. Hello\bWorld!")   # 7. HellWorld!

# /t: tab
print("8. Hello\tWorld!")   # 8. Hello	World!

# \xhh:	Character with hex value hh
print("9. \x41\x42\x30\x31\x39\x61\x62")    # 9. AA019ab

#  아래는 참고 사항. 추후 한글 인코딩에 대해 고찰 예정
a = b"\xed\x95\x9c"      # bytes object for UTF-8 Hanguel 한
print(a.decode('utf-8'))                    # 한
print(a.decode('utf-8').encode('utf-8'))    # b'\xed\x95\x9c'
print(a.decode('utf-8').encode('cp949'))    # b'\xc7\xd1'
# decode(encoding='UTF-8',errors='strict')
#   Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding.
# encode(encoding='UTF-8',errors='strict')
#   Determines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix;
#   returns true if so and false otherwise.

