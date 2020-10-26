#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minX(arr):
    num = arr[0]
    min_val = num
    for i in range(1, len(arr)):
        num += arr[i]
        min_val = min(min_val, num)

    return 1-min_val


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = minX(arr)

    print(result)
