import queue
def solution(priorities, location):
    answer = 1
    #Store priorities sorted in descending order.
    sort_prior = sorted(priorities, reverse=True)
    q = queue.Queue()
    arr = queue.Queue()

    #Store priorities and index in arr.
    for i, data in enumerate(priorities):
        arr.put((data, i))

    while(True):
        data, index = arr.get()
        if data == sort_prior[0]:
            #If data is maximum value and same index with location, break.
            if index == location:
                break
            #If data is maximum value and different index with location, print(pop) current value and subtract the values in the queue and append them after arr.
            else:
                sort_prior.pop(0)
                answer += 1
                while(not q.empty()):
                    arr.put(q.get())
        #If data is not maximum value, enqueue (data, index) in the queue.
        else:
            q.put((data, index))

    return answer
