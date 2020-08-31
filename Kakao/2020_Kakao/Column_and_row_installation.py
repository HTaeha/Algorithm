# 2020 KAKAO BLIND REQRUITMENT
# 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061

import copy

# item과 frame이 제거 됐을 때 item을 설치 할 수 있는지 check함.
def delete_validate(item, frame, installed):
    [x, y, a, b] = frame
    test_frame = [x, y, a]

    # frame과 item의 인덱스를 기억해놓고 제거
    frame_idx = installed.index(test_frame)
    item_idx = installed.index(item)
    installed.remove(test_frame)
    installed.remove(item)

    # validate.
    ret = validate(item, installed)

    # 원래 위치에 다시 insert.
    installed.insert(frame_idx, test_frame)
    installed.insert(item_idx, item)
    if not ret:
        return False
    else:
        return True

def run(frame, installed):
    [x, y, a, b] = frame
    test_frame = [x, y, a]
    # 삭제
    # 해당 frame이 제거 됐을 때 인접해있는 frame을 찾아서 delete_validate를 함.
    # 하나라도 안 되면 False, 모두 통과하면 해당 frame 제거.
    if b == 0:
        # 기둥
        if a == 0:
            for item in installed:
                [temp_x, temp_y, temp_a] = item
                # 기둥
                if temp_a == 0:
                    if temp_x == x and (temp_y-1 == y or temp_y+1 == y):
                        if not delete_validate(item, frame, installed):
                            return False
                # 보
                else:
                    if (temp_x == x and (temp_y == y or temp_y-1 == y)) or (temp_x+1 == x and (temp_y == y or temp_y-1 == y)):
                        if not delete_validate(item, frame, installed):
                            return False
        # 보
        else:
            for item in installed:
                [temp_x, temp_y, temp_a] = item
                # 기둥
                if temp_a == 0:
                    if (temp_y == y and (temp_x == x or temp_x-1 == x)) or (temp_y+1 == y and (temp_x == x or temp_x-1 == x)):
                        if not delete_validate(item, frame, installed):
                            return False
                # 보
                else:
                    if temp_y == y and (temp_x-1 == x or temp_x+1 == x):
                        if not delete_validate(item, frame, installed):
                            return False

        installed.remove(test_frame)
        return True
    # 설치.
    else:
        # 설치 가능하면 기둥 또는 보 추가.
        if validate(test_frame, installed):
            installed.append(test_frame)

# 설치 가능한 지 검사해줌.
def validate(frame, installed):
    [x, y, a] = frame

    # 기둥
    if a == 0:
        # 바닥
        if y == 0:
            return True
        else:
            for item in installed:
                [temp_x, temp_y, temp_a] = item
                # 기둥 위
                if temp_a == 0:
                    if temp_x == x and temp_y+1 == y:
                        return True
                # 보 위
                else:
                    if temp_y == y and (temp_x == x or temp_x+1 == x):
                        return True

    # 보
    else:
        count = 0
        for item in installed:
            [temp_x, temp_y, temp_a] = item
            if temp_a == 0:
                if temp_y+1 == y and (temp_x == x or temp_x-1 == x):
                    return True
            else:
                if temp_y == y and (temp_x-1 == x or temp_x+1 == x):
                    count += 1
                    if count == 2:
                        return True

    return False

def solution(n, build_frame):
    installed = []

    for frame in build_frame:
        run(frame, installed)

    answer = sorted(installed, key = lambda x : (x[0], x[1], x[2]))
    return answer

if __name__ == "__main__":
    n = 5
    build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
    print(solution(n, build_frame))
