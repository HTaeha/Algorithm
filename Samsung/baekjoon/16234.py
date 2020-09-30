from collections import deque

def check(value):
    global L, R
    value = abs(value)
    if value >= L and value <= R:
        return True
    else:
        return False

def bfs(start, visited):
    global N, Map

    if start in visited:
        return [0, []]

    q = deque()
    q.append(start)
    visited.append(start)
    result = [start]
    _sum = Map[start[0]][start[1]]
    while q:
        idx = q.popleft()
        [i, j] = idx

        temp = [i-1, j]
        if i-1 >= 0 and temp not in visited and check(Map[i][j]-Map[i-1][j]):
            q.append(temp)
            visited.append(temp)
            result.append(temp)
            _sum += Map[temp[0]][temp[1]]
        temp = [i+1, j]
        if i+1 < N and temp not in visited and check(Map[i][j]-Map[i+1][j]):
            q.append(temp)
            visited.append(temp)
            result.append(temp)
            _sum += Map[temp[0]][temp[1]]
        temp = [i, j-1]
        if j-1 >= 0 and temp not in visited and check(Map[i][j]-Map[i][j-1]):
            q.append(temp)
            visited.append(temp)
            result.append(temp)
            _sum += Map[temp[0]][temp[1]]
        temp = [i, j+1]
        if j+1 < N and temp not in visited and check(Map[i][j]-Map[i][j+1]):
            q.append(temp)
            visited.append(temp)
            result.append(temp)
            _sum += Map[temp[0]][temp[1]]
        
    return [_sum, result]

def calculate(lst):
    global Map

    for _sum,l in lst:
        value = len(l)
        for i, j in l:
            Map[i][j] = _sum//value

if __name__ == "__main__":
    N, L, R = map(int, input().split())

    Map = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        Map.append(temp)

    count = 0
    while True:
        country = []
        visited = []
        flag = False
        for i in range(N):
            for j in range(N):
                [val, temp] = bfs([i, j], visited)
                if len(temp) > 1:
                    flag = True
                    country.append([val, temp])
        
        if not flag:
            break

        calculate(country)
        count += 1

    print(count)
