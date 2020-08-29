class Node(object):
    def __init__(self, data, depth):
        self.data = data
        self.next = set()
        self.is_terminal = False
        self.depth = depth

class Trie(object):
    def __init__(self):
        self.root = Node("", 0)

    def insert(self, s):
        node = self.root
        for i, char in enumerate(s):
            found_char_flag = False
            for child in node.next:
                if child.data == char:
                    found_char_flag = True
                    node = child
                    break

            if not found_char_flag:
                new_node = Node(char, i+1)
                node.next.add(new_node)
                node = new_node

        node.is_terminal = True

    def search(self, s):
        count = 0
        char_idx = 0
        node = self.root
        queue = []
        queue.append(node)
        while len(queue):
            current = queue.pop(0)
            char_idx = current.depth

            if char_idx == len(s): 
                if current.is_terminal:
                    count += 1
                continue

            if s[char_idx] == '?':
                for child in current.next:
                    queue.append(child)
            else:
                for child in current.next:
                    if s[char_idx] == child.data:
                        queue.append(child)

        return count

    def print_node(self):
        node = self.root
        depth = 1
        queue = []
        queue.append(node)
        while len(queue):
            current = queue.pop(0)
            for child in current.next:
                print("depth : ", child.depth)
                print(child.data)
                queue.append(child)

            depth += 1

def solution(words, queries):
    answer = []

    t = Trie()
    for word in words:
        t.insert(word)

    for query in queries:
        answer.append(t.search(query))

    return answer

if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

    print(solution(words, queries))

