def clockwise(w):
    return w[-1] + w[:len(w)-1]

def counter_clockwise(w):
    return w[1:] + w[0]

if __name__ == "__main__":
    # 더미 데이터 -1. 톱니바퀴가 1~4이므로 index도 1~4로 맞춘 것.
    wheel = [-1]
    for i in range(4):
        wheel.append(input())

    K = int(input())
    for i in range(K):
        [n, d] = list(map(int, input().split()))

        check = []
        check.append([n, d])
        if n != 1:
            temp_d = d
            for idx in range(n-1, 0, -1):
                w1 = wheel[idx]
                w2 = wheel[idx+1]
                if w1[2] == w2[6]:
                    break
                else:
                    temp_d *= -1
                    check.append([idx, temp_d])

        temp_d = d
        for idx in range(n, len(wheel)-1):
            w1 = wheel[idx]
            w2 = wheel[idx+1]
            if w1[2] == w2[6]:
                break
            else:
                temp_d *= -1
                check.append([idx+1, temp_d])

        for c in check:
            if c[1] == 1:
                wheel[c[0]] = clockwise(wheel[c[0]])
            elif c[1] == -1:
                wheel[c[0]] = counter_clockwise(wheel[c[0]])

    result = int(wheel[1][0]) + int(wheel[2][0])*2 + int(wheel[3][0])*4 + int(wheel[4][0])*8
    print(result)

