# 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257

import re

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
        print(data)
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
        elif data == '(':
            stack.append(data)
        elif data == ')':
            result.append(int(temp))
            temp = ""
            while True:
                top = stack.pop()
                if top == '(':
                    break
                result.append(top)
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

def solution(expression):
    answer = 0

    order = dict()

    order['('] = 0
    order['-'] = 1
    order['+'] = 2
    order['*'] = 3

    postfix_exp = infix_to_postfix(expression, order)
    print(postfix_exp)
    print(eval(postfix_exp))

    return answer

if __name__ == "__main__":
    expression = "(100-200)*300-500+20"
    print(solution(expression))
