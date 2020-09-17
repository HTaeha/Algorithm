from copy import deepcopy
from collections import deque

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Marble_game(object):
    def __init__(self, R, B, arr, count, result):
        self.arr = arr
        self.R = R
        self.B = B
        self.count = count
        self.result = result

# direction : [-1, 0] - up
#             [0, 1] - right
#             [1, 0] - down
#             [0, -1] - left
def move(R, B, arr, direction):
    new_arr = deepcopy(arr)
    new_arr[R.x] = new_arr[R.x].replace('R', '.')
    new_arr[B.x] = new_arr[B.x].replace('B', '.')

    R = deepcopy(R)
    B = deepcopy(B)
    first_R = [R.x, R.y]
    first_B = [B.x, B.y]
    R_current_x = R.x
    R_current_y = R.y
    B_current_x = B.x
    B_current_y = B.y

    R_prev_x = R.x - direction[0]
    R_prev_y = R.y - direction[1]
    B_prev_x = B.x - direction[0]
    B_prev_y = B.y - direction[1]
    R_count = 0
    B_count = 0
    R_flag = False
    B_flag = False
    while True:
        R_next_x = R_current_x + direction[0]
        R_next_y = R_current_y + direction[1]
    #    print(R_next_x, R_next_y)
        next_item = new_arr[R_next_x][R_next_y]

        if next_item == '#':
            R.x = R_current_x
            R.y = R_current_y
            break
        elif next_item == 'O':
            R_flag = True
            break
        elif next_item == '.':
            R_prev_x = R_current_x
            R_prev_y = R_current_y

            R_current_x = R_next_x
            R_current_y = R_next_y

        R_count += 1
            
    while True:
        B_next_x = B_current_x + direction[0]
        B_next_y = B_current_y + direction[1]
        next_item = new_arr[B_next_x][B_next_y]

        if next_item == '#':
            B.x = B_current_x
            B.y = B_current_y
            break
        elif next_item == 'O':
            B_flag = True
            break
        elif next_item == '.':
            B_prev_x = B_current_x
            B_prev_y = B_current_y

            B_current_x = B_next_x
            B_current_y = B_next_y

        B_count += 1

    if B_flag:
        result = 0
    else:
        if R_flag:
            result = 1
        else:
            result = 2

    if R.x == B.x and R.y == B.y:
        if R_count < B_count:
            B.x = B_prev_x
            B.y = B_prev_y
        else:
            R.x = R_prev_x
            R.y = R_prev_y

    if result == 2:
        if first_R[0] == R.x and first_R[1] == R.y:
            if first_B[0] == B.x and first_B[1] == B.y:
                result = 0

    new_arr[R.x] = new_arr[R.x][:R.y] + 'R' + new_arr[R.x][R.y+1:]
    new_arr[B.x] = new_arr[B.x][:B.y] + 'B' + new_arr[B.x][B.y+1:]

    return [new_arr, R, B, result]

            
def bfs(arr, R, B):
    q = deque()

    arr[R.x] = arr[R.x].replace('R', '.')
    arr[B.x] = arr[B.x].replace('B', '.')

    # array, R, B, result, count
    # result - 0 : blue goal
    #          1 : blue not goal, red goal
    #          2 : red, blue goal
    q.append([arr, R, B, 2, 0])
    while True:
        temp = q.popleft()
        #'''
        print()
        for i in range(5):
            if i in [1, 2]:
                print(temp[i].x, temp[i].y)
            elif i == 0:
                for j in range(len(temp[i])):
                    print(temp[i][j])
            else:
                print(temp[i])
        #'''
        if temp[4] == 10:
            return -1

        if temp[3] == 0:
            continue
        elif temp[3] == 1:
            return temp[4]
        else:
            q.append(move(temp[1], temp[2], temp[0], [1, 0])+[temp[4]+1])
            q.append(move(temp[1], temp[2], temp[0], [-1, 0])+[temp[4]+1])
            q.append(move(temp[1], temp[2], temp[0], [0, 1])+[temp[4]+1])
            q.append(move(temp[1], temp[2], temp[0], [0, -1])+[temp[4]+1])

def find(arr, what):
    for i in range(len(arr)):
        if what in arr[i]:
            j = arr[i].index(what)
            return Point(i, j)

if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = []
    for i in range(n):
        arr.append(input())

    result = bfs(arr, find(arr, 'R'), find(arr, 'B'))

    print(result)

