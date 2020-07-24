# https://www.hackerrank.com/challenges/counting-valleys/problem

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    height = 0
    SeaLevel = []
    for i in s:
        if i == 'U':
            height += 1
        else:
            height -= 1
        if height == 0:
            SeaLevel.append(i)
    return SeaLevel.count('U')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
