from itertools import combinations
from collections import deque

DIRECTION = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs(comb, length):
    global Map, DIRECTION, answer
    queue = deque()

    visited = set()
    for c in comb:
        queue.append(c+[0])
        visited.add(tuple(c))

    check = set()
    while queue:
        [x, y, count] = queue.popleft()

        if count >= answer:
            flag = False
            break
        flag = False
        for i, j in DIRECTION:
            new_x = x + i
            new_y = y + j
            value = Map[new_x][new_y]
            if value == 1 or (new_x, new_y) in visited:
                continue
            else:
                if value == 0:
                    check.add((new_x, new_y))
                    if len(check) == length:
                        flag = True
                        count += 1
                        break
                queue.append([new_x, new_y, count+1])
                visited.add((new_x, new_y))
        if flag:
            break

    return [flag, count]

if __name__ == "__main__":
    N, M = map(int, input().split())

    Map = [[1 for _ in range(N+2)]]
    virus = []
    empty = set()
    for i in range(N):
        temp = [1] + list(map(int, input().split())) + [1]
        for j in range(len(temp)):
            if temp[j] == 2:
                virus.append([i+1, j])
            elif temp[j] == 0:
                empty.add((i+1, j))
        Map.append(temp)
    Map.append([1 for _ in range(N+2)])

    if len(empty) == 0:
        answer = 0
    else:
        answer = 2505
        for c in combinations(virus, M):
            [flag, count] = bfs(c, len(empty))
            if flag:
                answer = min(answer, count)

        if answer == 2505:
            answer = -1

    print(answer)