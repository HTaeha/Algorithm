#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lastLetters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING word as parameter.
#

def lastLetters(word):
    s = "%c %c"%(word[-1], word[-2])
    
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    word = input()

    result = lastLetters(word)

    fptr.write(result + '\n')

    fptr.close()

