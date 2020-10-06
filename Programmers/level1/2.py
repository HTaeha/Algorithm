def solution(N, stages):
    answer = []
    
    temp = [0 for _ in range(N+2)]
    for s in stages:
        temp[s] += 1
    _sum = temp[N+1]
    for i in range(N, 0, -1):
        _sum += temp[i]
        if _sum == 0:
            answer.append([0, i])
        else:
            answer.append([temp[i]/_sum, i])

    temp = sorted(answer, key = lambda x:(x[1]))
    temp = sorted(temp, key = lambda x:(-x[0]))
    answer = []
    for ans in temp:
        answer.append(ans[1])

    return answer

if __name__ == "__main__":
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages))
