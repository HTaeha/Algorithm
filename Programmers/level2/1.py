def solution(n):
    answer = 1

    for num in range(1, n//2+1):
        _sum = 0
        while True:
            _sum += num
            if _sum == n:
                answer += 1
                break
            elif _sum > n:
                break
            num += 1
            
    return answer

if __name__ == "__main__":
    n = 15
    print(solution(n))
