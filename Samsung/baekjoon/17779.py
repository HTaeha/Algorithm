from collections import deque

DIRECTION = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs(x, y, start, d, direction):
    global DIRECTION

    queue = deque()
    count = 1
    queue.append(start + [count])

    visited = set((x, y))

    line = set((x, y))
    for i in range(d):
        new_x = x + 1
        new_y = y + direction
        line.add((new_x, new_y))
    limit_x = x
    limix_y = y
    while queue:
        [i, j, count] = queue.popleft()

        for d in DIRECTION:
            new_x = i + d[0]
            new_y = j + d[1]
            value = Map[new_x][new_y]
            if (new_x, new_y) in visited or (new_x, new_y) in line or new_x > limit_x or new_y > limix_y or value == 0:
                continue
            else:
                queue.append([new_x, new_y, count+1])
    return count

if __name__ == "__main__":
    N = int(input())

    Map = [[0 for _ in range(N+2)]]
    for i in range(N):
        temp = [0] + list(map(int, input().split())) + [0]
        Map.append(temp)
    Map.append([0 for _ in range(N+2)])

    humans = [0, 0, 0, 0, 0]

    for x in range(1, len(Map)-3):
        for y in range(2, len(Map)-2):
            for d1 in range(1, N):
                for d2 in range(1, N):
                    if x+d1+d2 > len(Map)-1 or y-d1 < 1 or y+d2 > len(Map)-2:
                        continue
                    print(x, y, d1, d2)
                    bfs(x, y, d1, d2)
    

