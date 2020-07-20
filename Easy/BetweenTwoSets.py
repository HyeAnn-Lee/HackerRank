# https://www.hackerrank.com/challenges/between-two-sets/problem

import math
import os
import random
import re
import sys

def getTotalX(a, b):
    # Find integers which are both 'common multiple of a' AND 'common divisor of b'
    answer = []
    for i in range(max(a), min(b)+1):
        answer.append(i)
        for j in a:     # check whether i is common multiple of all element in a
            if i%j:
                answer.pop()
                break
    
    fail = 0
    for i in answer:
        for j in b:     # check whether i is common divisor of all element in b
            if j%i:
                fail += 1
                break

    return len(answer) - fail

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
