class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = set()
        self.is_terminal = False

class Trie(object):
    def __init__(self):
        self.root = Node("")

    def insert(self, s):
        node = self.root
        for char in s:
            found_char_flag = False
            for child in node.next:
                if child.data == char:
                    found_char_flag = True
                    node = child
                    break

            if not found_char_flag:
                new_node = Node(char)
                node.next.add(new_node)
                node = new_node

        node.is_terminal = True

    def search(self, s):
        node = self.root
        for char in s:
            found_char_flag = False
            for child in node.next:
                if child.data == char:
                    found_char_flag = True
                    node = child
                    break

            if not found_char_flag:
                return False

        return True

    def print_node(self):
        node = self.root
        depth = 1
        queue = []
        queue.append(node)
        while len(queue):
            current = queue.pop(0)
            print("depth : ", depth)
            for child in current.next:
                print(child.data)
                queue.append(child)

            depth += 1

if __name__ == "__main__":
    t = Trie()

    t.insert("apple")
    t.insert("approach")

    t.print_node()

    print(t.search("apple"))
    print(t.search("abc"))
    print(t.search("approach"))
    t.insert("abc")
    print(t.search("abc"))
