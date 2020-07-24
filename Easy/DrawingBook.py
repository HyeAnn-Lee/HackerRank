# https://www.hackerrank.com/challenges/drawing-book/problem

import os
import sys

def pageCount(n, p):
    if p > n//2:
        p = n-p+(p%2)
    return p//2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
