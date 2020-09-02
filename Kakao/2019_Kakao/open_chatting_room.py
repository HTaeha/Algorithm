# 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888

# User class.
class User(object):
    def __init__(self, user_id, nickname):
        self.user_id = user_id
        self.nickname = nickname

    def change_nickname(self, new_name):
        self.nickname = new_name

def solution(record):
    answer = []
    temp_answer = []

    # 모든 user들이 들어있는 dictionary.
    # Key : user id
    # Value : user class
    user_manager = dict()

    for r in record:
        temp = r.split()
        # 처음 들어오는 user면 user_manager에 추가.
        if temp[1] not in user_manager:
            user_manager[temp[1]] = User(temp[1], temp[2])

        # Enter, Leave이면 temp_answer에 user class를 shallow copy해서 1,2로 enter, leave를 구분하며 append.
        # Enter, Change일 때 nickname을 변경.
        if temp[0] == "Enter":
            temp_answer.append((user_manager[temp[1]], 1))
            user_manager[temp[1]].change_nickname(temp[2])
        elif temp[0] == "Leave":
            temp_answer.append((user_manager[temp[1]], 2))
        elif temp[0] == "Change":
            user_manager[temp[1]].change_nickname(temp[2])

    # temp_answer에 들어온 순서대로 출력.
    for data in temp_answer:
        if data[1] == 1:
            answer.append("%s님이 들어왔습니다."%(data[0].nickname))
        elif data[1] == 2:
            answer.append("%s님이 나갔습니다."%(data[0].nickname))

    return answer

if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))
