# 2018 KAKAO BLIND RECRUITMENT
# 캐시
# https://programmers.co.kr/learn/courses/30/lessons/17680
# 19min 22sec

def solution(cacheSize, cities):
    answer = 0
    queue = []

    # If cacheSize is 0, all cache miss.
    if cacheSize == 0:
        return len(cities)*5

    # lowercase.
    for i, data in enumerate(cities):
        cities[i] = data.lower()

    for i, data in enumerate(cities):
        flag = False
        if len(queue) < cacheSize:
            for i_q, d_q in enumerate(queue):
                # cache hit.
                if d_q == data:
                    answer += 1
                    queue.pop(i_q)
                    queue.append(data)
                    flag = True
                    break
            # cache miss.
            if not flag:
                answer += 5
                queue.append(data)
        else:
            for i_q, d_q in enumerate(queue):
                # cache hit.
                if d_q == data:
                    answer += 1
                    queue.pop(i_q)
                    queue.append(data)
                    flag = True
                    break
            # cache miss.
            if not flag:
                answer += 5
                # LRU. 0 index is least recently used item.
                queue.pop(0)
                queue.append(data)
                
    return answer

if __name__ == "__main__":
    cacheSize = 3
    cities = ['Jeju', 'Jeju', 'Jeju', 'Jeju', 'Jeju', 'Jeju', 'Jeju', 'Jeju', 'Jeju', 'Jeju']
    res = solution(cacheSize, cities)
    print(res)
