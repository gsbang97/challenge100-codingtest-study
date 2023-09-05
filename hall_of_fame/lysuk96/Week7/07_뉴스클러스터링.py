#https://programmers.co.kr/learn/courses/30/lessons/17677
# 왜 dict만 쓴 코드가 살짝 더 느릴까? dict.keys()때문인가?

from collections import defaultdict
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    d1 = defaultdict(int)
    d2 = defaultdict(int)

    # dict만 쓴 코드
#     for i in range(len(str1)-1):
#         if str1[i] in alphabet and str1[i+1] in alphabet:
#             d1[str1[i:i+2]] +=1
#     for i in range(len(str2)-1):
#         if str2[i] in alphabet and str2[i+1] in alphabet:
#             d2[str2[i:i+2]] +=1

#     l1_set = set(d1.keys())
#     l2_set = set(d2.keys())

    # list에 따로 저장한 코드
    l1 = [str1[i:i+2] for i in range(len(str1)-1) \
          if str1[i] in alphabet and str1[i+1] in alphabet]
    l2 = [str2[i:i+2] for i in range(len(str2)-1) \
          if str2[i] in alphabet and str2[i+1] in alphabet]

    for key in l1:
        d1[key] +=1
    for key in l2:
        d2[key] +=1
    l1_set = set(l1)
    l2_set = set(l2)


    u = l1_set | l2_set
    g = l1_set & l2_set

    hap = sum(max(d1[key], d2[key]) for key in u)
    gyo = sum(min(d1[key], d2[key]) for key in g)
    return 65536 if hap == 0 else int(gyo / hap * 65536)