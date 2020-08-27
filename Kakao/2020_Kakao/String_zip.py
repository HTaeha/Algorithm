# 2020 KAKAO BLIND REQRUITMENT
# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(s):
    answer = len(s)

    # 최대 split할 수 있는 길이는 전체 string길이의 절반이므로 절반까지만 for문을 돈다.
    for split in range(1, len(s)//2+1):
        # 현재 split 길이에서 만들어지는 string.
        temp_str = ""
        # 반복되는 split된 string 갯수 count.
        count = 1
        # 현재 비교하고 있는 split 된 string.
        split_str = s[0:split]

        # split만큼씩 뛰면서 s의 끝까지 도는 for문.
        for i in range(split, len(s), split):
            # 현재 split된 string.
            current_split = s[i:i+split]

            # 이전 string과 현재 string이 같으면 count에 +1.
            if split_str == current_split:
                count += 1
            # 이전 string과 현재 string이 다를 때
            else:
                # count가 1이면 쓰지 않음.
                # 이전까지의 string을 count와 함께 씀.
                if count != 1:
                    temp_str += str(count)
                temp_str += split_str

                # 비교할 split된 string을 현재 string으로 바꿈.
                split_str = current_split
                # count 초기화.
                count = 1

        # for문에서 이전 string들만 적어줬음.
        # for문의 마지막 string에 대한 처리.
        if count != 1:
            temp_str += str(count)
        temp_str += current_split
        
        # 가장 짧은 길이를 찾아 answer로 함.
        temp_answer = len(temp_str)
        if answer > temp_answer:
            answer = temp_answer

    return answer

if __name__ == "__main__":
    s = "aabbacccb"
    print(solution(s))
