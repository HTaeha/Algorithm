DIRECTION = [[], [-1, 0], [1, 0], [0, -1], [0, 1]]

class shark(object):
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.value = v
        self.d = -1
        self.order = []

    def move(self):
        global Map, DIRECTION, k

        flag = False
        for o in self.order[self.d]:
            x = self.x + DIRECTION[o][0]
            y = self.y + DIRECTION[o][1]

            if x < 0 or x >= len(Map) or y < 0 or y >= len(Map[0]):
                continue
            val = Map[x][y]
            if val == 0:
                self.x = x
                self.y = y
                self.d = o
                flag = True
                break
        if not flag:
            for o in self.order[self.d]:
                x = self.x + DIRECTION[o][0]
                y = self.y + DIRECTION[o][1]

                if x < 0 or x >= len(Map) or y < 0 or y >= len(Map[0]):
                    continue
                val = Map[x][y]
                if val[0] == self.value:
                    self.x = x
                    self.y = y
                    self.d = o
                    break

def remove():
    global sharks, k

    dictionary = dict()
    remove_lst = []
    for i, s in enumerate(sharks):
        if (s.x, s.y) not in dictionary:
            dictionary[(s.x, s.y)] = s.value
            Map[s.x][s.y] = [s.value, k]
        else:
            remove_lst.append(i)

    for idx in range(len(remove_lst)-1, -1, -1):
        sharks.pop(remove_lst[idx])

def smell():
    global Map, sharks, k

    for i in range(len(Map)):
        for j in range(len(Map[0])):
            if Map[i][j] != 0:
                val = Map[i][j]
                if val[1]-1 == 0:
                    Map[i][j] = 0
                else:
                    Map[i][j] = [val[0], val[1]-1]

    for s in sharks:
        Map[s.x][s.y] = [s.value, k]

if __name__ == "__main__":
    N, M, k = map(int, input().split())

    Map = []
    sharks = []
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(len(temp)):
            if temp[j] != 0:
                s = shark(i, j, temp[j])
                sharks.append(s)
                temp[j] = [temp[j], k]
        Map.append(temp)

    d = list(map(int, input().split()))

    sharks.sort(key = lambda x:x.value)
    for i in range(len(sharks)):
        order = [[]]
        sharks[i].d = d[i]
        for j in range(4):
            temp = list(map(int, input().split()))
            order.append(temp)
        sharks[i].order = order

    count = 0
    test = 0
    while True:
        test += 1
        for s in sharks:
            s.move()
        remove()
        smell()
        count += 1
        if count > 1000:
            count = -1
            break
        if len(sharks) == 1:
            break
    print(count)