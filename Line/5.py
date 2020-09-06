def solution(dataSource, tags):
    tag_dic = dict()

    for i, data in enumerate(dataSource):
        cnt = 0
        for t in tags:
            if t in data[1:]:
                cnt += 1
        tag_dic[data[0]] = cnt

    result = sorted(tag_dic.items(), key = (lambda x:x[0]))
    result = sorted(result, key = (lambda x:x[1]), reverse = True)

    res = []
    for i, data in enumerate(result):
        if i == 9 or data[1] == 0:
            break
        res.append(data[0])

    print res
if __name__ == "__main__":
    dataSource = [
        ["doc1", "t1", "t2", "t3"],
        ["doc2", "t0", "t2", "t3"],
        ["doc3", "t1", 't6', 't7'],
        ["doc4", "t1", "t2", "t4"],
        ["doc5", "t6", "t100", "t8"]
    ]
    tags = ["t1","t2","t3"]
    solution(dataSource, tags)