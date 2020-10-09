DIRECTION = [[-1, 0], [1, 0], [0, 1], [0, -1]]

class Cleaner(object):
    def __init__(self):
        self.pos = []

    def run(self):
        global Map

        up = self.pos[0]
        down = self.pos[1]
        for i in range(up[0]-2, 0, -1):
            Map[i+1][1] = Map[i][1]
        for i in range(2, len(Map[0])-1):
            Map[1][i-1] = Map[1][i]
        for i in range(2, up[0]+1):
            Map[i-1][len(Map[0])-2] = Map[i][len(Map[0])-2]
        for i in range(len(Map[0])-3, 1, -1):
            Map[up[0]][i+1] = Map[up[0]][i]
        Map[up[0]][2] = 0

        for i in range(down[0]+2, len(Map)-1):
            Map[i-1][1] = Map[i][1]
        Map[-2].pop(1)
        Map[-2].append(-2)
        Map[-2][-2] = Map[-3][-2]
        for i in range(len(Map)-3, down[0]-1, -1):
            Map[i+1][-2] = Map[i][-2]
        Map[down[0]].pop(-2)
        Map[down[0]].insert(2, 0)

def spread(pos, Map):
    global DIRECTION

    count = 0
    for d in DIRECTION:
        x = pos[0] + d[0]
        y = pos[1] + d[1]
        if Map[x][y] >= 0:
            count += 1
            Map[x][y] += pos[2]//5
    value = pos[2]//5 * count
    Map[pos[0]][pos[1]] -= value

if __name__ == "__main__":
    R, C, T = map(int, input().split())

    Map = [[-2 for _ in range(C+2)]]
    dust = []
    cleaner = Cleaner()
    for i in range(R):
        temp = [-2] + list(map(int, input().split())) + [-2]
        for j in range(len(temp)):
            if temp[j] == -1:
                cleaner.pos.append([i+1, j])
            elif temp[j] > 0:
                dust.append([i+1, j])
        Map.append(temp)
    Map.append([-2 for _ in range(C+2)])

    while T:
        T -= 1

        temp = []
        for i in range(1, len(Map)-1):
            for j in range(1, len(Map[0])-1):
                if Map[i][j] > 0:
                    temp.append([i, j, Map[i][j]])

        for t in temp:
            spread(t, Map)

        cleaner.run()

    answer = 0
    for i in range(1, R+1):
        for j in range(1, C+1):
            if Map[i][j] > 0:
                answer += Map[i][j]

    print(answer)
