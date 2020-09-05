import copy

class Mine(object):
    def __init__(self, value, x, y, arr):
        self.value = value
        self.x = x
        self.y = y
        self.arr = arr

    def print_value(self):
        print(self.value, self.x, self.y)


def bfs(arr, n):
    result = 1999000
    queue = []
    new_arr = copy.deepcopy(arr)
    new_arr[0][0] = -1
    queue.append([Mine(arr[0][0], 0, 0, new_arr), arr[0][0]])
    while len(queue) > 0:
        temp = queue.pop(0)
        new_arr = copy.deepcopy(temp[0].arr)
        if temp[0].x+1 < n and new_arr[temp[0].x+1][temp[0].y] != -1:
            new_arr[temp[0].x+1][temp[0].y] = -1
            queue.append([Mine(arr[temp[0].x+1][temp[0].y], temp[0].x+1, temp[0].y, new_arr), temp[1]+arr[temp[0].x+1][temp[0].y]])
        if temp[0].y+1 < n and new_arr[temp[0].x][temp[0].y+1] != -1:
            new_arr[temp[0].x][temp[0].y+1] = -1
            queue.append([Mine(arr[temp[0].x][temp[0].y+1], temp[0].x, temp[0].y+1, new_arr), temp[1]+arr[temp[0].x][temp[0].y+1]])
        if temp[0].x-1 >= 0 and new_arr[temp[0].x-1][temp[0].y] != -1:
            new_arr[temp[0].x-1][temp[0].y] = -1
            queue.append([Mine(arr[temp[0].x-1][temp[0].y], temp[0].x-1, temp[0].y, new_arr), temp[1]+arr[temp[0].x-1][temp[0].y]])
        if temp[0].y-1 >= 0 and new_arr[temp[0].x][temp[0].y-1] != -1:
            new_arr[temp[0].x][temp[0].y-1] = -1
            queue.append([Mine(arr[temp[0].x][temp[0].y-1], temp[0].x, temp[0].y-1, new_arr), temp[1]+arr[temp[0].x][temp[0].y-1]])

        if temp[0].x == n-1 and temp[0].y == n-1:
            if result > temp[1]:
                result = temp[1]

    return result

if __name__ == "__main__":
    n, d = map(int, input().split())
    arr = []
    for i in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp)

    '''
    for i in range(1, n):
        arr[i][0] += arr[i-1][0]
        arr[0][i] += arr[0][i-1]

    for i in range(1, n):
        for j in range(1, n):
            arr[i][j] += min(arr[i-1][j], arr[i][j-1])

    print(arr)
    '''
    #result = d - arr[n-1][n-1]
    result = d - bfs(arr, n)

    if result <= 0:
        result = -1

    print(result)
