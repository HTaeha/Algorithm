from collections import deque

direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def check(value):
    global L, R
    value = abs(value)
    if value >= L and value <= R:
        return True
    else:
        return False

# country 끼리 체크하면서 합쳐지면 다 안 돌고 흡수하도록 바꾸기.
def bfs(start, visited):
    global N, Map, direction

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

        for d in range(4):
            x = i + direction[d]
            y = j + direction[d]
            temp = [x, y]
            if x >= 0 and y < N and temp not in visited and check(Map[i][j]-Map[x][y]):
                q.append(temp)
                visited.append(temp)
                result.append(temp)
                _sum += Map[x][y]
       
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
    country = []
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(N):
            country.append([temp[j], [i, j]])
        Map.append(temp)

    count = 0
    while True:
        #country = []
        visited = []
        flag = False
        for i in range(N):
            for j in range(N):
                if j != N-1 and Map[i][j] == Map[i][j+1]:
                    continue
                if [i, j] not in visited:
                    [val, temp] = bfs([i, j], visited)
                    if len(temp) > 1:
                        flag = True
                        country.append([val, temp])
        
        if not flag:
            break

        calculate(country)
        count += 1

    print(count)
