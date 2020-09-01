# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []

    people_num = len(stages)
    count = [0 for _ in range(N+1)]
    for stage in stages:
        count[stage-1] += 1

    for i, people in enumerate(count):
        if i == N:
            break
        if i != 0:
            people_num -= count[i-1]

        if people_num == 0:
            answer.append([i+1, 0])
        else:
            answer.append([i+1 ,people/people_num])

    answer = list(map(list, zip(*sorted(answer, key = lambda x : -x[1]))))[0]

    return answer

if __name__ == "__main__":
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages))
