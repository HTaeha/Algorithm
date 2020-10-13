DIRECTION = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def calculate(x, y, d, direction, area):
    global Map

    count = 0
    line = set()
    line.add((x, y))
    new_x = x
    new_y = y
    for i in range(d):
        new_x += 1
        new_y += direction
        line.add((new_x, new_y))

    if area == 1:
        limit_x = x + d
        limit_y = y
        for i in range(1, limit_x):
            for j in range(1, limit_y+1):
                if (i, j) in line:
                    break
                count += Map[i][j]
    elif area == 2:
        limit_x = x + d
        limit_y = y
        for i in range(limit_x, 0, -1):
            for j in range(len(Map[0])-2, y, -1):
                if (i, j) in line:
                    break
                count += Map[i][j]
    elif area == 3:
        limit_x = x
        limit_y = y + d
        for i in range(x, len(Map)-1):
            for j in range(1, limit_y):
                if (i, j) in line:
                    break
                count += Map[i][j]
    elif area == 4:
        limit_x = x
        limit_y = y - d
        for i in range(len(Map)-2, x, -1):
            for j in range(len(Map[0])-2, limit_y-1, -1):
                if (i, j) in line:
                    break
                count += Map[i][j]

    return count

def five_area(x, y, d1, d2):
    global Map

    boundary = set()
    boundary.add((x, y))
    new_x = x
    new_y = y
    new_x2 = x + d2
    new_y2 = y + d2
    for i in range(d1):
        new_x += 1
        new_y -= 1
        boundary.add((new_x, new_y))
        new_x2 += 1
        new_y2 -= 1
        boundary.add((new_x2, new_y2))

    new_x = x
    new_y = y
    new_x2 = x + d1
    new_y2 = y - d1
    for i in range(d2):
        new_x += 1
        new_y += 1
        boundary.add((new_x, new_y))
        new_x2 += 1
        new_y2 += 1
        boundary.add((new_x2, new_y2))

    count = Map[x][y]
    count += Map[x+d1+d2][y+d2-d1]
    for i in range(x+1, x+d1+d2):
        start = False
        for j in range(y-d1, y+d2+1):
            if start:
                count += Map[i][j]
                if (i, j) in boundary:
                    break
            else:
                if (i, j) in boundary:
                    start = True
                    count += Map[i][j]

    return count

if __name__ == "__main__":
    N = int(input())

    Map = [[0 for _ in range(N+2)]]
    for i in range(N):
        temp = [0] + list(map(int, input().split())) + [0]
        Map.append(temp)
    Map.append([0 for _ in range(N+2)])

    humans = [0, 0, 0, 0, 0]

    answer = 40000
    for x in range(1, len(Map)-3):
        for y in range(2, len(Map)-2):
            for d1 in range(1, N):
                for d2 in range(1, N):
                    if x+d1+d2 > len(Map)-1 or y-d1 < 1 or y+d2 > len(Map)-2:
                        continue
                    temp = []
                    temp.append(calculate(x, y, d1, -1, 1))
                    temp.append(calculate(x, y, d2, 1, 2))
                    standard = [x+d1, y-d1]
                    temp.append(calculate(standard[0], standard[1], d2, 1, 3))
                    standard = [x+d2, y+d2]
                    temp.append(calculate(standard[0], standard[1], d1, -1, 4))
                    temp.append(five_area(x, y, d1, d2))
                    temp.sort()

                    answer = min(answer, temp[-1] - temp[0])
    
    print(answer)

