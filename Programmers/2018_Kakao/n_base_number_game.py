# 2018 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/17687
# 29min 8sec
def solution(n, t, m, p):
    answer = ''

    # count turn.
    cnt = 1
    num = 0
    # check the number of turn.
    check = 0
    # n based number. list
    check_num = n_base(n, num)
    while True:
        # Next number.
        if len(check_num) == 0:
            num += 1
            check_num = n_base(n, num)
        # My turn.
        if cnt%m == p or (cnt%m == 0 and m == p):
            answer += str(check_num[0])
            check += 1
            # Finish.
            if check == t:
                break
        check_num.pop(0)
        cnt += 1

    return answer

# Change n based number.
# return type : list
def n_base(n, num):
    result = []
    if num == 0:
        return [0]
    while True:
        if num == 0:
            break
        if num%n == 10:
            remainder = 'A'
        elif num%n == 11:
            remainder = 'B'
        elif num%n == 12:
            remainder = 'C'
        elif num%n == 13:
            remainder = 'D'
        elif num%n == 14:
            remainder = 'E'
        elif num%n == 15:
            remainder = 'F'
        else:
            remainder = str(num%n)
        result.insert(0, remainder)
        num = num//n
    return result

if __name__ == "__main__":
    n, t, m, p = 16, 16, 2, 2
    solution(n, t, m, p)