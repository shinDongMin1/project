#decimal = 10
decimal = 255
result = ''
while (decimal > 0):
    remainder = decimal % 2     # 2로 나눈 나머지를 취한다.
    decimal = decimal // 2      # 2로 나눈 몫을 취한다.
    result = str(remainder) + result    # 나머지를 역순으로 저장하기 위해 result를 뒤에서 더한다.
print(result)

# 주의!!!
# result += str(remainder) 로 처리하면 나머지가 역순으로 만들어지지 않는다.