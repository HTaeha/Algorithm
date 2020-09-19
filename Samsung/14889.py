from itertools import combinations, permutations

if __name__ == "__main__":
    result = 100*20 + 1
    N = int(input())

    arr = []
    team = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
        team.append(i)

    team = set(team)

    combs = list(combinations(team, int(N/2)))
    for i in range(int(len(combs)/2)):
        t1 = 0
        t2 = 0
        for p in permutations(combs[i], 2):
            t1 += arr[p[0]][p[1]]

        team2 = team - set(combs[i])
        for p in permutations(team2, 2):
            t2 += arr[p[0]][p[1]]

        result = min(result, abs(t1-t2))

    print(result)
