for i in range(10):
    print(i)
else:
    print("End of Program")

while i < 43:
    i += 1
else:
    print(i)

# else는 if 문 뿐만 아니라 for ~ in, while과도 함께 쓰이는 듯 하다.
# if 문과 함께 쓰인다면 if 혹은 else 블럭문이 둘 중의 하나만 수행되는 반면
# for ~ in, while과 함께 수행되면 해당 블럭이 수행되고 난 후
# else 블럭이 추가로 한 번 더 수행된다.
# 위 사례의 블럭은 다음과 같이 코딩하는 것과 동작이 같다.
# while i < 43:
#     i += 1
# print(i)
