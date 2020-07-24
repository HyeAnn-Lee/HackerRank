# https://www.hackerrank.com/challenges/migratory-birds/problem

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    freq = []
    for i in range(1, 6):
        freq.append(arr.count(i))
    maxi = max(freq)
    for i in range(5):
        if freq[i] == maxi:
            return i+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
