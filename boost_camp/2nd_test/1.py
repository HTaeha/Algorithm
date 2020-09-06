keyboard = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
["Z", "X", "C", "V", "B", "N", "M", ",", ".", "?"]]

# now : Current location index.
# next : Next location index.
# return : Distance between now and next.
def next_pos(now, next):
    ud = now[0] - next[0]
    lr = now[1] - next[1]

    return [lr, ud]

# alpha : The character to find on the keyboard.
# return : The index of the character to find on the keyboard.
def find_index(alpha):
    for i in range(len(keyboard)):
        for j in range(len(keyboard[0])):   
            if keyboard[i][j] == alpha:
                return [i, j]

def solution(word):
    answer = ''

    now = [0, 0]
    for i in range(len(word)):
        next = find_index(word[i])
        [lr, ud] = next_pos(now, next)
        if ud < 0:
            answer += "_"*(-ud)
        else:
            answer += "^"*ud

        if lr < 0:
            answer += ">"*(-lr)
        else:
            answer += "<"*lr

        answer += '@'

        now = next

    return answer
