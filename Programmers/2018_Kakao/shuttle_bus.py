# 1hour 12min 10sec pause.
def solution(n, t, m, timetable):
    answer = ''

    sort_timetable = sorted(timetable)
    '''
    for i, data in enumerate(sort_timetable):
        if data[0] == '0' and data[1] < '9':
            sort_timetable[i] = "09:00"
    '''

    now = "09:00"
    for i in range(n):
        h, m = time_to_int(now)
        if i == n-1:
            if len(sort_timetable) >= m:
                ans_h, ans_m = time_plus(sort_timetable[m-1], -1)
                answer = int_to_time(ans_h, ans_m)
            else:
                ans_h, ans_m = time_plus(now,t)
                answer = int_to_time(ans_h, ans_m)

            h, m = time_plus(now, t)
            now = int_to_time(h,m)
            print(now)
            if compare_time(answer, now) == -1:
                answer = now
            return answer
        count = 0
        for idx, time in enumerate(sort_timetable):
            time_h, time_m = time_to_int(time)
            if count == m:
                break
            if time_h < h or (time_h == h and time_m <= m):
                if len(sort_timetable) == 0:
                    answer = int_to_time(time_h, time_m)
                    return answer
                sort_timetable.pop(0)
                count += 1
        h, m = time_plus(now, t)
        now = int_to_time(h,m)
    answer = now
        

    print(sort_timetable)
    return answer
# s1 > s2 -> -1
# s1 == s2 -> 0
# s1 < s2 -> 1
def compare_time(s1, s2):
    h1, m1 = time_to_int(s1)
    h2, m2 = time_to_int(s2)
    if h1 < h2:
        return 1
    elif h1 > h2:
        return -1
    else:
        if m1 < m2:
            return 1
        elif m1 > m2:
            return -1
        else:
            return 0
def time_to_int(s):
    h = int(s[0])*10 + int(s[1])
    m = int(s[3])*10 + int(s[4])
    return h, m
def int_to_time(h,m):
    t = str(int(h/10)) + str(h%10) + ":" + str(int(m/10)) + str(m%10)
    return t
def time_plus(s, t):
    h, m = time_to_int(s)
    m += t
    h += int(m/60)
    m = m%60
    return h, m
if __name__ == "__main__":
    n = 1
    t = 1
    m = 5
    timetable = ["08:01", "08:02", "08:03", "08:00"]
    ret = solution(n,t,m,timetable)
    print("answer : ", ret)