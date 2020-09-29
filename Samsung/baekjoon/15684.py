lines = []
candidate = []

def combinations(lst,n):
    ret = []
    if n > len(lst): return ret

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n>1:
        for i in range(len(lst)-n+1):
            for temp in combinations(lst[i+1:],n-1):
                ret.append([lst[i]]+temp)

    return ret

def run(N, H, check):
    for c in range(1, N+1):
        now_c = c
        now_r = 0
        while True:
            flag = False
            for [i, j] in check:
                if j == now_c:
                    if now_r < i:
                        flag = True
                        now_r = i
                        now_c += 1
                if j+1 == now_c:
                    if now_r < i:
                        flag = True
                        now_r = i
                        now_c -= 1
                if flag:
                    break
            if not flag:
                break
        if now_c != c:
            return False

    return True

def is_valid(lst):
    global lines
    
    prev = [0, 0]
    for [i, j] in lst:
        if [i, j] in lines or [i, j-1] in lines or [i, j+1] in lines:
            return False
        if i == prev[0]:
            if j-1 == prev[1] or j+1 == prev[1]:
                return False
        prev = [i, j]

    return True
 
if __name__ == "__main__":
    N, M, H = map(int, input().split())

    if M == 0:
        print("0")
    else:
        for _ in range(M):
            a, b = map(int, input().split())
            lines.append([a, b])
        
        lines = sorted(lines, key = lambda x:(x[0]))
        for i in range(1, H+1):
            for j in range(1, N):
                if [i, j] not in lines and [i, j-1] not in lines and [i, j+1] not in lines:
                    candidate.append([i, j])

        if run(N, H, lines):
            print('0')
        else:
            for answer in range(1, 4):
                for c in combinations(candidate, answer):
                    if not is_valid(c):
                        continue
                    check = lines + c
                    check = sorted(check)
                    if run(N, H, check):
                        print(answer)
                        quit()

            print('-1')
