# https://www.hackerrank.com/challenges/encryption/problem

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    L = len(s)
    row = math.ceil(math.sqrt(L))
    
    mat = list('' for _ in range(row))
    for i in range(L):
        mat[i%row] += s[i]
        
    result = ''
    for i in range(row):
        result += mat[i] + ' '
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
