def solution(N, stages):
    answer = [0 for i in range(N)]
    # The number of people.
    people_num = len(stages)
    
    # Ex) fail_rate[2] = Fail rate in stage 3.
    fail_rate = [0 for i in range(N)]
    # Ex) count[3] = The number of people in stage 4.
    count = [0 for i in range(N+1)]
    
    # Count people in the stage.
    for i, data in enumerate(stages):
        count[data - 1] += 1
    for i, data in enumerate(count):
        if i == N:
            break
        if i != 0:
            people_num -= count[i-1]
        # Fail rate is 0.
        if people_num == 0:
            fail_rate[i] = (i+1, 0)
        else:
            # (stage number, fail rate)
            fail_rate[i] = (i+1, count[i]/(people_num))
    # Sort by fail_rate.
    answer = sorted(fail_rate, key = lambda x:x[1], reverse = True)
    # Store only stage number in answer.
    for i, data in enumerate(answer):
        ans, fail = data
        answer[i] = ans
    
    return answer

if __name__ == "__main__":
    #N = 5
    #stages = [2, 1, 2, 6, 2, 4, 3, 3]
    N=4
    stages=[1,1,1,1]
    solution(N, stages)