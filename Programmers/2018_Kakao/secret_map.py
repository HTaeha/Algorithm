# 10min 56sec
def solution(n, arr1, arr2):
    answer = []
    ans_str = ""

    for i, data in enumerate(arr1):
        ans_str = ""
        # Transform decimal number to binary number, align right, 0-padding
        d1 = format(data, 'b').rjust(n, '0')
        d2 = format(arr2[i], 'b').rjust(n, '0')
        for idx in range(n):
            # 0, 0 -> ' ' space, else -> '#' wall
            if d1[idx] == '0' and d2[idx] == '0':
                ans_str += ' '
            else:
                ans_str += '#'
        answer.append(ans_str)

    return answer

if __name__ == "__main__":
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]

    solution(n, arr1, arr2)
    