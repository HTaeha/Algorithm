# Trie에 들어가는 node class.
class Node(object):
    def __init__(self, data, depth):
        # character 하나.
        self.data = data
        # 다음 node를 저장하고 있음.
        self.next = set()
        # 단어의 끝인지 판별.
        self.is_terminal = False
        # 몇 번째 depth 인지 체크.
        self.depth = depth

# Trie class.
class Trie(object):
    def __init__(self):
        # Root node. data가 없고 depth = 0.
        self.root = Node("", 0)

    def insert(self, s):
        node = self.root
        for i, char in enumerate(s):
            found_char_flag = False
            # 이미 해당 node가 들어가 있으면 넘어감.
            for child in node.next:
                if child.data == char:
                    found_char_flag = True
                    node = child
                    break

            # 해당 node가 없으면 새로 생성.
            if not found_char_flag:
                new_node = Node(char, i+1)
                node.next.add(new_node)
                node = new_node

        # 마지막 node.
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

            # 해당 node가 없으면 바로 False return.
            if not found_char_flag:
                return False

        # 끝까지 돌 때까지 false에 안 결렸으면 True ㄱㄷ셔구.
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
