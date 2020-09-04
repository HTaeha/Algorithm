def solution(lines):
    answer = 0

    # 체크해야 할 포인트 저장.
    check = set()
    # (start, finish) 시간 저장.
    pair = []
    for l in lines:
        [date, time, T] = l.split()
        temp_T = T[:-1]
        if '.' in temp_T:
            [T_s, T_ms] = temp_T.split(".")
            T = int(T_s)*1000 + int(T_ms)
        else:
            T = int(temp_T)*1000
        [hour, minute, second] = time.split(":")
        finish = calculate_second(hour, minute, second)
        start = finish - T + 1
        check.add(start)
        check.add(finish)
        pair.append((start, finish))
        
    # 체크 포인트마다 겹치는 일이 몇개인지 계산.
    for t in check:
        answer = max(answer, max_traffic(t, pair))
        
    return answer

# 시간, 분, 모두 초 단위로 바꿔서 합침.
# 모든 시간에 1000을 곱해서 소수점을 없앰.
def calculate_second(h, m ,s):
    [s, ms] = s.split(".")
    return int(ms) + int(s)*1000 + int(m)*60*1000 + int(h)*60*60*1000

# 해당 시간에 겹치는 traffic 갯수 return.
def max_traffic(time, pair):
    result = 0
    for p in pair:
        (s, f) = p
        time_end = time+1000
        if not(time > f or time_end <= s):
            result += 1
    return result

if __name__ == "__main__":
    lines = [
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"
    ]
    lines = [
    "2016-09-15 00:00:01.002 2.0s",
    "2016-09-15 00:00:02.000 2s"
    ]
    print(solution(lines))
