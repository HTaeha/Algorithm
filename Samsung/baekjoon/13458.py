if __name__ == "__main__":
    N = int(input())

    candidate = list(map(int, input().split()))

    [B, C] = list(map(int, input().split()))

    result = 0
    for c in candidate:
        result += 1
        if c < B:
            continue
        result += (c-B)//C
        if (c-B)%C != 0:
            result += 1

    print(result)
