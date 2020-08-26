BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def numToNbase(num, b):
    res = ""
    while num:
        res+=BS[num % b]
        num //= b
    return res[::-1] or "0"

def solution(n, t, m, p):
    answer = ''

    cnt, num = 0, 0

    while True :
        nbase = numToNbase(num, n)
        print("[NBASE] " + nbase)
        for c in nbase:
            cnt += 1
            if cnt % m == p :
                answer += c
                print("Answer : " + answer + " len : " + str(len(answer)))
        if len(answer) == t :
            break
        num += 1

    return answer
if __name__ == "__main__":
    n, t, m, p = 16, 16, 2, 2
    solution(n, t, m, p)