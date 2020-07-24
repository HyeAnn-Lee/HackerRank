# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    dop = 256
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1700<= year < 1918:
        if (year%4) == 0:
            days[1] += 1
    elif year == 1918:
        dop += 13
    else:
        if (year%400 == 0) or ((year%4 == 0 and year%100 != 0)):
            days[1] += 1
    
    for i in range(12):
        dop -= days[i]
        if dop<0:
            mm = str(i+1).zfill(2)
            dd = str(dop + days[i]).zfill(2)
            break

    return f'{dd}.{mm}.{str(year)}'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
