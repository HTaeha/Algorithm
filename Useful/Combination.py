def combination(lst,n):
    ret = []
    if n > len(lst): return ret

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n>1:
        for i in range(len(lst)-n+1):
            for temp in combination(lst[i+1:],n-1):
                ret.append([lst[i]]+temp)

    return ret

print(combination([1,1,3,4,5], 2))
