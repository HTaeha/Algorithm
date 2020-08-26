#https://www.acmicpc.net/problem/17825
def play():
    print(yut)

def dfs(depth):
    if depth == 10:
        play()
        return
    for i in range(4):
        yut[depth] = i
        dfs(depth+1)

if __name__ == "__main__":
    input_sample = [1,2,3,4,5,1,2,3,4,5]
    #move = list(map(int, input().split(" ")))
    move = input_sample

    score = [2, 4, 6, 8, 10, 13, 16, 19, 12, 14, 16, 18, 20, 22, 24, 22, 24, 26, 28, 30, 28, 27, 26, 25, 32, 34, 36, 38, 30, 35, 40]
    yut = [0 for i in range(10)]

    result = 0
    print(len(score))

    dfs(0)
    while True:
    #    yut[0~3] += move[0~9]
    #    result += score[yut[0~3]-1]
        break
