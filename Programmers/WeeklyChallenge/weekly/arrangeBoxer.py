def solution(weights, head2head):
    answer = []
    data = []

    for i, battle in enumerate(head2head):
        point = 0
        larger = 0
        count = 0
        for j, bResult in enumerate(battle):
            if bResult == 'W':
                point += 1
                count += 1
                if weights[i] < weights[j]:
                    larger += 1
            elif bResult == 'L':
                count += 1
        winRate = point/count if count != 0 else 0
        data.append([i+1, winRate, larger, weights[i]])

    data.sort(key=lambda x:(-x[1], -x[2], -x[3]))
    answer = list(zip(*data[::1]))[0]

    return answer

if __name__ == "__main__":
    weights = [50, 82, 75, 120]
    head2head = ["NLWL","WNLL","LWNW","WWLN"]
    # weights = [60, 70, 60]
    # head2head = ["NNN","NNN","NNN"]

    print(solution(weights, head2head))