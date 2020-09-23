class Point:
    def __init__(self):
        self.r = 0
        self.c = 0

def left(t_board, t_red, t_blue):
    if t_red.r == t_blue.r:
        row = t_red.r
        if row == goal.r:
            t_result = -1
        else:
            if t_red.c > t_blue.c:
                for c in range(t_blue.c-1, -1, -1):
                    if t_board[row][c] == '#':
                        t_board[row][c+1] = 'B'
                        t_blue.c = c+1
                        t_board[row][c+2] = 'R'
                        t_red.c = c+2
                        t_result = 0
                        break
            else:
                for c in range(t_red.c-1, -1, -1):
                    if t_board[row][c] == '#':
                        t_board[row][c+1] = 'R'
                        t_red.c = c+1
                        t_board[row][c+2] = 'B'
                        t_blue.c = c+2
                        t_result = 0
                        break
    else:
        if t_red.r == goal.r:
            t_result = 1
        elif t_blue.r == goal.r:
            t_result = -1
        else:
            t_result = 0
            for c in range(t_red.c-1, -1, -1):
                if t_board[t_red.r][c] == '#':
                    t_board[t_red.r][c+1] = 'R'
                    t_red.c = c+1
                    break
            for c in range(t_blue.c-1, -1, -1):
                if t_board[t_blue.r][c] == '#':
                    t_board[t_blue.r][c+1] = 'B'
                    t_blue.c = c+1
                    break

    return t_board, t_result, t_red, t_blue

def right(t_board, t_red, t_blue):
    if t_red.r == t_blue.r:
        row = t_red.r
        if row == goal.r:
            t_result = -1
        else:
            if t_red.c > t_blue.c:
                for c in range(t_red.c+1, len(t_board[0])):
                    if t_board[row][c] == '#':
                        t_board[row][c-1] = 'R'
                        t_red.c = c-1
                        t_board[row][c-2] = 'B'
                        t_blue.c = c-2
                        t_result = 0
                        break
            else:
                for c in range(t_blue.c+1, len(t_board[0])):
                    if t_board[row][c] == '#':
                        t_board[row][c-1] = 'B'
                        t_blue.c = c-1
                        t_board[row][c-2] = 'R'
                        t_red.c = c-2
                        t_result = 0
                        break
    else:
        if t_red.r == goal.r:
            t_result = 1
        elif t_blue.r == goal.r:
            t_result = -1
        else:
            t_result = 0
            for c in range(t_red.c+1, len(t_board[0])):
                if t_board[t_red.r][c] == '#':
                    t_board[t_red.r][c-1] = 'R'
                    t_red.c = c-1
                    break
            for c in range(t_blue.c+1, len(t_board[0])):
                if t_board[t_blue.r][c] == '#':
                    t_board[t_blue.r][c-1] = 'B'
                    t_blue.c = c-1
                    break

    return t_board, t_result, t_red, t_blue

def up(t_board, t_red, t_blue):
    if t_red.c == t_blue.c:
        col = t_red.c
        if col == goal.c:
            t_result = -1
        else:
            if t_red.r > t_blue.r:
                for r in range(t_blue.r-1, -1, -1):
                    if t_board[r][col] == '#':
                        t_board[r+1][col] = 'B'
                        t_blue.r = r+1
                        t_board[r+2][col] = 'R'
                        t_red.r = r+2
                        t_result = 0
                        break
            else:
                for r in range(t_red.r-1, -1, -1):
                    if t_board[r][col] == '#':
                        t_board[r+1][col] = 'R'
                        t_red.r = r+1
                        t_board[r+2][col] = 'B'
                        t_blue.r = r+2
                        t_result = 0
                        break
    else:
        if t_red.c == goal.c:
            t_result = 1
        elif t_blue.c == goal.c:
            t_result = -1
        else:
            t_result = 0
            for r in range(t_red.r-1, -1, -1):
                if t_board[r][t_red.c] == '#':
                    t_board[r+1][t_red.c] = 'R'
                    t_red.r = r+1
                    break
            for r in range(t_blue.r-1, -1, -1):
                if t_board[r][t_blue.c] == '#':
                    t_board[r+1][t_blue.c] = 'B'
                    t_blue.r = r+1
                    break

    return t_board, t_result, t_red, t_blue

def down(t_board, t_red, t_blue):
    if t_red.c == t_blue.c:
        col = t_red.c
        if col == goal.c:
            t_result = -1
        else:
            if t_red.r > t_blue.r:
                for r in range(t_red.r+1, len(t_board)):
                    if t_board[r][col] == '#':
                        t_board[r-1][col] = 'R'
                        t_red.r = r-1
                        t_board[r-2][col] = 'B'
                        t_blue.r = r-2
                        t_result = 0
                        break
            else:
                for r in range(t_blue.r+1, len(t_board)):
                    if t_board[r][col] == '#':
                        t_board[r-1][col] = 'B'
                        t_blue.r = r-1
                        t_board[r-2][col] = 'R'
                        t_red.r = r-2
                        t_result = 0
                        break
    else:
        if t_red.c == goal.c:
            t_result = 1
        elif t_blue.c == goal.c:
            t_result = -1
        else:
            t_result = 0
            for r in range(t_red.r+1, len(t_board)):
                if t_board[r][t_red.c] == '#':
                    t_board[r-1][t_red.c] = 'R'
                    t_red.r = r-1
                    break
            for r in range(t_blue.r+1, len(t_board)):
                if t_board[r][t_blue.c] == '#':
                    t_board[r-1][t_blue.c] = 'B'
                    t_blue.r = r-1
                    break

    return t_board, t_result, t_red, t_blue

def dfs(depth, t_board, t_red, t_blue):
    global result

    print(depth)

    if depth == 10:
        return -1

    for i in range(4):
        if i == 0:
            t_board, t_result, t_red, t_blue = left(t_board, t_red, t_blue)
        elif i == 1:
            t_board, t_result, t_red, t_blue = right(t_board, t_red, t_blue)
        elif i == 2:
            t_board, t_result, t_red, t_blue = up(t_board, t_red, t_blue)
        else:
            t_board, t_result, t_red, t_blue = down(t_board, t_red, t_blue)

        if t_result == -1:
            pass
        elif t_result == 1:
            result = min(result, depth)
        else:
            dfs(depth+1, t_board)

if __name__ == "__main__":
    n, m = list(map(int, input().split(" ")))

    board = []
    result = -1

    for i in range(n):
        board.append(input())

    red = Point()
    blue = Point()
    goal = Point()

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                red.r = i
                red.c = j
            elif board[i][j] == 'B':
                blue.r = i
                blue.c = j
            elif board[i][j] == 'O':
                goal.r = i
                goal.c = j

    dfs(0, board, red, blue)
    
    print(result)