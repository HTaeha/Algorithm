# 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065

import re
def solution(s):
    answer = []

    s = s[1:-1]
    exp = "({[\d,]+})"
    regex = re.compile(exp)

    t = regex.findall(s)

    # string을 int가 들어있는 list로 변환.
    tuples = []
    for data in t:
        data = data[1:-1]
        temp = list(map(int, data.split(',')))
        
        tuples.append(temp)

    # 길이가 짧은 순서대로 정렬.
    tuples = sorted(tuples, key = lambda x : len(x))

    # set에 저장하면서 안 나온 숫자들을 answer에 추가.
    check = set()
    for l in tuples:
        for num in l:
            if num not in check:
                check.add(num)
                answer.append(num)

    return answer

if __name__ == "__main__":
    s = "{{2,1,3,4,5},{2},{2,1},{2,1,3},{2,1,3,4}}"
    print(solution(s))
