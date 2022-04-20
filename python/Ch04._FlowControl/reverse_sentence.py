sentence = "I love you."
reverse_sentence = ''
for char in sentence:
    # 아래의 1)과 2는 numeric value를 더할 때는 같은 연산이다.
    reverse_sentence = char + reverse_sentence  # 1) 현재의 문자에 읽은 문자열을 붙인다.
    #reverse_sentence += char                   # 2) 읽은 문자열에 현재 문자를 붙인다.
    print(char+'|'+reverse_sentence)

print()
print(reverse_sentence)
print(len(sentence), len(reverse_sentence))


"""
sentence = "I love you."
reverse_sentence = ''
for char in sentence:
    reverse_sentence = char + reverse_sentence
    print(char+'|'+reverse_sentence)

print()
print(reverse_sentence)
print(len(sentence), len(reverse_sentence))

"""
