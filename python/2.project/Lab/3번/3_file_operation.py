"""

File_object = open(r"File_Name", "Access_Mode")

Access_Mode: open() 함수의 인자.
    "r" : Read - Default value. Opens a file for reading, error if the file does not exist
    "a" : Append - Opens a file for appending, creates the file if it does not exist
    "w" : Write - Opens a file for writing, creates the file if it does not exist
    "x" : Create - Creates the specified file, returns an error if the file exists
    "w+": Write and Read - Open the file for reading and writing.
            For an existing file, data is truncated and over-written.
            The handle is positioned at the beginning of the file.
    "r+" : Read and Write -  Open the file for reading and writing.
            The handle is positioned at the beginning of the file.
            Raises I/O error if the file does not exists.
    "a+" : Append and Read - Open the file for reading and writing.
            The file is created if it does not exist.
            The handle is positioned at the end of the file.
            The data being written will be inserted at the end, after the existing data.


    "t" - Text - Default value. Text mode
    "b" - Binary - Binary mode (e.g. images)

    결합사례: rt, wb ...

text 파일:
Note: ‘\n’ is treated as a special character of two bytes. LF -> CR, LF로 확장. 0x0a => 0x0d, 0x0a로 확장

    텍스트 파일용 읽어 내는 함수 3가지
    read() : Returns the read bytes in form of a string.
        Reads n bytes, if no n specified, reads the entire file.
        File_object.read([n])
    readline() : Reads a line of the file and returns in form of a string.
        For specified n, reads at most n bytes. However, does not reads more than one line, even if n exceeds the length of the line.
        File_object.readline([n])
    readlines() : Reads all the lines and return them as each line a string element in a list.
        File_object.readlines()

    텍스트 파일용 쓰는 함수 2가지
    write() : Inserts the string str1 in a single line in the text file.
        File_object.write(str1)
    writelines() : For a list of string elements, each string is inserted in the text file.
        Used to insert multiple strings at a single time.
        File_object.writelines(L) for L = [str1, str2, str3]


링크:
    https://www.geeksforgeeks.org/writing-to-file-in-python/


참고: 파일이나 폴더를 삭제하기
    import os
    os.remove("write.txt")      # 파일 지우고 싶으면;
    os.rmdir("myfolder")        # 폴더 삭제하고 싶으면


"""

# 현재 수행하는 파일의 이름을 지정하는 변수: __file__
# 파일의 크기를 알아내는 함수: os.path.getsize
import os


# --------------------------------------------------------------------------------------
# 실습 0: 자신의 파일의 이름과 파일 크기 알아내기
#  __file__ : current file name including path
# --------------------------------------------------------------------------------------
print(f'Name of this file including path: \n__file__="{__file__}"')
sz = os.path.getsize(__file__)
print(f'file size={sz:#,}')

idx = __file__.rfind('/')  # 주의!!: directory 구분 문자='/' 모듈에서는 '\'
sz = os.path.getsize(__file__[idx+1:])
print(f'\nfile name excluding path: "{__file__[idx+1:]}"')
print(f'file size={sz:#,}')
exit()

"""
# --------------------------------------------------------------------------------------
# 실습 1: 본 예제를 수행할 때마다 새로 문장을 추가하기 때문에 생성된 파일의 내용이 많아진다.
# append mode: 파일이 없으면 생성하고 있으면 원래 있는 것에 추가한다.
# text mode: default mode. text 문서를 다룬다 't'로 명시할 수 있다.
# --------------------------------------------------------------------------------------
f = open("append.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("append.txt", "r")
print(f.read())
# By default the read() method returns the whole text, 
# but you can also specify how many characters you want to return: read(100)- 100바이트 읽는다.

exit()
"""

"""
# --------------------------------------------------------------------------------------
# 실습 2: 텍스트 파일을 생성하여 쓰고 읽어서 확인해 보기
# --------------------------------------------------------------------------------------
file1 = open('myfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"

# Writing a string to file
file1.write(s)

# Writing multiple strings at a time
file1.writelines(L)

# Closing file
file1.close()

# Checking if the data is written to file or not
file1 = open('myfile.txt', 'r')
print(file1.read())
file1.close()

exit()
"""


# --------------------------------------------------------------------------------------
# 실습 3: 1바이트씩 읽어 처리한다.
# --------------------------------------------------------------------------------------
file = open("2_sample.txt", "rb")
byte = file.read(1)    # byte object
while byte:     # byte=false at end of file.
    print(type(byte), byte, ord(byte), hex(ord(byte)), f'{ord(byte):#2x}')
    #print(hex(byte))    # 'bytes' object cannot be interpreted as an integer
    byte = file.read(1)
#file. close()

# ord(): Returns an integer representing the Unicode code point of the given Unicode character.
print('\n한:', ord('한'), f'{ord("한"):#2x}')

# 한꺼번에 처리한다.
file = open("2_sample.txt", "rb")
# 같은 파일을 2번 열지 않으려면 파일을 닫지 말고 아래 seek()를 수행하면 된다.
#file.seek(0) # 포인터를 0으로 향하게 만든다.
#file.seek(1)        # 맨 처음 바이트는 건너뛰고 1번 부터 액세스하게 만든다.

max_bytes = 10000
bt_obj = file. read(max_bytes)    # byte object
print('\nbt_obj:', type(bt_obj), len(bt_obj), bt_obj)

print("\n'bytes' object is index accessable.")
for i in range(len(bt_obj)):
    print(f'bt_obj[{i}]:', type(bt_obj[i]), f'{bt_obj[i]:#2x}')

print("\n'bytes' object is iterable.")
for bt in bt_obj:  # bt_obj는 byte object이지만 bt는 int type이다.
    #print(type(byte), byte, ord(byte), hex(ord(byte)))
    print(type(bt), bt, hex(bt), f'{bt:#02x}')
file.close()
