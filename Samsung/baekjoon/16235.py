from collections import OrderedDict

DIRECTION = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def spring():
    global age, energy

    dead = dict()
    new = dict()
    for (x, y), d in age.items():
        for z, num in d.items():
            if energy[x][y] < z*num:
                save = energy[x][y]//z
                die = num - save

                energy[x][y] -= z*save
                if save != 0:
                    if (x, y) not in new:
                        new[(x, y)] = OrderedDict()
                    new[(x, y)][z+1] = save

                dead[(x, y, z)] = die
            else:
                energy[x][y] -= z*num
                if (x, y) not in new:
                    new[(x, y)] = OrderedDict()
                new[(x, y)][z + 1] = num

    age = new

    return dead

def summer(dead):
    global energy

    for (x, y, z), value in dead.items():
        energy[x][y] += (z//2)*value

def fall(age):
    global energy, DIRECTION

    new = []
    for (x, y), d in age.items():
        for z, num in d.items():
            if z%5 == 0:
                for dir in DIRECTION:
                    new_x = x + dir[0]
                    new_y = y + dir[1]
                    if energy[new_x][new_y] != -1:
                        new.append((new_x, new_y, num))

    for (new_x, new_y, num) in new:
        if (new_x, new_y) in age:
            if 1 in age[(new_x, new_y)]:
                age[(new_x, new_y)][1] += num
            else:
                age[(new_x, new_y)][1] = num
                age[(new_x, new_y)].move_to_end(1, last=False)
        else:
            age[(new_x, new_y)] = OrderedDict()
            age[(new_x, new_y)][1] = num

def winter(add):
    global energy

    for i in range(1, N+1):
        for j in range(1, N+1):
            energy[i][j] += add[i][j]

if __name__ == "__main__":
    N, M, K = map(int, input().split())

    add = [[-1 for _ in range(N+2)]]
    for i in range(N):
        temp = [-1] + list(map(int, input().split())) + [-1]
        add.append(temp)
    add.append([-1 for _ in range(N+2)])

    age = dict()
    for i in range(M):
        x, y, z = map(int, input().split())
        age[(x, y)] = OrderedDict()
        age[(x, y)][z] = 1

    energy = [[-1 for _ in range(N+2)]]
    for i in range(N):
        temp = [-1] + [5 for _ in range(N)] + [-1]
        energy.append(temp)
    energy.append([-1 for _ in range(N+2)])

    for i in range(K):
        dead = spring()
        summer(dead)
        fall(age)
        winter(add)

    answer = 0
    for k, v in age.items():
        for a, value in v.items():
            answer += value

    print(answer)