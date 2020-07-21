import copy

# Remove a duplicated element.
def make_set(arr):
    result = []
    for i, num in enumerate(arr):
        flag = False
        for j in range(i+1, len(arr)):
            # Find a duplicated element.
            # result 에 추가하지 않고 넘어간다. 
            if num == arr[j]:
                flag = True
                break
        if not flag:
            result.append(num)

    return result

def sum(base, other):
    # base set을 deepcopy로 가져옴.
    result = copy.deepcopy(base)
    for data in other:
        # base set에는 없지만 other set에만 있는 원소를 추가.
        if data not in base:
            result.append(data)
    return result

def complement(base, other):
    # 빈 list 생성.
    result = []
    for data in base:
        # other set에는 없지만 base set에만 있는 원소를 추가.
        if data not in other:
            result.append(data)
    return result

def intersect(base, other):
    # 빈 list 생성.
    result = []
    for data in other:
        # 두 set이 공통으로 가지고 있는 원소를 추가.
        if data in base:
            result.append(data)
    return result

def solution(arrA, arrB):
    answer = []

    arrA = make_set(arrA)
    arrB = make_set(arrB)
    answer.append(len(arrA))
    answer.append(len(arrB))
    arr_sum = sum(arrA, arrB)
    arr_com = complement(arrA, arrB)
    arr_inter = intersect(arrA, arrB)

    answer.append(len(arr_sum))
    answer.append(len(arr_com))
    answer.append(len(arr_inter))

    print(arrA)
    print(arrB)
    print(arr_sum)
    print(arr_com)
    print(arr_inter)
    print()
    print(answer)

if __name__ == "__main__":
    arrA = [1,2,3,2]
    arrB = [1,3]

    solution(arrA, arrB)
