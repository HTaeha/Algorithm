# 2018 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/17686
# 30min 30sec.
def solution(files):
    answer = []

    file_dic = dict()
    temp_list = []
    head_flag = False
    num_flag = False
    head = ""
    number = ""
    for idx, file in enumerate(files):
        temp_list = []
        head_flag = False
        num_flag = False
        number = ""
        for i, word in enumerate(file):
            if word.isdigit() and not head_flag:
                head = file[:i]
                head_flag = True
                num_flag = True
                number += word
            elif word.isdigit() and head_flag:
                number += word
            if num_flag and not word.isdigit():
                break
        temp_list.append(head)
        temp_list.append(number)
        temp_list.append(idx+1)
        file_dic[file] = temp_list

    temp = sorted(file_dic.items(), key = (lambda x:x[1][2]))
    temp = sorted(temp, key = (lambda x:int(x[1][1])))
    temp = sorted(temp, key = (lambda x:x[1][0].lower()))
    for i, data in enumerate(temp):
        s, l = data
        answer.append(s)

    return answer

if __name__ == "__main__":
    files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    solution(files)