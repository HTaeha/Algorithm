# 프렌즈4블록
# https://programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    answer = 0

    board = [list(s) for s in board]

    while True:
        flag = False
        temp = [[0 for _ in range(n)] for _ in range(m)]
        # 4가지 같은 블록이 있을 경우 temp list에 1로 표시.
        # 같은 블록이 발견되지 않을 경우 flag가 True가 되고 종료.
        for i in range(0, m-1):
            for j in range(0, n-1):
                check = board[i][j]
                if check == 0:
                    continue

                if check == board[i+1][j] and check == board[i][j+1] and check == board[i+1][j+1]:
                    temp[i][j] = 1
                    temp[i+1][j] = 1
                    temp[i][j+1] = 1
                    temp[i+1][j+1] = 1
                    flag = True

        # 더 이상 지워질 블록이 없음.
        if not flag:
            break

        # board와 temp 2차원 배열을 시계방향으로 90도 회전.
        rotate_board = list(map(list,zip(*board[::-1])))
        rotate_temp = list(map(list,zip(*temp[::-1])))
        # temp 에서 1인 블록을 제거하고 뒤에 0을 넣어준다. 
        for i, l in enumerate(rotate_temp):
            while True:
                try:
                    empty_idx = l.index(1)
                except ValueError:
                    break
                l.pop(empty_idx)
                l.append(0)
                rotate_board[i].pop(empty_idx)
                rotate_board[i].append(0)
                answer += 1

        # 시계 반대 방향으로 90도 돌려서 원위치.
        board = list(map(list,zip(*rotate_board)))[::-1]

    return answer

if __name__ == "__main__":
    m = 6
    n = 6
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
    board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
    print(solution(m, n, board))
