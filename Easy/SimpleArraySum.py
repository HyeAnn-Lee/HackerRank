// https://www.hackerrank.com/challenges/simple-array-sum/problem

import os
import sys

def simpleArraySum(ar):
    result = 0
    for i in range(ar_count):
        result += ar[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
