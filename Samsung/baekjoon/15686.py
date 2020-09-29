def dfs(idx, count, value):
    global Map, home, chicken, result

    if count == value:
        _sum = 0
        for h in home:
            _sum += calculate(Map, h)
        result = min(result, _sum)
    else:
        for chi_i in range(idx, len(chicken)):
            i, j = chicken[chi_i]
            Map[i][j] = 0
            dfs(chi_i+1, count+1, value)
            Map[i][j] = 2
        
def calculate(lst, idx):
    global chicken

    result = 987654321
    for c in chicken:
        if lst[c[0]][c[1]] == 2:
            temp = abs(idx[0]-c[0]) + abs(idx[1]-c[1])
            result = min(result, temp)
    return result

if __name__ == "__main__":
    N, M = map(int, input().split())

    Map = []
    home = []
    chicken = []
    for i in range(N):
        temp = list(map(int, input().split()))
        for j, data in enumerate(temp):
            if data == 2:
                chicken.append([i, j])
            elif data == 1:
                home.append([i, j])
        Map.append(temp)

    result = 987654321

    dfs(0, 0, len(chicken)-M)

    print(result)
