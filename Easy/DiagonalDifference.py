# https://www.hackerrank.com/challenges/diagonal-difference/problem

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    dgn1 = 0
    dgn2 = 0
    for i in range(n):
        dgn1 += arr[i][i]
        dgn2 += arr[i][n-i-1]
    return abs(dgn1 - dgn2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
