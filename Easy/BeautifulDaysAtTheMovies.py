# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

import math
import os
import random
import re
import sys

def reverse(i):
    rev = list(map(str, str(i)))
    rev.reverse()
    return int(''.join(rev))

def beautifulDays(i, j, k):
    result = 0
    for day in range(i, j+1):
        if not abs(day - reverse(day)) % k:
            result += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
