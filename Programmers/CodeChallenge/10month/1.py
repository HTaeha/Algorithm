def solution(n):
    answer = 0

    new = ""
    while n > 0:
        new += str(n%3)
        n = n//3

    new = str(int(new))

    for i, n in enumerate(new):
        answer += int(n) * 3**(len(new)-i-1)
    
    return answer

n = 125
print(solution(n))
