def solution(table, languages, preference):
    answer = ''
    score = dict()
    lanIndex = dict()
    for i, lan in enumerate(languages):
        lanIndex[lan] = i

    for row in table:
        rowList = row.split()
        key = rowList[0]
        score[key] = 0
        for i, l in enumerate(rowList):
            if i == 0:
                continue
            else:
                if l not in languages:
                    continue
                score[key] += (6-i)*preference[lanIndex[l]]

    answer = sorted(score.items(), key=lambda x:(-x[1], x[0]))[0][0]
    return answer

if __name__ == "__main__":
    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
    languages = ["PYTHON", "C++", "SQL"]
    preference = [7, 5, 5]

    print(solution(table, languages, preference))