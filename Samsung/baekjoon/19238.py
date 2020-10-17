from collections import deque

DIRECTION = [[-1, 0], [0, -1], [0, 1], [1, 0]]
def start(start):
    global fuel, DIRECTION, Map, first

    if tuple(start) in first:
        return [first[tuple(start)], 0, start]
    queue = deque()
    queue.append([start, 0])
    visited = set()
    visited.add(tuple(start))

    result = []
    while queue:
        [[x, y], count]= queue.popleft()

        for d in DIRECTION:
            new_x = x + d[0]
            new_y = y + d[1]

            value = Map[new_x][new_y]
            if value != 1 and (new_x, new_y) not in visited:
                if (new_x, new_y) in first:
                    visited.add((new_x, new_y))
                    result.append([first[(new_x, new_y)], count + 1, [new_x, new_y]])
                else:
                    visited.add((new_x, new_y))
                    queue.append([[new_x, new_y], count + 1])
        if fuel == count:
            if len(result) != 0:
                result.sort(key=lambda x: x[2][1])
                result.sort(key=lambda x: x[2][0])
                result.sort(key=lambda x: x[1])
                if result[0][1] <= fuel:
                    [_, _, [x, y]] = result[0]
                    Map[x][y] = 0
                    return result[0]
                else:
                    return [-1, -1, -1]
            else:
                return [-1, -1, -1]
    if len(result) != 0:
        result.sort(key=lambda x: x[2][1])
        result.sort(key=lambda x: x[2][0])
        result.sort(key=lambda x: x[1])
        if result[0][1] <= fuel:
            [_, _, [x, y]] = result[0]
            Map[x][y] = 0
            return result[0]
        else:
            return [-1, -1, -1]
    else:
        return [-1, -1, -1]

def finish(start, num):
    global fuel, DIRECTION, Map, second

    queue = deque()
    queue.append([start, 0])
    visited = set()
    visited.add(tuple(start))

    while queue:
        [[x, y], count]= queue.popleft()

        for d in DIRECTION:
            new_x = x + d[0]
            new_y = y + d[1]

            value = Map[new_x][new_y]
            if value != 1 and (new_x, new_y) not in visited:
                if second[n] == (new_x, new_y):
                    Map[new_x][new_y] = 0
                    return [count + 1, [new_x, new_y]]
                else:
                    visited.add((new_x, new_y))
                    queue.append([[new_x, new_y], count + 1])
        if fuel == count:
            return [-1, -1]
    return [-1, -1]


if __name__ == "__main__":
    N, M, fuel = map(int, input().split())

    Map = [[1 for _ in range(N+2)]]
    for i in range(N):
        temp = [1] + list(map(int, input().split())) + [1]
        Map.append(temp)
    Map.append([1 for _ in range(N+2)])

    car = list(map(int, input().split()))

    first = dict()
    second = dict()
    for i in range(M):
        temp = list(map(int, input().split()))
        first[(temp[0], temp[1])] = i
        second[i] = (temp[2], temp[3])

    pos = car
    for i in range(M):
        [n, cnt, pos] = start(pos)
        if n == -1:
            fuel = -1
            break
        fuel -= cnt
        first.pop(tuple(pos))

        [cnt, pos] = finish(pos, n)
        if cnt == -1:
            fuel = -1
            break
        fuel += cnt

    print(fuel)