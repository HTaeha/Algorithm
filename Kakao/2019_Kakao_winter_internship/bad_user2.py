# 불량 사용자
# https://programmers.co.kr/learn/courses/30/lessons/64064

import re
from itertools import permutations
def solution(user_id, banned_id):
    answer = 0
    ids = set()

    for p in permutations(user_id, len(banned_id)):
        if check(p, banned_id):
            ids.add(tuple(sorted(p)))

    answer = len(ids)
    return answer

def check(p, banned_id):
    for i, ban in enumerate(banned_id):
        if not validate(ban, p[i]):
            return False

    return True

def validate(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if not (s1[i] == s2[i] or s1[i] == '*' or s2[i] == '*'):
            return False
    return True

if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]
    print(solution(user_id, banned_id))

