def permutation(lst,n):
    ret = []
    if n > len(lst): return ret

    if n==1:
        for i in lst:
            ret.append([i])
    elif n>1:
        for i in range(len(lst)):
            temp = [i for i in lst]
            temp.remove(lst[i])
            for p in permutation(temp,n-1):
                ret.append([lst[i]]+p)

    return ret

print(permutation([1,2,3], 2))
