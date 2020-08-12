# https://www.hackerrank.com/challenges/non-divisible-subset/problem

import math
import os
import random
import re
import sys

def nonDivisibleSubset(k, s):
    # Write your code here
    rmd = list(map(lambda x: x%k, s))
    cnt = []
    for i in range(k):
        cnt.append(rmd.count(i))
    
    result = min(1, cnt[0])
    for i in range(k//2):
        if i+1 == k/2:
            result += min(1, cnt[i+1])
        else:
            result += max(cnt[i+1], cnt[k-i-1])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
