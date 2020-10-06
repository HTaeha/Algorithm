
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
                    if node.parent.value < node.value:
                        new = None
                        node.parent.right = new
                    else:
                        node.parent.left = new
                elif node.left is None:
                    new = node.right
                    new.parent = node.parent
                    if node.parent.value < node.value:
                        node.parent.right = new
                    else:
                        node.parent.left = new
                elif node.right is None:
                    new = node.left
                    new.parent = node.parent
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
                    if new.right is not None:
                        new.parent.left = new.right
                        new.right.parent = new.parent

                    new.right = node.right
                    new.left = node.left
                    new.parent = node.parent
                    if node.parent.value < node.value:
                        node.parent.right = new
                    else:
                        node.parent.left = new

                if num == self.root.value:
                    self.root = new

                del node

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
    temp = [5, 4, 7, 2, 1, 9, 10]
    b = BST()
    for num in temp:
        b.insert(num)
        
    b.preorder(b.root)
    print()
    b.inorder(b.root)
    print()
    b.postorder(b.root)
    print()
    print(b.search(12))
    print(b.search(10))
    b.delete(4)
    b.inorder(b.root)
    b.delete(5)
    b.inorder(b.root)
