#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def countPerms(n):
    if n == 1:
        return 5

    INF = 10**9 + 7
    
    # 'a', 'e', 'i', 'o', 'u'
    now = [0 for _ in range(5)]
    prev = [1 for _ in range(5)]

    for i in range(1, n):
        now[0] = prev[1]
        now[1] = prev[0] + prev[2]
        now[2] = prev[0] + prev[1] + prev[3] + prev[4]
        now[3] = prev[2] + prev[4]
        now[4] = prev[0]

        for j in range(5):
            now[j] = now[j]%INF
            prev[j] = now[j]

    return sum(now)%INF

if __name__ == '__main__':
    n = int(input().strip())

    result = countPerms(n)

    print(result)
