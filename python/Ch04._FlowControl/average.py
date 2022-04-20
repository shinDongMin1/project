# 다음은 학생 5명의 3개 과목의 과목별 취득 점수이다.
# 학생별 과목 평균(3개 과목에 대한)을 구하시오.
# => [47.0, 74.0, 51.0, 60.0, 90.0]

"""
# =======================================================================================================
# 실습 1: 교재 원본 파일
# =======================================================================================================
kor_score = [49, 80, 20, 100, 80]
math_score = [43, 60, 85, 30, 90]
eng_score = [49, 82, 48, 50, 100]

midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
i = 0
for subject in midterm_score:
    for score in subject:
        student_score[i] += score                   # 학생마다 개별로 교과 점수를 저장
        i += 1                                      # 학생 인덱스 구분
    i = 0                                           # 과목이 바뀔 때 학생 인덱스 초기화
else:
    a, b, c, d, e = student_score                   # 학생별 점수를 언패킹
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print(student_average)
"""




# =======================================================================================================
# 미션 1: 문제 추가
#   학생별 과목 평균 외에 과목별 학생들의 평균을 구하시오.
#   즉, 3개 과목에 대한 5명 학생의 평균을 구하시오.
#   조건- 현재의 for loop 구조를 유지하는 것으로 한다.
#
# 출력 사례:
#   average of each student= [47.0, 74.0, 51.0, 60.0, 90.0]
#   average of each subject= [65.8, 61.6, 65.8]
# =======================================================================================================

kor_score = [49, 80, 20, 100, 80]
math_score = [43, 60, 85, 30, 90]
eng_score = [49, 82, 48, 50, 100]

midterm_score = [kor_score, math_score, eng_score]

#import numpy as np

#mid = np.array(midterm_score)
#print(type(mid))

student_score = [0, 0, 0, 0, 0]
i = 0
for subject in midterm_score:
    for score in subject:
        student_score[i] += score                   # 학생마다 개별로 교과 점수를 저장
        i += 1                                      # 학생 인덱스 구분
    i = 0                                           # 과목이 바뀔 때 학생 인덱스 초기화
else:
    a, b, c, d, e = student_score                   # 학생별 점수를 언패킹
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print(student_average)

k = 0
for i in midterm_score:
    Sum = 0
    for j in i:
        Sum += j
    student_score[k] = Sum / 5
    k += 1
else:
    x, y, z, g, h = student_score
    student_average = [x, y, z]
    print(student_average)

exit(0)
