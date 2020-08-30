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
        # 해당 node 아래에 존재하는 단어의 수.
        self.count = 1

# Trie class.
class Trie(object):
    def __init__(self):
        # Root node. data가 없고 depth = 0.
        self.root = Node("", 0)
        # root의 count는 0부터 시작한다. 
        # insert할 때마다 증가시킨다. -> 해당 객체 안에 들어있는 word의 수를 의미.
        self.root.count = 0

    def insert(self, s):
        node = self.root
        node.count += 1
        for i, char in enumerate(s):
            found_char_flag = False
            # 이미 해당 node가 들어가 있으면 넘어감.
            for child in node.next:
                if child.data == char:
                    found_char_flag = True
                    node = child
                    node.count += 1
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
        for c in s:
            # ?가 나오는 순간 count가 정답이다.
            # count는 해당 node 밑에 존재하는 word의 수를 나타낸다.
            if c == '?':
                return node.count
            else:
                find_flag = False
                for child in node.next:
                    if c == child.data:
                        node = child
                        find_flag = True
                        break
                # 해당 character를 발견하지 못했을 때.
                if not find_flag:
                    return 0

    def print_node(self):
        node = self.root
        depth = 1
        queue = []
        queue.append(node)
        while len(queue):
            current = queue.pop(0)
            for child in current.next:
                print("depth : ", child.depth)
                print("count : ", child.count)
                print(child.data)
                queue.append(child)

            depth += 1

def solution(words, queries):
    answer = []

    forward = dict()
    backward = dict()

    # Make Trie class.
    for word in words:
        # word의 길이 별로 Trie 객체를 생성한다. 
        # forward는 word를 그대로 insert하고 backward는 word를 reverse하여 insert한다.
        if len(word) in forward:
            forward[len(word)].insert(word)
            backward[len(word)].insert(word[::-1])
        else:
            f_t = Trie()
            b_t = Trie()
            forward[len(word)] = f_t
            backward[len(word)] = b_t
            f_t.insert(word)
            b_t.insert(word[::-1])

    for query in queries:
        # 길이에 맞는 Trie 를 찾고 ?가 앞에서부터 나오면 backward로 하고 뒤에서부터 나오면 forward로 한다.
        if len(query) in forward:
            if query[0] == '?':
                t = backward[len(query)]
                answer.append(t.search(query[::-1]))
            else:
                t = forward[len(query)]
                answer.append(t.search(query))
        else:
            answer.append(0)

    return answer

if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]

    print(solution(words, queries))

