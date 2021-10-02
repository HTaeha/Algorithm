from itertools import product

# 이전에 존재하는 단어들 계산. 
def solution(word):
    answer = 0
    vowel = {
        'A': 0,
        'E': 1,
        'I': 2,
        'O': 3,
        'U': 4
    }
    number = [781, 156, 31, 6, 1]
    wordLen = len(word)
    for i, char in enumerate(word):
        answer += vowel[char] * number[i]

    return answer+wordLen

# 직접 사전을 만든 후 찾을 단어의 인덱스를 출력.
def solution2(word):
    dictionary = []
    for i in range(1, 6):
        for p in product(["A", "E", "I", "O", "U"], repeat=i):
            dictionary.append("".join(p))

    dictionary.sort()
    return dictionary.index(word) +1

if __name__ == "__main__":
    word = "EIO"

    print(solution2(word))
