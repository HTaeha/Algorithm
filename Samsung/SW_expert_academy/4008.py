from itertools import permutations

def calculate(operand, operator):
    result = operand[0]
    for i, o in enumerate(operator):
        if o == '+':
            result += operand[i+1]
        elif o == '-':
            result -= operand[i+1]
        elif o == '*':
            result *= operand[i+1]
        else:
            if result > 0:
                result = result//operand[i+1]
            else:
                result = -((-result)//operand[i+1])

    return result

def dfs(count, temp):
    global operand, operator, Min, Max

    if count == N:
        value = calculate(operand, temp)
        Min = min(Min, value)
        Max = max(Max, value)
    else:
        if '+' in operator:
            temp.append('+')
            operator.remove('+')
            dfs(count+1, temp)
            temp.pop()
            operator.append('+')
        if '-' in operator:
            temp.append('-')
            operator.remove('-')
            dfs(count+1, temp)
            temp.pop()
            operator.append('-')
        if '*' in operator:
            temp.append('*')
            operator.remove('*')
            dfs(count+1, temp)
            temp.pop()
            operator.append('*')
        if '/' in operator:
            temp.append('/')
            operator.remove('/')
            dfs(count+1, temp)
            temp.pop()
            operator.append('/')

if __name__ == "__main__":
    T = int(input())

    for t in range(T):
        N = int(input())
        temp = list(map(int, input().split()))
        operator = []
        for i in range(temp[0]):
            operator.append('+')
        for i in range(temp[1]):
            operator.append('-')
        for i in range(temp[2]):
            operator.append('*')
        for i in range(temp[3]):
            operator.append('/')

        operand = list(map(int, input().split()))

        Max = -10**8 - 1
        Min = 10**8 + 1

        dfs(1, [])
        
        print("#%d %d"%(t+1, Max-Min))
