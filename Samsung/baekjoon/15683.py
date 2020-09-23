from copy import deepcopy
from collections import deque

DIRECTION = [[-1, 0], [0, 1], [1, 0], [0, -1]]

class CCTV(object):
    def __init__(self, t, x, y):
        self.type = t
        self.d = 0
        self.x = x
        self.y = y

    def rotate(self):
        if self.d == 3:
            self.d = 0
        else:
            self.d += 1

if __name__ == "__main__":
    N, M = map(int, input().split())

    room = [[6 for _ in range(M+2)]]
    for i in range(N):
        temp = [6] + list(map(int, input().split())) + [6]
        room.append(temp)
    room.append([6 for _ in range(M+2)])

    N += 2
    M += 2

    cctv = []
    for i in range(N):
        for j in range(M):
            if room[i][j] > 0 and room[i][j] != 6:
                cctv.append(CCTV(room[i][j], i, j))
    
    print(cctv)
    q = deque()
    idx = 0
    q.append(deepcopy(cctv))
    while idx < len(cctv):
        arr = q.popleft()
        for i in arr:
            print(i.type, i.x, i.y, i.d)
        print()

        for _ in range(4):
            temp = deepcopy(cctv[idx])
            temp.rotate()
            arr[idx] = temp
            q.append(arr)

        idx += 1

    print(len(q))



    result = 0
    while True:
        pass
        
