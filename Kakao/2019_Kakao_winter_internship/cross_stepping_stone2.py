answer = 0

def solution(stones, k):
    global answer

    num = max(stones)
    num = 200000000
    binary_search(stones, k, 1, num)

    return answer

def check(stones, k, num):
    count = 0
    for s in stones:
        if s+1 <= num:
            count += 1
        else:
            count = 0
        if count >= k:
            return False
    return True

def binary_search(stones, k, left, right):
    global answer

    if left+1 == right:
        if check(stones, k, left):
            answer = max(answer, left)
        if check(stones, k, right):
            answer = max(answer, right)

    if left < right:
        num = (left+right)//2
        if check(stones, k, num):
            answer = max(answer, num)
            binary_search(stones, k, num+1, right)
        else:
            binary_search(stones, k, left, num-1)

if __name__ == "__main__":
    stones = [2, 4, 5, 2, 2, 1, 2, 2, 5, 1]
    stones = [5, 5, 5, 5, 5, 5, 5, 5, 5]
    k = 3
    print(solution(stones, k))
