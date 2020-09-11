# 징검다리 건너기
# https://programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    answer = 0

    zero_idx = []
    stones_with_idx = dict()
    for i, s in enumerate(stones):
        if s not in stones_with_idx:
            stones_with_idx[s] = [i]
        else:
            stones_with_idx[s].append(i)

    sorted_stones = sorted(stones_with_idx.items(), key = lambda x:-x[0])
    while check(zero_idx, k):
        (min_s, idxs) = sorted_stones.pop()

        answer = min_s
        zero_idx += idxs

    return answer

def check(zero_idx, k):
    if len(zero_idx) == 0:
        return True
    elif len(zero_idx) == 1 and k == 1:
        return False
    sorted_zero = sorted(zero_idx)

    count = 0
    prev = sorted_zero[0]
    for i in range(1, len(sorted_zero)):
        if sorted_zero[i] == prev + 1:
            count += 1
        else:
            count = 0

        if count == k-1:
            return False

        prev = sorted_zero[i]

    return True

if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(solution(stones, k))
