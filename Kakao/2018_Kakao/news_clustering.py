# 2018 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/17677
def solution(str1, str2):
    answer = 0

    s1 = seperate_str(str1)
    s2 = seperate_str(str2)

    if len(s1) == 0 and len(s2) == 0:
        return 65536

    # eliminate duplicated data.
    set_s1 = set(s1)
    set_s2 = set(s2)
    # intersection of set_s1 and set_s2.
    inter = set_s1.intersection(set_s2)
    # union of set_s1 and set_s2.
    union = set_s1.union(set_s2)
    diff = union-inter

    set_s1.clear()
    set_s2.clear()

    # key : 2 words string
    # val : the number of its key.
    # ex) s = ['fr', 'ra', 'fr', 'ce']
    #     dict_s = ['fr' : 2, 'ra' : 1, 'ce' : 1]
    dict_s1 = dict()
    dict_s2 = dict()

    # make dictionary.
    for i, data in enumerate(s1):
        if data in dict_s1:
            dict_s1[data] += 1
        else:
            dict_s1[data] = 1
    for i, data in enumerate(s2):
        if data in dict_s2:
            dict_s2[data] += 1
        else:
            dict_s2[data] = 1

    inter_sum = 0
    uni_sum = 0

    for data in inter:
        if dict_s1[data] > dict_s2[data]:
            inter_sum += dict_s2[data]
            uni_sum += dict_s1[data]
        else:
            inter_sum += dict_s1[data]
            uni_sum += dict_s2[data]
    for data in diff:
        if data in dict_s1:
            uni_sum += dict_s1[data]
        if data in dict_s2:
            uni_sum += dict_s2[data]
            
    answer = int((inter_sum/uni_sum) * 65536)

    return answer

# Split string 2words and make all word lowercase.
# ex) "France" -> "fr", "ra", "an", "nc", "ce"
def seperate_str(s):
    seperate = []
    
    for i, data in enumerate(s):
        if i == len(s)-1:
            break
        if s[i:i+2].isalpha():
            seperate.append(s[i:i+2].lower())

    return seperate

if __name__ == "__main__":
    str1 = "AA"
    str2 = "AAA"

    solution(str1, str2)
