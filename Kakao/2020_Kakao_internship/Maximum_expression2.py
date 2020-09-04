# 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257

import re
import copy

# 0 이상 integer만 가능.
# -, +, * 만 고려돼있음.
# expression : string 
#               ex) "(100-200)*300-500+20"
# order : dictionary
#         ex) {'+' = 1, '*' = 2, '-' = 1}
def infix_to_postfix(expression, order):
    result = []
    # operand 저장.
    stack = []
    # 숫자 character를 모아서 하나의 integer로 만듦.
    temp = ""
    for data in expression:
        if data in ['-', '+', '*']:
            if temp != "":
                result.append(int(temp))
                temp = ""

            while True:
                if len(stack) == 0:
                    stack.append(data)
                    break
                top = stack.pop()
                if order[top] >= order[data]:
                    result.append(top)
                else:
                    stack.append(top)
                    stack.append(data)
                    break
        else:
            temp += data

    result.append(int(temp))

    result = result + stack[::-1] 

    return result

def eval(postfix):
    result = 0
    stack = []

    for data in postfix:
        if data in ['-', '+', '*']:
            num2 = stack.pop()
            num1 = stack.pop()

            if data == '-':
                stack.append(num1-num2)
            elif data == '+':
                stack.append(num1+num2)
            elif data == '*':
                stack.append(num1*num2)
        else:
            stack.append(data)

    return stack.pop()

def permutation(l, n):
    result = []
    if n > len(l):
        return result

    if n == 1:
        for data in l:
            result.append([data])
    elif n > 1:
        for i in range(len(l)):
            temp = copy.deepcopy(l)
            temp.remove(l[i])
            for p in permutation(temp, n-1):
                result.append([l[i]] + p)

    return result

def solution(expression):
    answer = 0

    order = dict()

    perm = permutation([1,2,3], 3)
    print(perm)

    for p in perm:
        order['-'] = p[0]
        order['+'] = p[1]
        order['*'] = p[2]

        postfix_exp = infix_to_postfix(expression, order)
        answer = max(abs(eval(postfix_exp)), answer)

    return answer

if __name__ == "__main__":
    expression = "100-200*300-500+20"
    print(solution(expression))
