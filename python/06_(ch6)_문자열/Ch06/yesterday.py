"""
# 실습 0: 원본
f = open("yesterday.txt", 'r')
yesterday_lyric = f.readlines() # 여러 줄들을 읽어 들인다.
f.close()

contents = ""
for line in yesterday_lyric:
    contents = contents + line.strip() + "\n"

n_of_yesterday = contents.upper().count("YESTERDAY")
print("Number of a Word 'Yesterday'" , n_of_yesterday)
"""




"""
# 실습 1: 간략 수정본 -------
f = open("yesterday.txt", 'r')  # encoding='UTF8'
yesterday_lyric = f.readlines()     # 가사 파일의 각 라인을 원소로 하는 리스트 자료형이 반환된다. 원소 수 = 라인 수
f.close()

print(type(yesterday_lyric), 'number of elements in the list=', len(yesterday_lyric))
# <class 'list'> number of elements in the list= 34

# 리스트의 원소를 관찰하여 보면 맨 끝에 \n이 들어 있음을 알 수 있다.
print(yesterday_lyric)

contents = ''.join(yesterday_lyric)
print(type(contents), 'number of letters=', len(contents))
# <class 'str'> number of letters= 669

#print(contents)     # 파일의 내용이 모두 출력된다.

print("number of '\\n codes=", contents.count('\n'))        # '\\ => '\은 다음 문자를 문자 자체로 처리하라는 요구
# number of '\n codes= 34

n_of_yesterday = contents.upper().count("YESTERDAY")
print("Number of a Word 'Yesterday'=" , n_of_yesterday)
# Number of a Word 'Yesterday'= 9

a=contents.replace('\n', '')    # \n을 ''로 대치. 사실상 삭제.
print(a)

"""

# 실습 2: 파일에서 \n을 삭제 ------
f = open("2017305039신동민.txt", 'r')                        # 저장된 txt 파일을 파이참에서 오픈한다.
file = f.readlines()                            # 파일의 각 라인을 원소로 하는 리스트 자료형이 반환된다.
f.close()
contents = ''.join(file)                        # 리스트인 file 을 str 자료형으로 바꾼다.


Dir_py = contents.count(".py")                  # str 자료형에서 각 파일 확장자를 카운트한다.
Dir_exe = contents.count(".exe")
Dir_txt = contents.count(".txt")

Sum_file = Dir_py+Dir_exe+Dir_txt               # 총 파일의 수를 출력할 변수이다.


Ext_count = 0                                   # 총 확장자의 수의 변수에 초기값을 설정한다.
if Dir_py > 0:                                  # 조건문으로 확장자수를 카운트한다.
    Ext_count += 1
if Dir_exe > 0:
    Ext_count += 1
if Dir_txt > 0:
    Ext_count += 1


byte_py = 0                                     # 총 용량의 변수에 초기값을 설정한다.
byte_exe = 0
byte_txt = 0
list_py = []                                    # 파일의 이름들을 받는 변수를 list 형으로 초기화한다.
list_exe = []
list_txt = []
for i in range(len(file)):                      # 리스트자료형으로 각 인덱스마다 확장자를 찾는다.
    if file[i].count(".py") == 1:               # 각 확장자마다 파일의 용량을 합한다.
        Temp = file[i].split(' ')
        byte_py += int(Temp[-2].replace(',', ''))
        list_py.append(Temp[-1].replace('.py\n', ''))
    elif file[i].count(".exe") == 1:
        Temp = file[i].split(' ')
        byte_exe += int(Temp[-2].replace(',', ''))
        list_exe.append(Temp[-1].replace('.exe\n', ''))
    elif file[i].count(".txt") == 1:
        Temp = file[i].split(' ')
        byte_txt += int(Temp[-2].replace(',', ''))
        list_txt.append(Temp[-1].replace('.txt\n', ''))

Sum_byte = byte_py+byte_exe+byte_txt             # 총 용량을 출력할 변수이다.


print("확장자의 개수와 각 학장자에 따른 파일의 수를 출력하시오.")
print("\t확장자: 개수: 파일크기의 합:")
if Dir_py > 0:                                   # 확장자가 있는 파일이 하나라도 있으면 출력한다.
    print("   py: {0:>7,}{1:>15,}{2:13.6f}%\t{3}".format(Dir_py, byte_py, byte_py/(Sum_byte*1.0), list_py))
