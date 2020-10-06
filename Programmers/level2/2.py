def solution(progresses, speeds):
    answer = []

    days = []
    for p, s in zip(progresses, speeds):
        _sum = p
        count = 0
        while True:
            _sum += s
            count += 1
            if _sum >= 100:
                break
        days.append(count)

    standard = days[0]
    count = 1
    for i in range(1, len(days)):
        if standard >= days[i]:
            count += 1
        else:
            answer.append(count)
            standard = days[i]
            count = 1
    answer.append(count)
            
    return answer

if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
#    progresses = [95, 90, 99, 99, 80, 99]
#    speeds = [1, 1, 1, 1, 1, 1]
    print(solution(progresses, speeds))
