// https://www.hackerrank.com/challenges/staircase/problem

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    str_list = []
    for i in range(n):
        str_list.append(' ')
    for i in range(n):
        str_list[n-i-1] = '#'
        print(''.join(str_list))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
