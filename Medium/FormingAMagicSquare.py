# https://www.hackerrank.com/challenges/magic-square-forming/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def absdif(s1, s2):
    result = 0
    for i in range(len(s1)):
        for j in range(len(s1[0])):
            result += abs(s1[i][j] - s2[i][j])
    return result

def formingMagicSquare(s):
    s1 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    s2 = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
    s3 = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    s4 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    result = min(absdif(s1, s), absdif(s2, s), absdif(s3, s), absdif(s4, s))

    s1.reverse()
    s2.reverse()
    s3.reverse()
    s4.reverse()

    return min(result, absdif(s1, s), absdif(s2, s), absdif(s3, s), absdif(s4, s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
