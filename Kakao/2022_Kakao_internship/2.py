from collections import deque

def solution(queue1, queue2):
    answer = 0;

    sum1 = sum(queue1)
    sum2 = sum(queue2)
    deq1 = deque(queue1);
    deq2 = deque(queue2);

    while(True):
        if(sum1 < sum2):
            item = deq2.popleft();
            deq1.append(item);
            sum1 += item;
            sum2 -= item;
        elif(sum1 > sum2):
            item = deq1.popleft();
            deq2.append(item);
            sum2 += item;
            sum1 -= item;
        else:
            break;

        if(sum1 == 0 or sum2 == 0):
            return -1;

        answer += 1;

    return answer;

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

print(solution(queue1, queue2));