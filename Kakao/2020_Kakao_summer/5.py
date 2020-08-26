def solution(n, path, order):
    answer = True

    max_num = max(max(path))+1
    path_map = [[0 for _ in range(max_num)] for _ in range(max_num)]

    for p in path:
        path_map[p[0]][p[1]] = 1
        path_map[p[1]][p[0]] = 1

    for i in range(len(path_map)):
        for j in range(len(path_map[0])):
            print(str(path_map[i][j])+' ', end = "")
        print()

    order_state = []
    lock_dict = dict()

    for o in order:
        lock_dict[o[1]] = True

    q = []
    visited = []
    for o in order:
        q.append(o[1])
        while True:
            new = q.pop(0)
            for i in range(len(path_map[new])):
                if path_map[new][i] == 1 and i not in visited:
                    if i in lock_dict and lock_dict[i] == False:
                        visited.append(new)
                        q.append(j)
            if visited
    print(lock_dict)

    return answer

if __name__ == "__main__":
    n = 9
    path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
    order = [[8,5],[6,7],[4,1]]
    solution(n, path, order)
