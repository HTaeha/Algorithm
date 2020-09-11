# 불량 사용자
# https://programmers.co.kr/learn/courses/30/lessons/64064

ban_list = set()
def solution(user_id, banned_id):
    answer = 0

    matching = dict()

    for b_id in banned_id:
        matching[b_id] = find_banned_id(user_id, b_id)
    
    dfs(matching, banned_id)

    answer = len(ban_list)

    return answer

def dfs(matching, banned_id):
    stack = []
    temp = [0 for _ in range(len(banned_id))]

    # 처음 위치의 것들 stack에 push.
    for first in matching[banned_id[0]]:
        stack.append([first, 0])
    while len(stack):
        [item, idx] = stack.pop()

        temp[idx] = item
        # 다음 것들 추가.
        if idx < len(banned_id)-1:
            for data in matching[banned_id[idx+1]]:
                stack.append([data, idx+1])
        # 끝에 도달.
        elif idx == len(banned_id)-1:
            temp_set = set(temp)
            if len(temp) == len(temp_set):
                temp_tuple = tuple(sorted(temp))
                ban_list.add(temp_tuple)
            
def find_banned_id(user_id, b_id):
    result = []
    for u_id in user_id:
        if len(u_id) != len(b_id):
            continue
        flag = True 
        for i, c in enumerate(b_id):
            if not(c == '*' or c == u_id[i]):
                flag = False
                break
        if flag:
            result.append(u_id)

    return result
                    
if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]
    banned_id = ["*****", "*****", "*****", "*****"]
    print(solution(user_id, banned_id))
