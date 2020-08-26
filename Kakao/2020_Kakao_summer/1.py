def solution(numbers, hand):
    answer = ''

    keypad = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]
    L_cur = '*'
    R_cur = '#'

    for i, num in enumerate(numbers):
        if num in [1, 4, 7]:
            answer += 'L'
            L_cur = str(num)
        elif num in [3, 6, 9]:
            answer += 'R'
            R_cur = str(num)
        else:
            for k_i in range(len(keypad)):
                for k_j in range(len(keypad[0])):
                    if keypad[k_i][k_j] == str(num):
                        r = k_i
                        c = k_j
                    if keypad[k_i][k_j] == L_cur:
                        l_r = k_i
                        l_c = k_j
                    if keypad[k_i][k_j] == R_cur:
                        r_r = k_i
                        r_c = k_j
            L_dist = abs(r-l_r) + abs(c-l_c)
            R_dist = abs(r-r_r) + abs(c-r_c)
            if L_dist < R_dist:
                answer += "L"
                L_cur = str(num)
            elif L_dist > R_dist:
                answer += "R"
                R_cur = str(num)
            else:
                if hand == "right":
                    answer += "R"
                    R_cur = str(num)
                else:
                    answer += "L"
                    L_cur = str(num)

    return answer

if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    solution(numbers, hand)

    '''
    keypad = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]
    for k_i in range(len(keypad)):
        for k_j in range(len(keypad[0])):
            print(keypad[k_i][k_j])
    '''
