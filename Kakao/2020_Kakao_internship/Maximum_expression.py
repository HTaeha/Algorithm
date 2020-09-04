from copy import deepcopy
from itertools import permutations

def solution(expression):
    answer = 0
    result = []

    ope_dict = dict()
    temp_num = ''
    s_expression = []
    for i, exp in enumerate(expression):
        if exp in ['-', '+', '*']:
            s_expression.append(temp_num)
            s_expression.append(exp)
            temp_num = ''
            ope_dict[exp] = 0
        else:
            temp_num += exp
    s_expression.append(temp_num)
    print(s_expression)

    l = len(ope_dict)
    if l == 1:
        for k, v in ope_dict.items():
            ope_dict[k] = 1
        post_order_exp = make_post_order(s_expression, ope_dict)
        result.append(abs(calc(post_order_exp)))
    elif l == 2:
        for p in list(permutations([1,2], 2)):
            i = 0
            for k, v in ope_dict.items():
                ope_dict[k] = p[i]
                i += 1
            post_order_exp = make_post_order(s_expression, ope_dict)
            result.append(abs(calc(post_order_exp))) 
    elif l == 3:
        for p in list(permutations([1,2,3], 3)):
            i = 0
            for k, v in ope_dict.items():
                ope_dict[k] = p[i]
                i += 1
            post_order_exp = make_post_order(s_expression, ope_dict)
            result.append(abs(calc(post_order_exp)))   

    answer = max(result)

    print(result)
    return answer

def make_post_order(s_expression, ope_dict):
    s = []
    q = []
    
    print(ope_dict)
    temp_exp = deepcopy(s_expression)
    while len(temp_exp):
        if temp_exp[0] not in ope_dict:
            q.append(temp_exp.pop(0))
        else:
            #if len(s) != 0 and ope_dict[s[-1]] >= ope_dict[temp_exp[0]]:
            while True:
                if len(s) != 0 and ope_dict[s[-1]] >= ope_dict[temp_exp[0]]:
                    q.append(s.pop())
                else:
                    break
            s.append(temp_exp.pop(0))

    while len(s):
        q.append(s.pop())

    return q

def calc(post_order_exp):
    s = []
    print(post_order_exp)

    for exp in post_order_exp:
        if exp not in ['-', '+', '*']:
            s.append(exp)
        else:
            n2 = s.pop()
            n1 = s.pop()
            if exp == '-':
                n = int(n1) - int(n2)
            elif exp == '+':
                n = int(n1) + int(n2)
            elif exp == '*':
                n = int(n1) * int(n2)
            s.append(n)

    print(s)
    return s[0]

if __name__ == "__main__":
    expression = "100-200*300-500+20"
    print(solution(expression))
