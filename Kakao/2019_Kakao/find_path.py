# 길 찾기 게임
# https://programmers.co.kr/learn/courses/30/lessons/42892

# 파이썬의 재귀는 1000으로 한도가 정해져 있어서 늘려줘야 함. 
import sys
sys.setrecursionlimit(10**6)

# Tree의 Node class.
class Node(object):
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.left = None
        self.right = None

class Binary_tree(object):
    def __init__(self, value, x, y):
        self.head = Node(value, x, y)

    def insert(self, node):
        current = self.head
        while True:
            if current == None or node.y == current.y:
                if node.x < parent.x:
                    parent.left = node
                else:
                    parent.right = node
                break

            if node.y < current.y:
                parent = current
                if node.x < current.x:
                    current = current.left
                else:
                    current = current.right

    def preorder(self, node, order = []):
        if node:
            order.append(node.value)
            self.preorder(node.left, order)
            self.preorder(node.right, order)

        return order

    def inorder(self, node, order = []):
        if node:
            self.inorder(node.left, order)
            self.inorder(node.right, order)
            order.append(node.value)

        return order

    def postorder(self, node, order = []):
        if node:
            self.postorder(node.left, order)
            self.postorder(node.right, order)
            order.append(node.value)

        return order

def solution(nodeinfo):
    answer = []

    for i, data in enumerate(nodeinfo):
        data.append(i+1)

    sorted_nodeinfo = sorted(nodeinfo, key = lambda x:(-x[1], x[0]))
    [x, y, v] = sorted_nodeinfo.pop(0)
    t = Binary_tree(v, x, y)

    for data in sorted_nodeinfo:
        [x, y, v] = data
        temp = Node(v, x, y)
        t.insert(temp)

    answer.append(t.preorder(t.head))
    answer.append(t.postorder(t.head))
    
    return answer

if __name__ == "__main__":
    nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    print(solution(nodeinfo))
