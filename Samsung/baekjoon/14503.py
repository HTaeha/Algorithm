import time

DIRECTION = [[-1, 0], [0, 1], [1, 0], [0, -1]]

class Robot(object):
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.count = 0

    def rotate(self):
        if self.d == 0:
            self.d = 3
        else:
            self.d -= 1

    def next(self):
        x = self.x + DIRECTION[self.d][0]
        y = self.y + DIRECTION[self.d][1]
        return [x, y]

    def forward(self):
        self.x += DIRECTION[self.d][0]
        self.y += DIRECTION[self.d][1]

    def backward(self):
        self.x -= DIRECTION[self.d][0]
        self.y -= DIRECTION[self.d][1]

def check(lst, x, y, d):
    count = 0
    if lst[x-1][y] == 1 or lst[x-1][y] == 2:
        count += 1
    if lst[x+1][y] == 1 or lst[x+1][y] == 2:
        count += 1
    if lst[x][y-1] == 1 or lst[x][y-1] == 2:
        count += 1
    if lst[x][y+1] == 1 or lst[x][y+1] == 2:
        count += 1

    flag = False
    if lst[x-DIRECTION[d][0]][y-DIRECTION[d][1]] == 1:
        flag = True

    if count == 4:
        if flag:
            return 0
        else:
            return 1
    else:
        return 2

if __name__ == "__main__":
    N, M = map(int, input().split())
    x, y, d = map(int, input().split())

    Map = [[1 for _ in range(M+2)]]
    for i in range(N):
        temp = [1] + list(map(int, input().split())) + [1]
        Map.append(temp)
    Map.append([1 for _ in range(M+2)])

    x += 1
    y += 1
    robot = Robot(x, y, d)
    Map[x][y] = 2
    robot.count += 1
    while True:
        ret = check(Map, robot.x, robot.y, robot.d)
        if ret == 0:
            break
        elif ret == 1:
            robot.backward()
        else:
            robot.rotate()
            [i, j] = robot.next()
            if Map[i][j] == 0:
                robot.forward()
                Map[i][j] = 2
                robot.count += 1

    print(robot.count)
