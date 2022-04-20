def addition(x, y):
    return x + y

def divided_by_2(x):
    return x / 2

# 타이핑 수고를 덜기위해 좀더 짧은 길이의 함수명을 사용해 재 정의한다.
def add(x, y):
    return x + y

def div(x):
    return x / 2

def main():
    base_line = float(input("밑변의 길이는? "))
    upper_edge = float(input("윗변의 길이는? "))
    height = float(input("높이는? "))

    print("넓이는:", divided_by_2(addition(base_line, upper_edge) * height))

if __name__ == "__main__":
    main()
else:
    print("Modified module 'abcd2' is being loaded.")