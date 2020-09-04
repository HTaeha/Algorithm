# 압축
# https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictionary = dict()
    for i, a in enumerate(alpha):
        dictionary[a] = i+1

    max_num = 26
    index = 0
    while True:
        s = ""
        flag = False
        for i in range(index, len(msg)):
            s += msg[i]
            if s not in dictionary:
                max_num += 1
                dictionary[s] = max_num
                answer.append(dictionary[s[:-1]])
                index = i
                flag = True
                break

        if not flag:
            answer.append(dictionary[s])
            break
                
        
    return answer

if __name__ == "__main__":
    msg = "KAKAO"
    print(solution(msg))
