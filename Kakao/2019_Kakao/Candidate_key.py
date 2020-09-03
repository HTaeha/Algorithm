# 후보키
# https://programmers.co.kr/learn/courses/30/lessons/42890

def combination(l, n):
    result = []
    if n > len(l):
        return result

    if n == 1:
        for data in l:
            result.append([data])
    elif n > 1:
        for i in range(len(l)-n+1):
            for temp in combination(l[i+1:], n-1):
                result.append(temp + [l[i]])

    return result

# 최소성 체크.
# keys : 후보키가 들어있는 set.
# check : 최소성 체크하고 싶은 key (tuple)
def minimality_check(keys, check):
    # 후보키가 없으면 True
    if len(keys) == 0:
        return True
    for data in keys:
        flag = False
        # 후보키 중에 하나라도 포함되는 것이 있다면 False.
        for d in data:
            if d not in check:
                flag = True
                break
        if not flag:
            return False
    return True
    
def solution(relation):
    answer = 0

    # relation에서 속성별로 list를 만들어 저장.
    tuples = list(zip(*relation))

    # DB에 저장된 item의 갯수
    item_len = len(relation)

    # 후보키 저장하는 set.
    keys = set()
    # 속성별로 순서대로 번호를 매김.
    temp = [i for i in range(len(tuples))]
    for i in range(len(tuples)):
        # 속성의 갯수를 변화시키면서 combination을 생성.
        comb = combination(temp, i+1)
        for c in comb:
            uniqueness_check = set()
            key_flag = True
            for j in range(item_len):
                item = []
                # tuple로 선택된 속성들의 값을 묶음. 
                for i in c:
                    item.append(tuples[i][j])
                item = tuple(item)
                # set에 겹치는 값이 있는지 체크.
                if item in uniqueness_check:
                    key_flag = False
                    break
                else:
                    uniqueness_check.add(item)
            # 유일성 만족.
            if key_flag:
                # 최소성 만족.
                if minimality_check(keys, tuple(c)):
                    keys.add(tuple(c))

    answer = len(keys)

    return answer

if __name__ == "__main__":
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(solution(relation))
