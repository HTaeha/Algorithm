from collections import deque
from copy import deepcopy

def calculate(oper, num1, num2):
    if oper == '+':
        result = num1 + num2
    elif oper == '-':
        result = num1 - num2
    elif oper == '*':
        result = num1 * num2
    elif oper == '/':
        if num1 < 0:
            result = -((-num1)//num2)
        else:
            result = num1//num2

    return result

if __name__ == "__main__":
    minimum = 10**9
    maximum = -10**9
    N = int(input())

    A = list(map(int, input().split()))

    [plus, minus, multiple, divide] = list(map(int, input().split()))

    duplicated = set()
    operand_check = dict()
    operand_check['+'] = plus
    operand_check['-'] = minus
    operand_check['*'] = multiple 
    operand_check['/'] = divide
    operand = []
    for i in range(plus):
        operand.append('+')
    
    for i in range(minus):
        operand.append('-')

    for i in range(multiple):
        operand.append('*')

    for i in range(divide):
        operand.append('/')

    s = deque()

    s.append(['start', 0, A[0], operand_check])
    while s:
        [op, count, value, check] = s.pop()

        if count == N-1:
            minimum = min(minimum, value)
            maximum = max(maximum, value)
            continue

        count += 1
        if check['+'] != 0:
            operand_check = deepcopy(check)
            operand_check['+'] -= 1
            s.append(['+', count, calculate('+', value, A[count]), operand_check])
        if check['-'] != 0:
            operand_check = deepcopy(check)
            s.append(['-', count, calculate('-', value, A[count]), operand_check])
            operand_check['-'] -= 1
        if check['*'] != 0:
            operand_check = deepcopy(check)
            s.append(['*', count, calculate('*', value, A[count]), operand_check])
            operand_check['*'] -= 1
        if check['/'] != 0:
            operand_check = deepcopy(check)
            s.append(['/', count, calculate('/', value, A[count]), operand_check])
            operand_check['/'] -= 1
          
    print(maximum)
    print(minimum)
