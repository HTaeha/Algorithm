def solution(heights):
    answer = []

    #O(n^2) using for loop.
    '''
    for i, data in enumerate(heights):
        flag = False
        if i == 0:
            answer.append(0)
        else:
            for j in range(i-1, -1, -1):
                if heights[j] > data:
                    answer.append(j+1)
                    flag = True
                    break
            if not flag:
                answer.append(0)
    '''
    #O(n) using stack.
    stack = []
    for i, data in enumerate(heights):
        flag = False
        if i == 0:
            answer.append(0)
            stack.append((data, i))
        else:
            top, index = stack.pop()
            if top > data:
                answer.append(index+1)
                stack.append((top, index))
                stack.append((data, i))
            else:
                while(len(stack)>0):
                    top, index = stack.pop()
                    if top > data:
                        answer.append(index+1)
                        stack.append((top, index))
                        stack.append((data, i))
                        flag = True
                        break
                if not flag:
                    answer.append(0)
                    stack.append((data, i))
    return answer
