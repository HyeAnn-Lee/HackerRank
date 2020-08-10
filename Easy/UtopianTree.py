# https://www.hackerrank.com/challenges/utopian-tree/problem

import math
import os
import random
import re
import sys

height = [1]
def utopianTree(n):
    if len(height) > n:
        return height[n]

    for i in range(len(height), n+1):
        if i%2:
            height.append(height[i-1]*2)
        else:
            height.append(height[i-1]+1)
    return height[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
