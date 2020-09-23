Map = []
DIRECTION = [[-1, -1], [-1, 1], [1, 1], [1, -1]]
result = -1
check = set()

def move(start, x, y, d, count, first):
    global result

    if start == [x, y] and not first:
        result = max(result, count)
    else:
        count += 1

        next_x = x + DIRECTION[d][0]
        next_y = y + DIRECTION[d][1]

        value = Map[next_x][next_y]
        if value > 0:
            if value not in check:
                check.add(value)

                move(start, next_x, next_y, d, count, False)

                check.remove(value)

        d += 1
        if d <= 3:
            next_x = x + DIRECTION[d][0]
            next_y = y + DIRECTION[d][1]

            value = Map[next_x][next_y]
            if value > 0:
                if value not in check:
                    check.add(value)

                    move(start, next_x, next_y, d, count, False)

                    check.remove(value)

if __name__ == "__main__":
    T = int(input())
    for c in range(T):
        N = int(input())
        Map.clear()
        Map.append([0 for _ in range(N+2)])
        for _ in range(N):
            temp = [0] + list(map(int, input().split())) + [0]
            Map.append(temp)
        Map.append([0 for _ in range(N+2)])

        N += 2
        result = -1
        for i in range(1, N-1):
            for j in range(1, N-1):
                start = [i, j]
                move(start, i, j, 0, 0, True)

        print("#%d %d"%(c+1, result))
