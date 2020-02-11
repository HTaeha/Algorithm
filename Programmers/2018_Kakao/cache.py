# 19min 22sec
def solution(cacheSize, cities):
    answer = 0
    queue = []

    if cacheSize == 0:
        return len(cities)*5

    for i, data in enumerate(cities):
        cities[i] = data.lower()

    for i, data in enumerate(cities):
        flag = False
        if len(queue) < cacheSize:
            for i_q, d_q in enumerate(queue):
                if d_q == data:
                    answer += 1
                    queue.pop(i_q)
                    queue.append(data)
                    flag = True
                    break
            if not flag:
                answer += 5
                queue.append(data)
        else:
            for i_q, d_q in enumerate(queue):
                if d_q == data:
                    answer += 1
                    queue.pop(i_q)
                    queue.append(data)
                    flag = True
                    break
            if not flag:
                answer += 5
                queue.pop(0)
                queue.append(data)
                
    return answer

if __name__ == "__main__":
    cacheSize = 3
    cities = ['Jeju', 'Jeju', 'Jeju', 'Jeju', 'Jeju', 'Jeju', 'Jeju', 'Jeju', 'Jeju', 'Jeju']
    res = solution(cacheSize, cities)
    print(res)
