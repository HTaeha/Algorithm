from copy import deepcopy
from collections import deque

def combinations(lst,n):
    ret = []
    if n > len(lst): return ret
    
    if n == 1:
        for i in lst:
            ret.append([i])
    elif n>1:
        for i in range(len(lst)-n+1):
            for temp in combinations(lst[i+1:],n-1):
                ret.append([lst[i]]+temp)

    return ret

def bfs(lst, start):
    q = deque()
    q.append(start)

    while q:
        [i, j] = q.popleft()

        if lst[i-1][j] == 0:
            q.append([i-1, j])
            lst[i-1][j] = 1
        if lst[i+1][j] == 0:
            q.append([i+1, j])
            lst[i+1][j] = 1
        if lst[i][j-1] == 0:
            q.append([i, j-1])
            lst[i][j-1] = 1
        if lst[i][j+1] == 0:
            q.append([i, j+1])
            lst[i][j+1] = 1

if __name__ == "__main__":
    N, M = map(int, input().split())

    Map = [[1 for _ in range(M+2)]]
    indexes = []
    bugs = []
    for i in range(N):
        temp = [1] + list(map(int, input().split())) + [1]
        Map.append(temp)
        for j in range(len(temp)):
            if temp[j] == 0:
                indexes.append([i+1, j])
            elif temp[j] == 2:
                bugs.append([i+1, j])
    Map.append([1 for _ in range(M+2)])

    result = 0
    for c in combinations(indexes, 3):
        for idx in c:
            [i, j] = idx
            Map[i][j] = 1
            
        temp_map = deepcopy(Map)
        for b in bugs:
            bfs(temp_map, b)

        count = 0
        for i in range(len(temp_map)):
            for j in range(len(temp_map[0])):
                if temp_map[i][j] == 0:
                    count += 1
        result = max(result, count)

        for idx in c:
            [i, j] = idx
            Map[i][j] = 0

    print(result)
