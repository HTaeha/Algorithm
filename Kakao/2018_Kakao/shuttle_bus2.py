# 셔틀버스
# https://programmers.co.kr/learn/courses/30/lessons/17678

def solution(n, t, m, timetable):
    answer = ''

    new_timetable = []
    for time in timetable:
        new_timetable.append(time_to_minute(time))

    new_timetable = sorted(new_timetable)

    start = time_to_minute("09:00")
    for i in range(n):
        bus = []

        for j in range(m):
            if len(new_timetable) == 0:
                break

            if new_timetable[0] <= start:
                person = new_timetable.pop(0)
                bus.append(person)
        
        start += t

    if len(bus) == m:
        answer = minute_to_time(bus[-1] - 1)
    else:
        answer = minute_to_time(start - t)
        
    return answer

def time_to_minute(s):
    arr = s.split(":")
    return int(arr[0])*60 + int(arr[1])

def minute_to_time(m):
    hour = m//60
    minute = m%60
    result = str(hour).rjust(2, '0') + ':' + str(minute).rjust(2, '0')

    return result

if __name__ == "__main__":
    n = 2
    t = 10
    m = 2
    timetable = ["09:10", "09:09", "08:00"]
    print(solution(n, t, m, timetable))
