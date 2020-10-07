from collections import deque

DIRECTION = [[0, 1], [1, 0]]
def bfs(m, n, puddles):
    queue = deque()
    count = 0

    queue.append([1, 1])
    while queue:
        pos = queue.popleft()
        if pos == [m, n]:
            count += 1
        else:
            for d in DIRECTION:
                new_pos = [pos[0] + d[0], pos[1] + d[1]]
                if new_pos[0] > m or new_pos[1] > n or new_pos in puddles:
                    continue
                else:
                    queue.append(new_pos)

    count = count%100000007

    return count

def solution(m, n, puddles):
    answer = 0

    answer = bfs(m, n, puddles)

    return answer

if __name__ == "__main__":
    m = 4
    n = 3
    puddles = [[2, 2], [3, 3], [1, 2]]
    print(solution(m, n, puddles))
