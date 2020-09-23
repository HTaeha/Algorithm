from collections import deque
from copy import deepcopy

if __name__ == "__main__":
    N = int(input())
    counsel = []
    for i in range(N):
        counsel.append(list(map(int, input().split())))

    result = -1
    q = deque()
    q.append(counsel[0]+[0, True, 0])
    q.append(counsel[0]+[0, False, 0])
    while q:
        [t, p, i, flag, v] = q.popleft()

        if flag:
            if N > i+t:
                [next_t, next_p] = counsel[i+t]
                q.append([next_t, next_p, i+t, True, v+p])
                q.append([next_t, next_p, i+t, False, v+p])
            else:
                if N > i+t-1:
                    v += p
                result = max(result, v)
        else:
            if N > i+1:
                [next_t, next_p] = counsel[i+1]
                q.append([next_t, next_p, i+1, True, v])
                q.append([next_t, next_p, i+1, False, v])
            else:
                result = max(result, v)

    print(result)
