from collections import deque

def run(lst):
    global N
    for c in range(N):
        col = c+1
        row = 0
        while True:
            flag = False
            for r in range(row+1, H+1):
                if lst[r][col] == 1:
                    row = r
                    col += 1
                    flag = True
                    break
                if lst[r][col-1] == 1:
                    col = col-1
                    row = r
                    flag = True
                    break
            if not flag:
                break
        if col != c+1:
            return False
    return True

def dfs(cnt_i, cnt_j, count, fin):
    global Map, N, H

    if count == fin:
        if run(Map):
            print(fin)
            quit()
        else:
            return

    for i in range(cnt_i, H+1):
        for j in range(1, N):
            if Map[i][j] == 0 and Map[i][j-1] == 0 and Map[i][j+1] == 0:
                Map[i][j] = 1
                dfs(i, j, count+1, fin)
                Map[i][j] = 0
                
if __name__ == "__main__":
    N, M, H = map(int, input().split())

    Map = [[0 for _ in range(N+1)] for _ in range(H+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        Map[a][b] = 1

    for i in range(4):
        dfs(1, 1, 0, i)
    print('-1')
