
# XOR 연산으로 8비트 데이터를 암호화하고, 다시 복호화하는 연산을 보인다.
# data와 res_data가 같은 결과이다.
# xor_data를 파일에 저장하여 정보를 보호한다.
# 복호화하기 위해서는 code8이 필요하다. 이는 암호화와 복호화를 위한 key로 사용한다.
data = 0b1010_1100
print('1. data:', type(data), data, f'{data:#x}')

code8 = 0b1000_0000
print('2. code8', type(code8), code8, f'{code8:#x}')

xor_data = data ^ code8
print('3. xor_data', type(xor_data), xor_data, f'{xor_data:#x}')

res_data = xor_data ^ code8
print('4. res_data', type(res_data), res_data, f'{res_data:#x}')

