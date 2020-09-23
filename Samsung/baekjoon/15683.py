from copy import deepcopy
from collections import deque

room = []
cctv = []
DIRECTION = [[-1, 0], [0, 1], [1, 0], [0, -1]]
result = 0

class CCTV(object):
    def __init__(self, t, x, y):
        self.type = t
        self.d = 0
        self.x = x
        self.y = y

    def rotate(self):
        self.d = (self.d+1)%4

    def back(self, check):
        for x, y in check:
            room[x][y] = 0

    def fill(self):
        check = []

        count = 0
        if self.type == 1:
            x = self.x
            y = self.y
            while True:
                next_x = x + DIRECTION[self.d][0]
                next_y = y + DIRECTION[self.d][1]

                value = room[next_x][next_y]
                if value == 6:
                    break
                elif value == 0:
                    x = next_x
                    y = next_y
                    room[next_x][next_y] = -1
                    check.append([x, y])
                    count += 1
                else:
                    x = next_x
                    y = next_y
        elif self.type == 2:
            x = self.x
            y = self.y
            while True:
                next_x = x + DIRECTION[self.d][0]
                next_y = y + DIRECTION[self.d][1]

                value = room[next_x][next_y]
                if value == 6:
                    break
                elif value == 0:
                    x = next_x
                    y = next_y
                    room[next_x][next_y] = -1
                    check.append([x, y])
                    count += 1
                else:
                    x = next_x
                    y = next_y
            x = self.x
            y = self.y
            while True:
                next_x = x - DIRECTION[self.d][0]
                next_y = y - DIRECTION[self.d][1]

                value = room[next_x][next_y]
                if value == 6:
                    break
                elif value == 0:
                    x = next_x
                    y = next_y
                    room[next_x][next_y] = -1
                    check.append([x, y])
                    count += 1
                else:
                    x = next_x
                    y = next_y
        elif self.type == 3:
            x = self.x
            y = self.y
            while True:
                next_x = x + DIRECTION[self.d][0]
                next_y = y + DIRECTION[self.d][1]

                value = room[next_x][next_y]
                if value == 6:
                    break
                elif value == 0:
                    x = next_x
                    y = next_y
                    room[next_x][next_y] = -1
                    check.append([x, y])
                    count += 1
                else:
                    x = next_x
                    y = next_y
            x = self.x
            y = self.y
            while True:
                next_x = x + DIRECTION[(self.d+1)%4][0]
                next_y = y + DIRECTION[(self.d+1)%4][1]

                value = room[next_x][next_y]
                if value == 6:
                    break
                elif value == 0:
                    x = next_x
                    y = next_y
                    room[next_x][next_y] = -1
                    check.append([x, y])
                    count += 1
                else:
                    x = next_x
                    y = next_y

        elif self.type == 4:
            x = self.x
            y = self.y
            while True:
                next_x = x + DIRECTION[self.d][0]
                next_y = y + DIRECTION[self.d][1]

                value = room[next_x][next_y]
                if value == 6:
                    break
                elif value == 0:
                    x = next_x
                    y = next_y
                    room[next_x][next_y] = -1
                    check.append([x, y])
                    count += 1
                else:
                    x = next_x
                    y = next_y
            x = self.x
            y = self.y
            while True:
                next_x = x + DIRECTION[(self.d+1)%4][0]
                next_y = y + DIRECTION[(self.d+1)%4][1]

                value = room[next_x][next_y]
                if value == 6:
                    break
                elif value == 0:
                    x = next_x
                    y = next_y
                    room[next_x][next_y] = -1
                    check.append([x, y])
                    count += 1
                else:
                    x = next_x
                    y = next_y
            x = self.x
            y = self.y
            while True:
                next_x = x + DIRECTION[(self.d+2)%4][0]
                next_y = y + DIRECTION[(self.d+2)%4][1]

                value = room[next_x][next_y]
                if value == 6:
                    break
                elif value == 0:
                    x = next_x
                    y = next_y
                    room[next_x][next_y] = -1
                    check.append([x, y])
                    count += 1
                else:
                    x = next_x
                    y = next_y

        elif self.type == 5:
            x = self.x
            y = self.y
            while True:
                next_x = x + DIRECTION[self.d][0]
                next_y = y + DIRECTION[self.d][1]

                value = room[next_x][next_y]
                if value == 6:
                    break
                elif value == 0:
                    x = next_x
                    y = next_y
                    room[next_x][next_y] = -1
                    check.append([x, y])
                    count += 1
                else:
                    x = next_x
                    y = next_y
            x = self.x
            y = self.y
            while True:
                next_x = x + DIRECTION[(self.d+1)%4][0]
                next_y = y + DIRECTION[(self.d+1)%4][1]

                value = room[next_x][next_y]
                if value == 6:
                    break
                elif value == 0:
                    x = next_x
                    y = next_y
                    room[next_x][next_y] = -1
                    check.append([x, y])
                    count += 1
                else:
                    x = next_x
                    y = next_y
            x = self.x
            y = self.y
            while True:
                next_x = x + DIRECTION[(self.d+2)%4][0]
                next_y = y + DIRECTION[(self.d+2)%4][1]

                value = room[next_x][next_y]
                if value == 6:
                    break
                elif value == 0:
                    x = next_x
                    y = next_y
                    room[next_x][next_y] = -1
                    check.append([x, y])
                    count += 1
                else:
                    x = next_x
                    y = next_y
            x = self.x
            y = self.y
            while True:
                next_x = x + DIRECTION[(self.d+3)%4][0]
                next_y = y + DIRECTION[(self.d+3)%4][1]

                value = room[next_x][next_y]
                if value == 6:
                    break
                elif value == 0:
                    x = next_x
                    y = next_y
                    room[next_x][next_y] = -1
                    check.append([x, y])
                    count += 1
                else:
                    x = next_x
                    y = next_y

        return [count, check]

def dfs(index, count):
    global result

    if index == len(cctv):
        result = max(result, count)
    else:
        if cctv[index].type in [1, 3, 4]:
            for _ in range(4):
                [ret, check] = cctv[index].fill()
                dfs(index+1, count+ret)
                cctv[index].back(check)
                cctv[index].rotate()
        elif cctv[index].type == 2:
            for _ in range(2):
                [ret, check] = cctv[index].fill()
                dfs(index+1, count+ret)
                cctv[index].back(check)
                cctv[index].rotate()
        elif cctv[index].type == 5:
            [ret, check] = cctv[index].fill()
            dfs(index+1, count+ret)
            cctv[index].back(check)
        
if __name__ == "__main__":
    N, M = map(int, input().split())

    room.append([6 for _ in range(M+2)])
    for i in range(N):
        temp = [6] + list(map(int, input().split())) + [6]
        room.append(temp)
    room.append([6 for _ in range(M+2)])

    N += 2
    M += 2

    zero_count = 0
    for i in range(N):
        for j in range(M):
            if room[i][j] > 0 and room[i][j] != 6:
                cctv.append(CCTV(room[i][j], i, j))
            elif room[i][j] == 0:
                zero_count += 1
    
    dfs(0, 0)

    print(zero_count - result)

