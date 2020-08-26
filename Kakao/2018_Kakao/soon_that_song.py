# 2018 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/17683
# 42min 43sec.
def solution(m, musicinfos):
    answer = []

    melody = {'C#' : 1, 'D#' : 2, 'F#' : 3, 'G#' : 4, 'A#' : 5}
    song_dic = dict()
    for key, val in melody.items():
        m = m.replace(key, str(val))

    for i, data in enumerate(musicinfos):
        split_data = data.split(',')
        t1, t2, name, mel = split_data
        for key, val in melody.items():
            mel = mel.replace(key, str(val))
        t = calc_time(t1, t2)
        mel2 = ""
        if len(mel) <= t:
            for i2 in range(t):
                mel2 += mel[i2%len(mel)]
        else:
            mel2 = mel[:t]

        song_dic[name] = [t, mel2, i+1]

    for key, val in song_dic.items():
        if m in val[1]:
            answer.append([key, val])

    if len(answer) == 0:
        return '(None)'

    temp_ans = sorted(answer, key = (lambda x:x[1][2]))
    temp_ans = sorted(temp_ans, key = (lambda x:x[1][0]), reverse = True)
    answer = temp_ans[0][0]
    
    return answer

def calc_time(t1, t2):
    temp_t1 = t1.split(':')
    temp_t2 = t2.split(':')
    result = int(temp_t2[0])*60 + int(temp_t2[1]) - (int(temp_t1[0])*60 + int(temp_t1[1]))

    return result
if __name__ == "__main__":
    m = "ABCDEFG"
    musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    solution(m, musicinfos)