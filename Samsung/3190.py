class snake(object):
    def __init__(self, board):
        self.body = [[0, 0]]
        self.DIRECTION = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.direction = 1
        self.board = board
        self.count = 0
        self.board[0][0] = -1

    def rotate(self, C):
        if C == 'L':
            if self.direction == 0:
                self.direction = 3
            else:
                self.direction -= 1
        elif C == 'D':
            if self.direction == 3:
                self.direction = 0
            else:
                self.direction += 1

    def move(self):
        head = self.body[-1]
        next_pos = [head[0] + self.DIRECTION[self.direction][0], head[1] + self.DIRECTION[self.direction][1]]
        if self.is_terminate(next_pos[0], next_pos[1]):
            self.count += 1
            return self.count
        else:
            next_val = self.board[next_pos[0]][next_pos[1]] 
            if next_val == 0:
                self.body.append(next_pos)
                self.board[next_pos[0]][next_pos[1]] = -1
                temp = self.body.pop(0)
                self.board[temp[0]][temp[1]] = 0
            elif next_val == 1:
                self.body.append(next_pos)
                self.board[next_pos[0]][next_pos[1]] = -1
                
            self.count += 1

            return -1

    def is_terminate(self, i, j):
        if i >= len(self.board) or j >= len(self.board):
            return True
        elif i < 0 or j < 0:
            return True
        elif self.board[i][j] == -1:
            return True
        else:
            return False

if __name__ == "__main__":
    N = int(input())
    K = int(input())

    board = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        [i, j] = list(map(int, input().split()))
        board[i-1][j-1] = 1

    L = int(input())
    info = []
    for i in range(L):
        [X, C] = list(input().split())
        info.append([int(X), C])

    s = snake(board)
    while True:
        ret = s.move()

        if len(info) != 0:
            if s.count == info[0][0]:
                s.rotate(info[0][1])
                info.pop(0)
        if ret != -1:
            break
        
    print(s.count)
