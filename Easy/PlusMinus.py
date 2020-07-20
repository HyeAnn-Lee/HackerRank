# https://www.hackerrank.com/challenges/plus-minus/problem

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    ps = 0
    ng = 0
    zr = 0
    for i in range(n):
        if arr[i] > 0:
            ps += 1
        elif arr[i] == 0:
            zr += 1
        else:
            ng += 1
    print('{:.6f}'.format(ps/n))
    print('{:.6f}'.format(ng/n))
    print('{:.6f}'.format(zr/n))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
