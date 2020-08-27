# 2020 KAKAO BLIND REQRUITMENT
# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(p):
    answer = ''

    if check_correct(p):
        return p
    else:
        return recursive(p)
    
def recursive(p):
    ret = ""

    if find_u_v(p) == "":
        return ""
    else:
        u, v = find_u_v(p)

    # 3. 문자열 u가 올바른 괄호 문자열 이라면 문자열 v에 대해 1단계부터 다시 수행.
    while check_correct(u):
        ret += u
        if find_u_v(v) == "":
            return ret
        else:
            u, v = find_u_v(v)

    # 4. 문자열 u가 올바른 괄호 문자열이 아니라면 아래 과정을 수행합니다. 
    # 4-1.
    empty = '('
    # 4-2.
    empty += recursive(v)
    # 4-3.
    empty += ')'

    # 4-4.
    u = u[1:-1]
    for item in u:
        if item == '(':
            empty += ')'
        else:
            empty += '('

    ret += empty

    # 4-5.
    return ret
   
def find_u_v(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환.
    if len(p) == 0:
        return ''

    # 2. 문자열을 두 균형잡힌 괄호 문자열 u, v로 분리.
    stack = []
    u = ""
    v = ""
    l_count = 0
    r_count = 0
    flag = False
    for i, item in enumerate(p):
        if not flag:
            if l_count == r_count and i != 0:
                flag = True
                v += item
            else:
                if item == '(':
                    l_count += 1
                elif item == ')':
                    r_count += 1
                u += item
        else:
            v += item

    return u, v

# 올바른 괄호 문자열 체크.
def check_correct(s):
    stack = []

    try:
        for i, item in enumerate(s):
            if item == '(':
                stack.append(item)
            elif item == ')':
                stack.pop()
    except:
        return False

    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    p = "(()())()"
    p2 = ")("
    p3 = "()))((()"
    print(solution(p))
    print(solution(p2))
    print(solution(p3))
