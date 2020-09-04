# 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256

import math
# 두 점 사이의 거리 측정.
def get_distance(n1, n2):
    return abs(n1[0]-n2[0])+abs(n1[1]-n2[1])

def solution(numbers, hand):
    answer = ''
    keypad = [[1,2,3], [4,5,6], [7,8,9], ['*', 0, '#']]
    # keypad의 좌표를 dictionary에 저장.
    key_pos = dict()
    for i in range(len(keypad)):
        for j in range(len(keypad[0])):
            key_pos[keypad[i][j]] = (i, j)

    # 시작점
    left = '*'
    right = '#'

    for n in numbers:
        # 왼쪽
        if n in [1,4,7]:
            left = n
            answer += 'L'
        # 오른쪽s
        elif n in [3,6,9]:
            right = n
            answer += 'R'
        else:
            # 거리 측정
            l_dist = get_distance(key_pos[n], key_pos[left])    
            r_dist = get_distance(key_pos[n], key_pos[right])    
            if l_dist > r_dist:
                right = n
                answer += 'R'
            elif l_dist < r_dist:
                left = n
                answer += 'L'
            # 거리가 같을 때는 오른손잡이인지 왼손잡이인지 체크.
            else:
                if hand == 'left':
                    left = n
                else:
                    right = n
                answer += hand[0].upper()

    return answer

if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = 'right'
    numbers =   [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = 'left'
    print(solution(numbers, hand))
