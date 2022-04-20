"""
연습:
    zip() 함수
    enumerate() 함수
    time()함수
"""


import os
directory =  "D:/Work/@@Python/LectureMaterials/report 공고/2차/Lab/mission"
directory =  "mission"


"""
# --------------------------------------------------------------------------------------
# 실습 1: splitext 함수 연습
# 스트링 변수를 입력받아 파일 path와 파일 확장자를 분리하여 반환한다.
# --------------------------------------------------------------------------------------

path = '/home/User/Desktop/file.txt'

# splitext 함수는 path와 파일명으로 주어진 입력 스트링에 대해 2개의 값을 반환한다.
# [0] : path
# [1] : 파일 확장자
root_ext = os.path.splitext(path)

# print root and ext of the specified path
print("root part of '% s':" % path, root_ext[0])
print("ext part of '% s':" % path, root_ext[1], "\n")

exit()
"""


# ----------------------------------------------------------------------
# 실습 2: os.path.join 함수
#   디렉터리와 파일 이름을 이어주는 함수.
#   디렉터리를 포함한 전체 경로를 쉽게 만들 수 있다.
#   https://www.geeksforgeeks.org/python-os-path-join-method/
# ----------------------------------------------------------------------
print("\nos.path.join 함수")
import time

s_time = time.time()

path = "/home"
print(1, os.path.join(path, "User/Desktop", "file.txt"))
# /home\User/Desktop\file.txt

path = "User/Documents"
print(2, os.path.join(path, "/home", "file.txt"))
# /home\file.txt
# "/home"이 절대적 위치라서 path 지정이 무시되었다.

path = "/User"
print(3, os.path.join(path, "Downloads", "file.txt", "/home"))
# /home

path = "/home"
print(4, os.path.join(path, "User/Public/", "Documents", ""))
# /home\User/Public/Documents\

path = ''  # 현재 위치. '.'도 OK.
a = os.path.join(path, "layer_1_1")
print(5.1, a)
file_list = os.listdir(a)
#file_list = os.listdir('.\layer_1')
print(5.2, file_list)
os.system('type '+ a + '\\' + file_list[-1])    # 맨 마지막 목록 파일을 type한다.
print()

c_time = time.time()

print('time:', c_time-s_time)
exit()



# --------------------------------------------------------------------------------------
# 실습 3: os.walk(path) 함수 연습
# 주어진 경로에 존재하는 서브폴더와 파일들을 tuple 자료로 반환한다.
# --------------------------------------------------------------------------------------
lst_py = []         # 확장자가 py인 full path가 포함된 파일 목록
lst_txt = []         # 확장자가 txt인 full path가 포함된 파일 목록
lst_pic =[]         # 확장자가 그림 파일인 full path가 포함된 파일 목록
for i, (path, sub_dir, files) in enumerate(os.walk(directory)):
    print(f'\nloop {i} .....')
    print(f'1) path={path}')
    print(f'2) sub_dir={sub_dir}')
    print(f'3) files={files}')
    for filename in files:
        # splitext method returns a tuple that represents root and ext part of the specified path name.
        ext = os.path.splitext(filename)[-1]        # 파일 확장자를 반환함.
        ext_and_lst = zip(['.py', '.txt', '.jpg', '.gif', '.png', '.tif'], [lst_py, lst_txt, lst_pic, lst_pic, lst_pic, lst_pic])
        for ext_nm, lst_n in ext_and_lst:
            if ext_nm == ext.lower():       # 소문자로 바꾸어 비교한다.
                a = os.path.join(path, filename)
                print(a)
                lst_n.append(a)
                break
print()
print(lst_py)
print(lst_txt)
print(lst_pic)
