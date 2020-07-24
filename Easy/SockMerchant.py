# https://www.hackerrank.com/challenges/sock-merchant/problem

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    sock = set(ar)
    count = []
    for i in sock:
        count.append(ar.count(i))
    count = [x//2 for x in count]
    return sum(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
