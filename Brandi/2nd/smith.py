
if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    lr = []
    for i in range(k):
        l, r = map(int, input().split())
        lr.append([l, r])

    l_dict = dict()
    lr_sort = sorted(lr, key = lambda x: (x[0], -x[1]))
    for data in lr_sort:
        [l, r] = data
        if l not in l_dict:
            count = dict()
            temp = []
            for a in arr[l-1:r]:
                if a not in count:
                    count[a] = 1
                else:
                    count[a] += 1

                temp.append(a*count[a])

            l_dict[l] = temp
            
    for data in lr:
        [l, r] = data

        print(sum(l_dict[l][:r-l+1]))
