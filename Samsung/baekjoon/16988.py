from itertools import combinations
from collections import deque

DIRECTION = [[-1, 0], [0, 1], [1, 0], [0, -1]]
def check(pos):
    global baduk

    for d in DIRECTION:
        x = pos[0] + d[0]
        y = pos[1] + d[1]
        if baduk[x][y] == 2:
            return True
    return False

def bfs(start):
    global baduk

    count = 1

    visited = [start]
    queue = deque()
    queue.append(start)
    while queue:
        pos = queue.popleft()
        
        for d in DIRECTION:
            x = pos[0] + d[0]
            y = pos[1] + d[1]
            if baduk[x][y] == 2 and [x, y] not in visited:
                count += 1
                queue.append([x, y])
                visited.append([x, y])
            elif baduk[x][y] == 0:
                return 0

    return count

def check_AI(start):
    global baduk, AI

    answer = [start]
    queue = deque()
    queue.append(start)
    while queue:
        pos = queue.popleft()
        
        for d in DIRECTION:
            x = pos[0] + d[0]
            y = pos[1] + d[1]
            if baduk[x][y] == 2 and [x, y] not in answer:
                queue.append([x, y])
                answer.append([x, y])
                AI.remove([x, y])

    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())

    baduk = [[-1 for _ in range(M+2)]]
    empty = []
    AI = []
    for i in range(N):
        temp = [-1] + list(map(int, input().split())) + [-1]
        for j, t in enumerate(temp):
            if t == 2:
                AI.append([i+1, j])
        baduk.append(temp)
    baduk.append([-1 for _ in range(M+2)])
    
    for i in range(len(baduk)):
        for j in range(len(baduk[0])):
            if baduk[i][j] == 0 and check([i, j]):
                empty.append([i, j])
    
    AI_dict = dict()
    cnt = 1
    for a in AI:
        AI_dict[cnt] = check_AI(a)
        cnt += 1

    answer = 0
    for c in combinations(empty, 2):
        visited = []
        for x, y in c:
            baduk[x][y] = 1
        temp = 0
        for k, v in AI_dict.items():
            temp += bfs(v[0])
        answer = max(answer, temp)
        for x, y in c:
            baduk[x][y] = 0

    print(answer)

