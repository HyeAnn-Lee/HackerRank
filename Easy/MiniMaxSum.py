// https://www.hackerrank.com/challenges/mini-max-sum/problem

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    mini = arr[0]
    maxi = arr[0]
    for ele in arr:
        if ele < mini:
            mini = ele
        if ele > maxi:
            maxi = ele
    Sum = sum(arr)
    print(f'{Sum-maxi} {Sum-mini}')

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
