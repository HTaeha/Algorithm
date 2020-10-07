from itertools import permutations

def calculate(lst):
    temp_ans = 0
    time = 0
    for l in lst:
        if time < l[0]:
            temp_ans += l[1]
            time = l[0] + l[1]
        else:
            temp_ans += (time-l[0]) + l[1]
            time += l[1]

    temp_ans = temp_ans//len(lst)

    return temp_ans

def solution(jobs):
    answer = 987654321

    count = 0
    for p in permutations(jobs):
        answer = min(calculate(p), answer)
        if count == 10:
            break
        count += 1

    return answer

if __name__ == "__main__":
    jobs = [[0, 3], [1, 9], [2, 6]]
    print(solution(jobs))
