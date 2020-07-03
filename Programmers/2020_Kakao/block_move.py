import queue
class block:
    def __init__(self, board):
        # If block is horizontal state, pos1 is left position and pos2 is right position.
        # If block is vertical state, pos1 is top position and pos2 is bottom position.
        self.pos1 = [0,0]
        self.pos2 = [0,1]

        self.board = board
        self.n = len(board)

        # 'h' : horizontal
        # 'v' : vertical
        self.state = 'h'

        self.count = 0

    def move_left(self, check):
        if self.state == 'h':
            if self.pos1[1] - 1 >= 0 and self.board[self.pos1[0]][self.pos1[1]-1] == 0:
                if not check:
                    self.pos2[1] -= 1
                    self.pos1[1] -= 1
                    self.count += 1
                return True
        elif self.state == 'v':
            if self.pos1[1] -1 >= 0 and self.board[self.pos1[0]][self.pos1[1]-1] == 0 and self.board[self.pos2[0]][self.pos2[1]-1] == 0:
                if not check:
                    self.pos1[1] -= 1
                    self.pos2[1] -= 1
                    self.count += 1
                return True
        
        return False

    def move_right(self, check):
        if self.state == 'h':
            if self.pos2[1] + 1 <= self.n-1 and self.board[self.pos2[0]][self.pos2[1]+1] == 0:
                if not check:
                    self.pos1[1] += 1
                    self.pos2[1] += 1
                    self.count += 1
                return True
        elif self.state == 'v':
            if self.pos1[1] + 1 >= self.n-1 and self.board[self.pos1[0]][self.pos1[1]+1] == 0 and self.board[self.pos2[0]][self.pos2[1]+1] == 0:
                if not check:
                    self.pos1[1] += 1
                    self.pos2[1] += 1
                    self.count += 1
                return True
        
        return False

    def move_up(self, check):
        if self.state == 'h':
            if self.pos1[0] - 1 >= 0 and self.board[self.pos1[0]-1][self.pos1[1]] == 0 and self.board[self.pos2[0]-1][self.pos2[1]] == 0:
                if not check:
                    self.pos1[0] -= 1
                    self.pos2[0] -= 1
                    self.count += 1
                return True
        elif self.state == 'v':
            if self.pos1[0] - 1 >= 0 and self.board[self.pos1[0]-1][self.pos1[1]] == 0:
                if not check:
                    self.pos1[0] -= 1
                    self.pos2[0] -= 1
                    self.count += 1
                return True
        
        return False

    def move_down(self, check):
        if self.state == 'h':
            if self.pos1[0] + 1 <= self.n-1 and self.board[self.pos1[0]+1][self.pos1[1]] == 0 and self.board[self.pos2[0]+1][self.pos2[1]] == 0:
                if not check:
                    self.pos1[0] += 1
                    self.pos2[0] += 1
                    self.count += 1
                return True
        elif self.state == 'v':
            if self.pos1[0] + 1 <= self.n-1 and self.board[self.pos1[0]+1][self.pos1[1]] == 0:
                if not check:
                    self.pos1[0] += 1
                    self.pos2[0] += 1
                    self.count += 1
                return True
        
        return False

    # 00    10  0: empty space.
    # 11 -> 10  1: block.
    def h_rotate_up1(self, check):
        if self.state == 'h':
            if self.pos1[0] - 1 >= 0 and self.board[self.pos1[0]-1][self.pos1[1]] == 0 and self.board[self.pos2[0]-1][self.pos2[1]] == 0:
                if not check:
                    self.state = 'v'
                    pos1[0] -= 1
                    pos2[1] -= 1
                    self.count += 1
                return True

        return False

    # 00    01  0: empty space.
    # 11 -> 01  1: block.
    def h_rotate_up2(self, check):
        if self.state == 'h':
            if self.pos1[0] - 1 >= 0 and self.board[self.pos1[0]-1][self.pos1[1]] == 0 and self.board[self.pos2[0]-1][self.pos2[1]] == 0:
                if not check:
                    self.state = 'v'
                    self.pos1[0] -= 1
                    self.pos1[1] += 1
                    self.count += 1
                return True

        return False

    # 11    10  0: empty space.
    # 00 -> 10  1: block.
    def h_rotate_down1(self, check):
        if self.state == 'h':
            if self.pos1[0] + 1 <= self.n-1 and self.board[self.pos1[0]+1][self.pos1[1]] == 0 and self.board[self.pos2[0]+1][self.pos2[1]] == 0:
                if not check:
                    self.state = 'v'
                    self.pos2[0] += 1
                    self.pos2[1] -= 1
                    self.count += 1
                return True

        return False

    # 11    01  0: empty space.
    # 00 -> 01  1: block.
    def h_rotate_down2(self, check):
        if self.state == 'h':
            if self.pos1[0] + 1 <= self.n-1 and self.board[self.pos1[0]+1][self.pos1[1]] == 0 and self.board[self.pos2[0]+1][self.pos2[1]] == 0:
                if not check:
                    self.state = 'v'
                    self.pos1[1] += 1
                    self.pos2[0] += 1
                    self.count += 1
                return True

        return False

    # 01    11  0: empty space.
    # 01 -> 00  1: block.
    def v_rotate_left1(self, check):
        if self.state == 'v':
            if self.pos1[1] - 1 >= 0 and self.board[self.pos1[0]][self.pos1[1]-1] == 0 and self.board[self.pos2[0]][self.pos2[1]-1] == 0:
                if not check:
                    self.state = 'h'
                    self.pos1[1] -= 1
                    self.pos2[0] -= 1
                    self.count += 1
                return True

        return False

    # 01    00  0: empty space.
    # 01 -> 11  1: block.
    def v_rotate_left2(self, check):
        if self.state == 'v':
            if self.pos1[1] - 1 >= 0 and self.board[self.pos1[0]][self.pos1[1]-1] == 0 and self.board[self.pos2[0]][self.pos2[1]-1] == 0:
                if not check:
                    self.state = 'h'
                    self.pos1[0] += 1
                    self.pos1[1] -= 1
                    self.count += 1
                return True

        return False

    # 10    11  0: empty space.
    # 10 -> 00  1: block.
    def v_rotate_right1(self, check):
        if self.state == 'v':
            if self.pos1[1] + 1 <= self.n-1 and self.board[self.pos1[0]][self.pos1[1]+1] == 0 and self.board[self.pos2[0]][self.pos2[1]+1] == 0:
                if not check:
                    self.state = 'h'
                    self.pos2[0] -= 1
                    self.pos2[1] += 1
                    self.count += 1
                return True

        return False

    # 10    00  0: empty space.
    # 10 -> 11  1: block.
    def v_rotate_right2(self, check):
        if self.state == 'v':
            if self.pos1[1] + 1 <= self.n-1 and self.board[self.pos1[0]][self.pos1[1]+1] == 0 and self.board[self.pos2[0]][self.pos2[1]+1] == 0:
                if not check:
                    self.state = 'h'
                    self.pos1[0] += 1
                    self.pos2[1] += 1
                    self.count += 1
                return True

        return False

    def check_move(self):
        if self.move_right(False):


def solution(board):
    answer = 0

    b = block(board)
    q = queue.Queue()

    while True:
        temp = []
        if b.move_right(False):
            temp.append(1)
        if b.move_left(False):
            temp.append(2)
        if b.move_up(False):
            temp.append(3)
        if b.move_down(False):
            temp.append(4)
        if b.h_rotate_down1(False):
            temp.append(5)
        if b.h_rotate_down2(False):
            temp.append(6)
        if b.h_rotate_up1(False):
            temp.append(7)
        if b.h_rotate_up2(False):
            temp.append(8)
        if b.v_rotate_left1(False):
            temp.append(9)
        if b.v_rotate_left2(False):
            temp.append(10)
        if b.v_rotate_right1(False):
            temp.append(11)
        if b.v_rotate_right2(False):
            temp.append(12)

        q.put(temp)
        
        


    print(b.h_rotate_down1(False))
    print(b.pos1, b.pos2, b.state)

    print(b.v_rotate_left1(False))
    print(b.pos1, b.pos2, b.state)

    return answer

if __name__ == "__main__":
    board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
    solution(board)