# -*- coding: utf-8 -*-

from itertools import permutations

if __name__ == "__main__":
    r, g, b = map(int, input().split())
    flowers_input = input()

    flowers = []
    for f in flowers_input:
        flowers.append(f)

    flower_len = dict()
    flower_len['R'] = flowers.count("R")
    flower_len['G'] = flowers.count("G")
    flower_len['B'] = flowers.count("B")

    min_flower = [[], 10000000, 100000]

    for p in permutations(['R','G','B'], 3):
        num = len(flowers)//3
        rest = len(flowers)%3
        temp = p*num + p[:rest]

        price = 0
        count = 0

        R_len = temp.count("R") - flower_len['R']
        G_len = temp.count("G") - flower_len['G']
        B_len = temp.count("B") - flower_len['B']
        if R_len > 0:
            price += r*R_len
        if G_len > 0:
            price += g*G_len
        if B_len > 0:
            price += b*B_len

        for i, f in enumerate(temp):
            if f != flowers[i]:
                count += 1

        if min_flower[1] > price:
            min_flower[0] = temp
            min_flower[1] = price
            min_flower[2] = count
        elif min_flower[1] == price:
            if min_flower[2] > count:
                min_flower[0] = temp
                min_flower[1] = price
                min_flower[2] = count

    print(min_flower[1], min_flower[2])
                

