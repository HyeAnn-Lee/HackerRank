# https://www.hackerrank.com/challenges/kangaroo/problem

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    dist = x1-x2
    speed = v1-v2
    if speed == 0:      # same speed
        if dist:
            return 'NO'
        else:
            return 'YES'
    if (dist > 0 and speed > 0) or (dist < 0 and speed < 0):    # cannot catch up
        return 'NO'
    if dist % speed:
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