if Dir_exe > 0:
    print("  exe: {0:>7,}{1:>15,}{2:13.6f}%\t{3}".format(Dir_exe, byte_exe, byte_exe/(Sum_byte*1.0), list_exe))
if Dir_txt > 0:
    print("  txt: {0:>7,}{1:>15,}{2:13.6f}%\t{3}".format(Dir_txt, byte_txt, byte_txt/(Sum_byte*1.0), list_txt))


Dir_count = 0                                    # 폴더의 수의 변수에 초기값을 설정한다.
for i in range(len(file)):                       # 리스트자료형에 각 인덱스마다 <DIR>가 있는지 확인하고
    if file[i].count("<DIR>") == 1:              # 폴더의 이름을 출력한다.
        Search = file[i].split(' ')
        Dir_count += 1  # 폴더의 수를 카운트한다.
        if Dir_count > 2:
            print("  <{}>".format(Search[-1].replace('\n', '')))

print("총 확장자의 수={:,}, 폴더의 수={:,}, 총 파일의 수={:,}, 총 용량={:,}".format(Ext_count, Dir_count-2, Sum_file, Sum_byte))
# 마지막으로 앞에서 했던 값들을 출력한다.



import SearchExt
f = open("2017305039신동민.txt", 'r')            # 저장된 txt 파일을 파이참에서 오픈한다. #encoding='UTF8'#
file = f.readlines()                            # 파일의 각 라인을 원소로 하는 리스트 자료형이 반환된다.
f.close()
contents = ''.join(file)                        # 리스트인 file 을 str 자료형으로 바꾼다.

def indexsearch(list1, n):
    count = 0
    for i in range(len(list1)):
        if list1[i] == n:
            count += 1
    return count

def countExt():
    list1 = []
    list3 = []
    for j in range(len(file)):
        if file[j].count("<DIR>") == 0:
            Temp = file[j].split(' ')
            if Temp.count('오전') == 1 or Temp.count('오후') == 1:
                Temp2 = Temp[-1].split('.')
                Temp3 = len(Temp2[-1].split(' '))
                if Temp3 <= 10:
                    list1.append(Temp2[-1].replace('\n', ''))

    list1.sort()
    list2 = list(set(list1))
    list2.sort()

    for i in list2:
       list3.append(indexsearch(list1, i))
    return list2, list3


listA, listB = countExt()
def bytesearch(i):
    Sum = 0
    for j in range(len(file)):
        if file[j].count(i) == 1:
            Temp = file[j].split(' ')
            a = (Temp[-2].replace(',', ''))
            Sum += int(a)
    return Sum


def byteSum():
    listC = []
    for i in listA:
        listC.append(bytesearch(i))
    return listC

listC = byteSum()

def listname(i):
    listname1 = []
    for j in range(len(file)):
        if file[j].count(i) == 1:
            Temp = file[j].split(' ')
            listname1.append(Temp[-1].replace('.', '').replace(i, '').replace('\n', ''))
    return listname1


def filelist():
    listD = []
    for i in listA:
        listD.append(listname(i))
    return listD

listD = filelist()


print("확장자의 개수와 각 학장자에 따른 파일의 수를 출력하시오.")
print("\t확장자:\t  개수:\t  파일크기의 합:\t 퍼센트 용량:\t 파일 리스트")
for i in range(len(listA)):
    print("   {:>5}: {:>7,}{:>15,}{:13.6f}%\t{}".format(listA[i], listB[i], listC[i], listC[i]/(sum(listC)*1.0), listD[i]))


Dir_count = 0                                    # 폴더의 수의 변수에 초기값을 설정한다.
for i in range(len(file)):                       # 리스트자료형에 각 인덱스마다 <DIR>가 있는지 확인하고
    if file[i].count("<DIR>") == 1:              # 폴더의 이름을 출력한다.
        Search = file[i].split(' ')
        Dir_count += 1                           # 폴더의 수를 카운트한다.
        if Dir_count > 2:
            print("  <{}>".format(Search[-1].replace('\n', '')))

print("총 확장자의 수={:,}, 폴더의 수={:,}, 총 파일의 수={:,}, 총 용량={:,}".format(len(listA), Dir_count-2, sum(listB), sum(listC)))
# 마지막으로 앞에서 했던 값들을 출력한다.
