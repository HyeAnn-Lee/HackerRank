# https://www.hackerrank.com/challenges/picking-numbers/problem

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    analyze = []
    a_dist = list(set(a))
    a_dist.sort()
    result = 0

    for i in a_dist:
        cnt = a.count(i)
        analyze.append(tuple((i, cnt)))
        result = max(result, cnt)
    
    for i in range(len(analyze)-1):
        if (analyze[i+1][0] - analyze[i][0] == 1):
            result = max(result, analyze[i][1] + analyze[i+1][1])
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
