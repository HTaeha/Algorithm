# 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []

    for n1, n2 in zip(arr1, arr2):
        merge = n1|n2
        binary = format(merge, 'b').zfill(n)
        secret = binary.replace('0', ' ')
        secret = secret.replace('1', '#')
        answer.append(secret)

    return answer

if __name__ == "__main__":
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))
