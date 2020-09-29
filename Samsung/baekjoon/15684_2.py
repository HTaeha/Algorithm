lines = dict()
candidate = dict()

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

def run():
    global N, H, lines

    for c in range(1, N+1):
        now_c = c
        now_r = 0
        #print(now_c, now_r)
        while True:
            flag = False
            temp_c1, temp_c2 = 0, 0
            temp_r1, temp_r2 = H+1, H+1
            if now_c != N:
                for r in lines[now_c]:
                    if now_r < r:
                        flag = True
                        temp_r1 = r
                        temp_c1 = now_c + 1
                        break
            if now_c != 1:
                for r in lines[now_c-1]:
                    if now_r < r:
                        flag = True
                        temp_r2 = r
                        temp_c2 = now_c - 1
                        break

            if not flag:
                break

            #print('temp : ',temp_r1, temp_c1)
            #print('temp : ',temp_r2, temp_c2)
            if temp_r1 > temp_r2:
                now_c, now_r = temp_c2, temp_r2
            else:
                now_c, now_r = temp_c1, temp_r1
            #print(now_c, now_r)

        if now_c != c:
            return False
        #print()

    return True

def is_valid(lst):
    global lines
    
    prev = [0, 0]
    for [i, j] in lst:
        if i in lines[j] or i in lines[j-1] or i in lines[j+1]:
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
        for i in range(-1, N):
            lines[i+1] = []
            candidate[i+1] = []

        for _ in range(M):
            a, b = map(int, input().split())
            lines[b].append(a)
        
        check = []
        for i in range(1, H+1):
            for j in range(1, N):
                if i not in lines[j] and i not in lines[j-1] and i not in lines[j+1]:
                    candidate[j].append(i)
                    check.append([i, j])

        if run():
            print('0')
        else:
            for answer in range(1, 4):
                for c in combinations(check, answer):
                    if not is_valid(c):
                        #print(lines)
                        #print(c)
                        #print()
                        continue

                    for [c_i, c_j] in c:
                        lines[c_j].append(c_i)
                        lines[c_j] = sorted(lines[c_j])

                    if run():
                        print(answer)
                        quit()
                    for [c_i, c_j] in c:
                        lines[c_j].remove(c_i)

            print('-1')
