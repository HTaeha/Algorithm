#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'balancedSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSum(arr):
    left = arr[0]
    right = sum(arr) - arr[0] - arr[1]
    for i in range(1, len(arr)-1):
        pivot = i
        if left == right:
            return pivot

        right -= arr[i+1]
        left += arr[i]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = balancedSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

