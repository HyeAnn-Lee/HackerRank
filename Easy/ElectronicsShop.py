# https://www.hackerrank.com/challenges/electronics-shop/problem

import os
import sys

def getMoneySpent(keyboards, drives, b):
    result = -1
    for i in keyboards:
        for j in drives:
            if (result < i+j <= b):
                result = i+j
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
