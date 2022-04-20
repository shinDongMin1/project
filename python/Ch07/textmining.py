
from collections import defaultdict

text = """A press release is the quickest and easiest way to get free publicity. 
If well written, a press release can result in multiple published articles about your firm and its products. 
And that can mean new prospects contacting you asking you to sell to them. ….""".lower().split()

# 아래 문장에 나오는 단어의 수를 세는 프로그램
text = 'AA bbbb CCCC ss eeeeeeeeee 11'
word_count = defaultdict(lambda: 0)  # Default 0
for word in text:
    word_count[word] += 1

from collections import OrderedDict
# t[1]이면 value를 기준으로 소팅했는데,
# reverse가 됨으로써 빈도수가 많은 단어 순으로 재정렬된다.
for i, v in OrderedDict(sorted(word_count.items(),
            key=lambda t: t[1], reverse=True)).items():
    print(i, v)

