def solution(gems):
    answer = []
    answer_dist = 0

    gem_set = set(gems)
    gem_len = len(gem_set)
    check_set = set()

    result = dict()
    temp_res = []
    res = tuple()
    index = 0
    while True:
        temp_res.append(index+1)
        for i in range(index, len(gems)):
            if gems[i] not in check_set:
                check_set.add(gems[i])
            if len(check_set) == gem_len:
                temp_res.append(i+1)
                break
        if len(temp_res) != 2:
            break
        dist = temp_res[1] - temp_res[0]
        if index == 0:
            answer_dist = dist
            answer = temp_res
        elif answer_dist > dist:
            answer_dist = dist
            answer = temp_res

        if answer_dist == gem_len:
            break

        temp_res = []
        check_set = set()
        index += 1
        if (len(gems)-index) < gem_len:
            break

    print(answer)
    return answer

if __name__ == "__main__":
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    solution(gems)
