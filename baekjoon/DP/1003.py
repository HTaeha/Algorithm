memo = [(-1, -1) for i in range(41)]

def fibonacci(n):
    global memo

    if n == 0:
        memo[0] = (1, 0)
        return memo[0]
    elif n == 1:
        memo[1] = (0, 1)
        return memo[1]
    elif memo[n] != (-1, -1):
        return memo[n]
    else:
        memo[n] = (fibonacci(n-1)[0] + fibonacci(n-2)[0], fibonacci(n-1)[1] + fibonacci(n-2)[1])
        return memo[n]

if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        num = int(input())
        result = fibonacci(num)
        print("%d %d"%(result[0], result[1]))
