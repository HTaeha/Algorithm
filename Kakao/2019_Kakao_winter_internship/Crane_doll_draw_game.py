# 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0

    stack = []
    machine = dict()
    
    for dolls in board:
        for i, doll in enumerate(dolls):
            if (i+1) not in machine:
                machine[i+1] = []
            if doll != 0:
                machine[i+1].append(doll)

    for m in moves:
        if len(machine[m]) == 0:
            continue
        else:
            doll = machine[m].pop(0)
            try:
                if stack[-1] == doll:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(doll)
            except IndexError:
                stack.append(doll)
        print(stack)
    print(machine)
    return answer

if __name__ == "__main__":
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves))
