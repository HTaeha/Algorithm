from collections import deque

DIRECTION = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def move():
    pass

def rotate():
    pass

def bfs(start):
    q = deque()

    q.append([start, 0])

    while q:
        pos, count = q.popleft()

        
    

def solution(board):
    answer = 0
    board = deque(board)

    for i in range(len(board)):
        board[i] = [1] + board[i] + [1]
    board.appendleft([1 for _ in range(len(board[0]))])
    board.append([1 for _ in range(len(board[0]))])

    answer = bfs([[1, 1], [1, 2]])

    return answer

if __name__ == "__main__":
    board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
    print(solution(board))
