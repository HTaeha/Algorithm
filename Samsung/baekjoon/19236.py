from copy import deepcopy

DIRECTION = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

class shark(object):
    def __init__(self):
        global Map, fishes
        self.x = 1
        self.y = 1
        self.value = 100
        self.direction = Map[1][1].direction
        fishes.pop(Map[1][1].value-1)

    def eat(self, fish):
        global Map, fishes
        Map[self.x][self.y], Map[fish.x][fish.y] = Map[fish.x][fish.y], Map[self.x][self.y]
        Map[self.x][self.y] = 0
        self.x = fish.x
        self.y = fish.y
        self.direction = fish.direction
        for i, f in enumerate(fishes):
            if f.value == fish.value:
                fishes.pop(i)
                break

class fish(object):
    def __init__(self, x, y, value, d):
        self.x = x
        self.y = y
        self.value = value
        self.direction = d-1

    def rotate(self):
        if self.direction == 7:
            self.direction = 0
        else:
            self.direction += 1

    def change(self, fish2):
        global Map
        Map[self.x][self.y], Map[fish2.x][fish2.y] = Map[fish2.x][fish2.y], Map[self.x][self.y]
        self.x, fish2.x = fish2.x, self.x
        self.y, fish2.y = fish2.y, self.y

    def move(self, x, y):
        global Map
        Map[x][y], Map[self.x][self.y] = Map[self.x][self.y], Map[x][y]
        self.x = x
        self.y = y

    def run(self):
        global DIRECTION, Map

        while True:
            new_x = self.x + DIRECTION[self.direction][0]
            new_y = self.y + DIRECTION[self.direction][1]

            temp = Map[new_x][new_y]
            if temp == -1:
                self.rotate()
            elif temp == 0:
                self.move(new_x, new_y)
                break
            elif temp.value == 100:
                self.rotate()
            else:
                self.change(temp)
                break

def dfs(count, depth):
    global sk, Map, fishes, answer

    prev = deepcopy(Map)
    print_map()
    for fish in fishes:
        fish.run()

    x = sk.x
    y = sk.y
    flag = False
    while True:
        backup_sk = deepcopy(sk)
        x += DIRECTION[sk.direction][0]
        y += DIRECTION[sk.direction][1]

        temp = Map[x][y]
        print(depth, x, y, temp)
        if temp not in [0, -1]:
            flag = True
            backup = deepcopy(temp)
            sk.eat(temp)
            dfs(count+temp.value, depth+1)
            fishes.append(backup)
            fishes.sort(key=lambda x:x.value)
            Map = deepcopy(prev)
            Map[backup_sk.x][backup_sk.y] = backup_sk
            sk = backup_sk
            Map[backup.x][backup.y] = backup
        elif temp == -1:
            break

    if flag:
        answer = max(answer, count)

def print_map():
    for m in Map:
        for t in m:
            if t in [-1, 0]:
                print(t, end=" ")
            else:
                print("(%d %d)" % (t.value, t.direction), end=" ")
        print()
    print()

if __name__ == "__main__":
    Map = [[-1 for _ in range(6)]]
    fishes = []
    for i in range(4):
        temp = list(map(int, input().split()))
        temp_lst = [-1]
        for j in range(0, 8, 2):
            temp_fish = fish(i+1, j//2+1, temp[j], temp[j+1])
            temp_lst.append(temp_fish)
            fishes.append(temp_fish)
        temp_lst += [-1]
        Map.append(temp_lst)
    Map.append([-1 for _ in range(6)])

    fishes.sort(key=lambda x:x.value)

    for m in Map:
        for t in m:
            if t == -1:
                print(t, end=" ")
            else:
                print("(%d %d)"%(t.value, t.direction), end=" ")
        print()

    count = Map[1][1].value
    sk = shark()
    Map[1][1] = sk
    answer = 0
    dfs(count,1)
    '''
    while True:
        for fish in fishes:
            fish.run()
        for m in Map:
            for t in m:
                if t in [-1]:
                    print(t, end=" ")
                else:
                    print("(%d %d)" % (t.value, t.direction), end=" ")
            print()
        quit()
    '''
    print(answer)