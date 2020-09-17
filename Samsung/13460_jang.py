from collections import deque
import sys

direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def move(cur, d) :
    cur_x, cur_y = cur
    dist = 0
    while True :
        next_x, next_y = cur_x + direction[d][0], cur_y + direction[d][1]
        if board[next_x][next_y] == "#" :
            return [cur_x, cur_y], dist
        elif board[next_x][next_y] == "O" :
            dist += 1
            return [next_x, next_y], dist
        elif board[next_x][next_y] == '.'  or board[next_x][next_y] == "B" or board[next_x][next_y] == "R":
            dist += 1
            cur_x, cur_y = next_x, next_y
    
if __name__ == "__main__" :
    N, M = map(int, input().split())
    board = []

    for _ in range(N) :
        str_ = input()
        temp = []
        for i in str_ :
            temp.append(i)
        board.append(temp)

    for idx_i, i in enumerate(board) :
        for idx_j, j in enumerate(i) :
            if j == "R" :
                r = [idx_i, idx_j]
            elif j == "B" :
                b = [idx_i, idx_j]
            elif j == 'O' :
                hall = [idx_i, idx_j]

    q = deque()
    q.append((r, b, 0))

    while q :
        cur_r, cur_b, cnt = q.popleft()
        if cnt == 10 :
            print(-1)
            sys.exit()

        for d in range(4) :
            next_r, dist_r = move(cur_r, d)
            next_b, dist_b = move(cur_b, d)
            if next_r != next_b :
                if cur_r == next_r and cur_b == next_b :
                    continue
                if next_r == hall :
                    print(cnt+1)
                    sys.exit()
                elif next_b == hall :
                    continue
                else :
                    q.append((next_r, next_b, cnt+1))
            else :
                if next_r == hall :
                    continue
                else :
                    if dist_r < dist_b :
                        next_b[0] -= direction[d][0]
                        next_b[1] -= direction[d][1]
                    else :
                        next_r[0] -= direction[d][0]
                        next_r[1] -= direction[d][1]
                    q.append((next_r, next_b, cnt+1))
