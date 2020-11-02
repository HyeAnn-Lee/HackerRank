# https://www.hackerrank.com/challenges/the-time-in-words/problem

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def digit2word(n):
    word = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return word[n-1]

def deci2word(n):
    if (n == 2):
        return "twenty"
    return "half"
    
def num2word(n):
    if (n < 10):
        return digit2word(n)
    if (10 <= n <= 19):
        if (n == 10):
            return "ten"
        if (n == 11):
            return "eleven"
        if (n == 12):
            return "twelve"
        if (n == 13):
            return "thirteen"
        if (n == 15):
            return "quarter"
        else:
            return digit2word(n-10) + "teen"
    if (n % 10 == 0):
        return deci2word(n // 10)
    return deci2word(n//10) + " " + digit2word(n%10)

def timeInWords(h, m):
    if (m == 0):
        return num2word(h) + " o' clock"
    if (m > 30):
        pre = num2word(60 - m)
        if (m == 59):
            pre += " minute"
        elif (m != 45):
            pre += " minutes"
        return pre + " to " + num2word(h+1)
    pre = num2word(m)
    if (m == 1):
        pre += " minute"
    elif (m % 15 != 0):
        pre += " minutes"
    return pre + " past " + num2word(h)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
