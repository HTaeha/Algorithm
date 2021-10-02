def solution(sizes):
    answer = 0

    maxW = 0
    maxH = 0
    for w, h in sizes:
        if w > h:
            if maxW < w:
                maxW = w
            if maxH < h:
                maxH = h
        else:
            if maxH < w:
                maxH = w
            if maxW < h:
                maxW = h

    answer = maxW*maxH
    return answer

if __name__ == "__main__":
    sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
    print(solution(sizes))