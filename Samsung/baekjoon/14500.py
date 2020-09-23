class Tetromino(object):
    def __init__(self):
        self.blocks = []
        self.set_blocks()

    def set_blocks(self):
        temp1 = [[1, 1, 1, 1]]
        temp2 = [[1], [1], [1], [1]]
        temp3 = [[1, 1], [1, 1]]
        temp4 = [[1, 1, 1], [1, 0, 0]]
        temp5 = [[0, 1, 1], [1, 1, 0]]
        temp6 = [[1, 0], [1, 1], [1, 0]]

        self.blocks.append(temp1)
        self.blocks.append(temp2)
        self.blocks.append(temp3)
        self.blocks.append(temp4)
        self.blocks.append(temp5)
        self.blocks.append(temp6)

    def rotate(self, idx):
        self.blocks[idx] = list(zip(*self.blocks[idx][::-1]))

    def symmetry(self, idx):
        original = self.blocks[idx]
        for i in range(len(original)):
            original[i] = original[i][::-1]

def calculate(base, arr):
    max_value = 0
    for i in range(len(base)):
        for j in range(len(base[0])):
            _sum = 0
            flag = True
            for a_i in range(len(arr)):
                if a_i + i >= len(base):
                    flag = False
                    break
                for a_j in range(len(arr[0])):
                    if a_j + j >= len(base[0]):
                        flag = False
                        break
                    _sum += arr[a_i][a_j] * base[i+a_i][j+a_j]
            if flag:
                max_value = max(max_value, _sum)

    return max_value

if __name__ == "__main__":
    N, M = map(int, input().split())

    paper = []
    for i in range(N):
        paper.append(list(map(int, input().split())))

    tetromino = Tetromino()

    result = 0
    result = max(result, calculate(paper, tetromino.blocks[0]))
    result = max(result, calculate(paper, tetromino.blocks[1]))
    result = max(result, calculate(paper, tetromino.blocks[2]))
    for i in range(4):
        result = max(result, calculate(paper, tetromino.blocks[3]))
        tetromino.symmetry(3)
        result = max(result, calculate(paper, tetromino.blocks[3]))
        tetromino.symmetry(3)
        tetromino.rotate(3)
    for i in range(2):
        result = max(result, calculate(paper, tetromino.blocks[4]))
        tetromino.symmetry(4)
        result = max(result, calculate(paper, tetromino.blocks[4]))
        tetromino.symmetry(4)
        tetromino.rotate(4)
    for i in range(4):
        result = max(result, calculate(paper, tetromino.blocks[5]))
        tetromino.rotate(5)

    print(result)
