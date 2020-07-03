import collections

def clockwise(deq):
    last = deq.pop()
    deq.appendleft(last)
    return deq

def counterclockwise(deq):
    first = deq.popleft()
    deq.append(first)
    return deq

if __name__ == "__main__":
    wheel = []
    for i in range(4):
        deq = collections.deque(input())
        wheel.append(deq)

    print(wheel)
    n = int(input())
    for i in range(n):
        num, direc = map(int, input().split())

        if num == 1 or num == 2:
            # 오른쪽 체크.
            if wheel[num-1][2] != wheel[num][6]:
                if direc == 1:
                    wheel[num-1] = clockwise(wheel[num-1])

                    wheel[num] = counterclockwise(wheel[num])

                elif direc == -1:
                    wheel[num-1] = counterclockwise(wheel[num-1])

                    wheel[num] = clockwise(wheel[num])

             #왼쪽 체크.
            if wheel[num-1][6] != wheel[num-2][2]:
                if direc == 1:
                    wheel[num-1] = clockwise(wheel[num-1])

                    wheel[num-2] = counterclockwise(wheel[num-2])

                elif direc == -1:
                    wheel[num-1] = counterclockwise(wheel[num-1])

                    wheel[num-2] = clockwise(wheel[num-2])


        else:

    print(wheel)

    answer = 0
    if wheel[0][0] == '1':
        answer += 1
    if wheel[1][0] == '1':
        answer += 2
    if wheel[2][0] == '1':
        answer += 4
    if wheel[3][0] == '1':
        answer += 8

    print(answer)