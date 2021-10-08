from itertools import combinations

def solution(n, wires):
    answer = n-2

    for deleteNode in wires:
        trees = [set()]
        first = True
        for wire in wires:
            if wire == deleteNode:
                continue
            [node1, node2] = wire
            if first:
                trees[0].add(node1)
                trees[0].add(node2)
                first = False
                continue

            addFlag = False
            for tree in trees:
                if node1 in tree:
                    tree.add(node2)
                    addFlag = True
                    break
                if node2 in tree:
                    tree.add(node1)
                    addFlag = True
                    break
            if not addFlag:
                trees.append({node1, node2})

        mergeTree(trees)
        if len(trees) == 2:
            diff = abs(len(trees[0]) - len(trees[1]))
            if answer > diff:
                answer = diff

    return answer

def mergeTree(trees):
    while True:
        flag = False
        for combTree in combinations(enumerate(trees), 2):
            (tree1, tree2) = combTree
            merged = set.union(tree1[1], tree2[1])
            if len(merged) == len(tree1[1])+len(tree2[1]):
                continue
            else:
                trees[tree1[0]] = merged
                del trees[tree2[0]]
                flag = True
                break
        if not flag:
            break

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
# n = 4
# wires = [[1,2], [2,3], [3,4]]
n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

print(solution(n, wires))
