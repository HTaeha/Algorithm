def solution(s):
    answer = 0

    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

    s_lst = []
    for char in s:
        s_lst.append(char)

    print(len(s_lst))
    i = 0
    j = 0
    start = [0, 0]
    while True:
        print(i, j)
        if i != j:
            if s_lst[i] != s_lst[j]:
                dp[i][j] = j-i
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        answer += dp[i][j]

        i += 1
        j += 1

        if i == 1 and j == len(s_lst):
            break
        elif i == len(s_lst) or j == len(s_lst):
            start = [start[0], start[1]+1]
            i = start[0]
            j = start[1]

    return answer

s = "baby"
print(solution(s))
