from collections import deque

DIRECTION = [[-1, 0], [0, -1], [0, 1], [1, 0]]


def bfs(baby, water):
    queue = deque()

    first = True
    check = 2*len(water)
    temp = []
    count = 0
    visited = [[baby[0], baby[1]]]
    queue.append([baby[0], baby[1], count])
    while queue:
        [x, y, count] = queue.popleft()

        count += 1
        for d in DIRECTION:
            i = x + d[0]
            j = y + d[1]
            if [i, j] not in visited:
                if water[i][j] == -1:
                    continue
                elif water[i][j] == 0 or water[i][j] == baby[2]:
                    queue.append([i, j, count])
                    visited.append([i, j])
                elif water[i][j] < baby[2]:
                    if first:
                        first = False
                        check = count
                        temp.append([i, j])
                    else:
                        if check < count:
                            break
                        elif check == count:
                            temp.append([i, j])
                    queue.append([i, j, count])
                    visited.append([i, j])

    if len(temp) == 0:
        return 0

    temp = sorted(temp, key = lambda x:x[1])
    temp = sorted(temp, key = lambda x:x[0])
    [i, j] = temp[0]

    water[baby[0]][baby[1]] = 0
    baby[0] = i
    baby[1] = j
    baby[3] += 1
    if baby[2] == baby[3]:
        baby[2] += 1
        baby[3] = 0
    water[i][j] = 9

    return check


if __name__ == "__main__":
    N = int(input())

    water = [[-1 for _ in range(N + 2)]]
    for i in range(N):
        temp = [-1] + list(map(int, input().split())) + [-1]
        for j, t in enumerate(temp):
            if t == 9:
                baby = [i + 1, j, 2, 0]
        water.append(temp)
    water.append([-1 for _ in range(N + 2)])

    answer = 0
    while True:
        value = bfs(baby, water)
        if value == 0:
            break
        else:
            answer += value

    print(answer)
