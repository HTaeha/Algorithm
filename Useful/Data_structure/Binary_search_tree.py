import random

class Node(object):
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, num):
        if self.root is None:
            self.root = Node(num)
            return True
        else:
            node = self.root
            while True:
                if node is None:
                    new = Node(num)
                    if parent.value > num:
                        parent.left = new
                    else:
                        parent.right = new
                    new.parent = parent
                    return True

                if node.value == num:
                    return False
                elif node.value > num:
                    parent = node
                    node = node.left
                else:
                    parent = node
                    node = node.right

    def search(self, num):
        node = self.root
        while True:
            if node is None:
                return False

            if node.value == num:
                return True
            elif node.value > num:
                node = node.left
            else:
                node = node.right

    def delete(self, num):
        node = self.root
        while True:
            if node is None:
                return False

            if node.value == num:
                if node.left is None and node.right is None:
                    new = None
                    if node.parent is not None:
                        if node.parent.value < node.value:
                            node.parent.right = new
                        else:
                            node.parent.left = new
                elif node.left is None:
                    new = node.right
                    new.parent = node.parent
                    if node.parent is not None:
                        if node.parent.value < node.value:
                            node.parent.right = new
                        else:
                            node.parent.left = new
                elif node.right is None:
                    new = node.left
                    new.parent = node.parent
                    if node.parent is not None:
                        if node.parent.value < node.value:
                            node.parent.right = new
                        else:
                            node.parent.left = new
                else:
                    new = node.right
                    while True:
                        if new.left is None:
                            break
                        new = new.left
                    if new.parent.value < new.value:
                        new.parent.right = new.right
                    else:
                        new.parent.left = new.right
                    if new.right is not None:
                        new.right.parent = new.parent

                    node.value = new.value
                    new = node

                if num == self.root.value:
                    self.root = new

                return True

            elif node.value > num:
                node = node.left
            else:
                node = node.right

    def preorder(self, node):
        if node is not None:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)

if __name__ == "__main__":
    temp = [5, 4, 7, 2, 1, 9, 10, 6]
    b = BST()
    for num in temp:
        b.insert(num)
        
    b.preorder(b.root)
    print()
    b.inorder(b.root)
    print()
    b.postorder(b.root)
    print()
    print(b.delete(5))
    print("root : ",b.root.value)
    b.preorder(b.root)
    print()
    b.inorder(b.root)
    print()
    b.postorder(b.root)
    print()
    print(b.delete(7))
    print(b.delete(7))
    print("root : ",b.root.value)
    b.preorder(b.root)
    print()
    b.inorder(b.root)
    print()
    b.postorder(b.root)
    print()


    # 1 ~ 1000 중, 100개의 숫자 랜덤 선택 
    bst_nums = set()
    while len(bst_nums) != 100:
        bst_nums.add(random.randint(0, 999))

    # 100개의 숫자 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
    binary_tree = BST()
    for num in bst_nums:
        binary_tree.insert(num)

    # 입력한 100개의 숫자를 검색 (검색 기능 확인)
    for num in bst_nums:
        if binary_tree.search(num) == False:
            print ('search failed', num)

    # 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
    delete_nums = set()
    bst_nums = list(bst_nums)
    while len(delete_nums) != 10:
        delete_nums.add(bst_nums[random.randint(0, 99)])

    # 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
    for del_num in delete_nums:
        if binary_tree.delete(del_num) == False:
            print ('search failed', delete_nums, del_num)
