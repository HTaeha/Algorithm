# 2020 KAKAO BLIND REQRUITMENT
# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

import copy
def solution(key, lock):
    pad_lock = zero_padding(lock, len(key))

    for _ in range(4):
        # rotate
        key = tuple(zip(*key[::-1]))

        for i in range(len(pad_lock)-len(key)+1):
            for j in range(len(pad_lock[0])-len(key[0])+1):
                flag = False
                check = copy.deepcopy(pad_lock)
                # key와 lock을 더해서 check 배열에 저장. 
                for k_i in range(len(key)):
                    for k_j in range(len(key[0])):
                        check[i+k_i][j+k_j] = key[k_i][k_j] + pad_lock[i+k_i][j+k_j]

                # key가 맞는지 check.
                for l_i in range(len(lock)):
                    for l_j in range(len(lock[0])):
                        # 안 맞는 부분이 있음.
                        if check[l_i+len(key)-1][l_j+len(key[0])-1] != 1:
                            flag = True
                            break

                    if flag:
                        break
                # key가 lock배열을 전부 1로 채움. 
                if not flag:
                    return True

    return False
    
# a 배열에 l길이-1 만큼 0 padding 한다.
def zero_padding(a, l):
    new_arr = [[0 for j in range(len(a)+(l-1)*2)] for i in range(len(a)+(l-1)*2)]
    for i in range(len(a)):
        for j in range(len(a[0])):
            new_arr[i+l-1][j+l-1] = a[i][j]

    return new_arr

if __name__ == "__main__":
    key = [[0,0,0], [1,0,0], [0,1,1]]
    lock = [[1,1,1], [1,1,0], [1,0,1]]

    print(solution(key, lock))
