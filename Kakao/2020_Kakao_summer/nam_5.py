import copy

def solution(n, path, order):
    answer = False

    tree = {}
    path = sorted(path)

    locked = set()
    start = set()

    idx = 0
    curr = []
    for p in path:
        if p[0] not in tree:
            tmp = []
            tmp.append(p[1])
            tree[p[0]] = tmp
        else:
            tree[p[0]].append(p[1])

        if p[1] not in tree:
            tmp = []
            tmp.append(p[0])
            tree[p[1]] = tmp
        else:
            tree[p[1]].append(p[0])

    # lock
    for o in order:
        locked.add(o[1])
        start.add(o[0])

    #traversal
    while True:
        nexti = False
        for o in order:
            cond, lock = o[0], o[1]

            # already out
            if cond not in start:
                continue

            check_list = copy.deepcopy(tree[cond])

            while len(check_list) is not 0:
                node = check_list.pop(0)

                if node in locked:
                    continue

                if node == 0 :
                    start.remove(cond)
                    locked.remove(lock)
                    nexti = True
                    break

                check_list = check_list + tree[node]

        if nexti is False:
            return False

        if len(start) is 0:
            return True

    return answer
