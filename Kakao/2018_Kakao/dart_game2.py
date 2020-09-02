# 다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682

import re
def solution(dartResult):
    answer = []

    # Regular Expression
    exp = "([\d]+)([SDT][*#]?)([\d]+)([SDT][*#]?)([\d]+)([SDT][*#]?)"
    regex = re.compile(exp)
    score = regex.search(dartResult).groups()

    score_merge = []

    for i in range(0, len(score), 2):
        score_merge.append((score[i], score[i+1]))
    print(score_merge)

    for i, s in enumerate(score_merge):
        num, t = s
        num = int(num)
        if t[0] == 'S':
            answer.append(num)

        elif t[0] == 'D':
            answer.append(num**2)

        elif t[0] == 'T':
            answer.append(num**3)

        if len(t) == 2:
            if t[1] == '*':
                answer[i] *= 2
                if i != 0:
                    answer[i-1] *= 2
            elif t[1] == '#':
                answer[i] *= -1

    answer = sum(answer)
    return answer

if __name__ == "__main__":
    dartResult = "1S2D*3T"
    dartResult = "1D2S#10S"
    print(solution(dartResult))
