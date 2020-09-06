graph = [[0, 1, 2, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Circular Queue.
class Queue(object):
    # MAX_LEN sized queue.
    def __init__(self, MAX_LEN):
        self.front = 0
        self.rear = 0

        # In Python, I don't have to do this, but to implement circular queues, I did it like dynamic assignment.
        self.data = [None for i in range(MAX_LEN)]
        # Maximum size of queue.
        self.MAX_LEN = MAX_LEN

    def enQueue(self, value):
        if not self.is_full():
            self.rear = (self.rear+1)%self.MAX_LEN
            self.data[self.rear] = value
            return True
        else:
            return False

    def deQueue(self):
        if not self.is_empty():
            self.front = (self.front+1)%self.MAX_LEN
            value = self.data[self.front]
            self.data[self.front] = None
            return value
        else:
            return -1

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def is_full(self):
        if self.rear == self.front and self.data[self.front] != None:
            return True
        else:
            return False

# A~K <-> 0~11
def translate(data):
    if isinstance(data, int):
        return chr(ord('A')+data)
    elif isinstance(data, str):
        return ord(data)-ord('A')

# origin : Start point.
# dest : Destination point.
# distance : List of routes and distances between start and destination points.
def bfs(origin, dest):
    distance = []
    q = Queue(100)
    q.enQueue([translate(origin), 0, origin])
    while not q.is_empty():
        [idx, count, s_alpha] = q.deQueue()
        if translate(idx) == dest:
            distance.append([s_alpha, count])
            continue
        for i, data in enumerate(graph[idx]):
            if data != 0:
                q.enQueue([i, count+data, s_alpha+translate(i)])

    return distance

# arr : The array to sort.
# col : The column index array to sort.
# reversed : True - Ascending.
#          : False - Descending.
def sort_2dArray(arr, col, reversed=True):
    for i, value in enumerate(arr):
        idx = i
        for j in range(i+1, len(arr)):
            value2 = arr[j]
            if reversed:
                if arr[idx][col] > value2[col]:
                    idx = j
            else:
                if arr[idx][col] < value2[col]:
                    idx = j
        arr[idx], arr[i] = arr[i], arr[idx]

def solution(origin, dest):
    answer = []

    res = bfs(origin, dest)
    if len(res) == 0:
        answer.append(-1)
    else:
        sort_2dArray(res, 0, True)
        for data in res:
            answer.append(data[1])

    return answer
