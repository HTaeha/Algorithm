from copy import deepcopy

class Dice(object):
    def __init__(self, x, y, N, M, Map):
        self.num = [0,0,0,0,0,0]
        self.x = x
        self.y = y
        self.N = N
        self.M = M
        self.Map = Map

    def left(self):
        if self.validate(self.x, self.y-1):
            self.y -= 1
        else:
            return -1

        temp = deepcopy(self.num)
        self.num[0] = temp[5]
        self.num[2] = temp[4]
        self.num[4] = temp[0]
        self.num[5] = temp[2]

        if self.Map[self.x][self.y] == 0:
            self.Map[self.x][self.y] = self.num[2]
        else:
            self.set_num(self.Map[self.x][self.y])
            self.Map[self.x][self.y] = 0

        return self.num[0]

    def right(self):
        if self.validate(self.x, self.y+1):
            self.y += 1
        else:
            return -1

        temp = deepcopy(self.num)
        self.num[0] = temp[4]
        self.num[2] = temp[5]
        self.num[4] = temp[2]
        self.num[5] = temp[0]

        if self.Map[self.x][self.y] == 0:
            self.Map[self.x][self.y] = self.num[2]
        else:
            self.set_num(self.Map[self.x][self.y])
            self.Map[self.x][self.y] = 0

        return self.num[0]

    def up(self):
        if self.validate(self.x-1, self.y):
            self.x -= 1
        else:
            return -1

        temp = deepcopy(self.num)
        self.num[0] = temp[1]
        self.num[1] = temp[2]
        self.num[2] = temp[3]
        self.num[3] = temp[0]

        if self.Map[self.x][self.y] == 0:
            self.Map[self.x][self.y] = self.num[2]
        else:
            self.set_num(self.Map[self.x][self.y])
            self.Map[self.x][self.y] = 0

        return self.num[0]

    def down(self):
        if self.validate(self.x+1, self.y):
            self.x += 1
        else:
            return -1

        temp = deepcopy(self.num)
        self.num[0] = temp[3]
        self.num[1] = temp[0]
        self.num[2] = temp[1]
        self.num[3] = temp[2]

        if self.Map[self.x][self.y] == 0:
            self.Map[self.x][self.y] = self.num[2]
        else:
            self.set_num(self.Map[self.x][self.y])
            self.Map[self.x][self.y] = 0

        return self.num[0]

    def set_num(self, n):
        self.num[2] = n

    def validate(self, x, y):
        if x >= self.N or y >= self.M or x < 0 or y < 0:
            return False
        else:
            return True

if __name__ == "__main__":
    [N, M, x, y, K] = list(map(int, input().split()))

    Map = []
    for i in range(N):
        Map.append(list(map(int, input().split())))

    move = list(map(int, input().split()))

    dice = Dice(x, y, N, M, Map)
    for m in move:
        if m == 1:
            ret = dice.right()
        elif m == 2:
            ret = dice.left()
        elif m == 3:
            ret = dice.up()
        elif m == 4:
            ret = dice.down()
        if ret != -1:
            print(ret)

