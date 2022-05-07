from collections import deque

def solution (rc, operations):
    deq = deque()
    for row in rc:
        deq.append(deque(row))

    for operation in operations:
        if(operation == "ShiftRow"):
            ShiftRow(deq);
        elif(operation == "Rotate"):
            Rotate(deq);

    answer = []
    for row in deq:
        answer.append(list(row))
    return answer;

def ShiftRow(arr):
    row = arr.pop();
    arr.appendleft(row);

def Rotate(arr):
    rowLen = len(arr);

    for i in range(rowLen-2, -1, -1):
        change = arr[i].pop();
        arr[i+1].append(change);
    temp = arr[rowLen-1].popleft();
    for i in range(0, rowLen-2):
        change = arr[i+1].popleft();
        arr[i].appendleft(change);
    arr[rowLen-2].appendleft(temp)

rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
operations = ["Rotate", "ShiftRow"];

print(solution(rc, operations));