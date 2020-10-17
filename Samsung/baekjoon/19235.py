from collections import deque

def rotate(lst):
    return list(map(list, zip(*lst)))

def check(lst):
    flag = False
    blocks = [[-1, -1] for _ in range(4)]
    for i in range(len(lst)-2, -1, -1):
        if not flag:
            if False not in lst[i]:
                lst.pop(i)
        else:
            for j in range(4):
                if blocks[j] == [-1, -1]:
                    if lst[i][j]:
                        blocks[j] = [i, j]

    lst.appendleft([False, False, False, False])

    count = [[i+1, 1, 0] for i in range(4)]
    for i in range(len(lst)-2, -1, -1):
        for j in range(4):
            if lst[i][j] == False:
                if count[j][1] == 1:
                    count[j][1] = 2
                    count[j][2] += 1
                elif count[j][1] == 2:
                    count[j][2] += 1
            else:
                if count[j][1] == 1:




    return lst

def check2(lst):
    for i in range(2):
        if True in lst[1]:
            lst.pop(-2)
            lst.appendleft([False, False, False, False])
    return lst

if __name__ == "__main__":
    N = int(input())

    blue = deque([[False for _ in range(6)] for _ in range(4)])
    blue = rotate(blue)
    blue.append([True, True, True, True])
    blue = rotate(blue)
    green = deque([[False for _ in range(4)] for _ in range(6)])
    green.append([True, True, True, True])
    score = 0
    for i in range(N):
        t, x, y = map(int, input().split())

        if t == 1:
            for j in range(7):
                if blue[x][j]:
                    blue[x][j-1] = True
                    break
                    #
                    # flag = True
                    # for i in range(4):
                    #     if blue[i][j-1] == False:
                    #         flag = False
                    #         break
                    # if flag:
                    #     score += 1
                    #     blue = rotate(blue)
                    #     blue.pop(j-1)
                    #     blue = rotate(blue)
            for i in range(7):
                if green[i][y]:
                    green[i-1][y] = True
                    break
        elif t == 2:
            for j in range(7):
                if blue[x][j]:
                    blue[x][j-1] = True
                    blue[x][j-2] = True
                    break
            for i in range(7):
                if green[i][y] or green[i][y+1]:
                    green[i-1][y] = True
                    green[i-1][y+1] = True
                    break
        else:
            for j in range(7):
                if blue[x][j] or blue[x+1][j]:
                    blue[x][j-1] = True
                    blue[x+1][j-1] = True
                    break
            for i in range(7):
                if green[i][y]:
                    green[i-1][y] = True
                    green[i-2][y] = True
                    break

        blue = rotate(blue)
        blue = check(blue)
        blue = check2(blue)
        blue = rotate(blue)
        green = check(green)
        green = check2(green)

        for b in blue:
            print(b)
        for g in green:
            print(g)
        print()

    cnt = 0
    blue = rotate(blue)
    for i in range(6):
        for j in range(4):
            if blue[i][j]:
                cnt += 1
            if green[i][j]:
                cnt += 1
    print(score)
    print(cnt)