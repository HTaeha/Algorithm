zero = 0
one = 0

def check(arr):
    val = arr[0][0]

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != val:
                return False
    return True

def dfs(lst):
    global zero, one

    if check(lst):
        if lst[0][0] == 0:
            zero += 1
        else:
            one += 1
    else:
        idx = len(lst)//2

        if idx == 1:
            for i in range(len(lst)):
                for j in range(len(lst[0])):
                    if lst[i][j] == 0:
                        zero += 1
                    else:
                        one += 1
        else:
            temp = []
            for i in range(idx):
                temp.append(lst[i][:idx])
            dfs(temp)

            temp = []
            for i in range(idx):
                temp.append(lst[i][idx:])
            dfs(temp)

            temp = []
            for i in range(idx, len(lst)):
                temp.append(lst[i][:idx])
            dfs(temp)

            temp = []
            for i in range(idx, len(lst)):
                temp.append(lst[i][idx:])
            dfs(temp)

def solution(arr):
    global zero, one
    answer = []

    dfs(arr)
    answer = [zero, one]

    return answer

arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))
