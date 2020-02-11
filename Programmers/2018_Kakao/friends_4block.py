from collections import deque

def solution(m, n, board):
    numboard = [[0] * n for i in range(m)]
    for i in range(m) :
        for j in range(n) :
            numboard[i][j] = ord(board[i][j])
    answer = 0
    flag = True
    while flag :
        flag = False
        idx = []
        for i in range(m-1) :
            for j in range(n-1) :
                char = numboard[i][j]
                if char :
                    if numboard[i+1][j]==char and numboard[i][j+1] == char and numboard[i+1][j+1] == char :
                        flag = True
                        idx.append((i, j))
        for i in idx :
            x = i[0]
            y = i[1]
            numboard[x][y] = 0
            numboard[x+1][y] = 0
            numboard[x][y+1] = 0
            numboard[x+1][y+1] = 0
        for i in range(n) :
            block = deque()
            cnt = 0
            for j in range(m) :
                if numboard[j][i] :
                    block.append(numboard[j][i])
                    cnt += 1
            tmp = m-1
            while block :
                numboard[tmp][i] = block.pop()
                tmp -= 1
            for j in range(m - cnt) :
                numboard[j][i] = 0
    for i in numboard :
        answer += i.count(0)

    return answer

m, n = 6, 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
solution(m, n, board)