
def R(A):
    new = []
    length = 0
    for lst in A:
        d = dict()
        for j, num in enumerate(lst):
            if num == 0:
                continue
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        length = max(length, len(d)*2)
        temp = sorted(d.items(), key = lambda x:x[0])
        temp = sorted(temp, key = lambda x:x[1])
        temp2 = []
        for t in temp:
            temp2.append(t[0])
            temp2.append(t[1])
        new.append(temp2)

    for n in new:
        if len(n) < length:
            n += [0]*(length-len(n))

    return new

def C(A):
    A = rotate(A)
    A = R(A)
    A = rotate(A)

    return A

def rotate(lst):
    return list(map(list, zip(*lst)))

if __name__ == '__main__':
    r, c, k = map(int, input().split())
    A = []
    for i in range(3):
        temp = list(map(int, input().split()))
        A.append(temp)

    answer = 0
    while True:
        try:
            if A[r-1][c-1] == k:
                break
        except IndexError:
            pass

        if len(A) >= len(A[0]):
            A = R(A)
        else:
            A = C(A)

        answer += 1
        if answer > 100:
            answer = -1
            break

    print(answer)