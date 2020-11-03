# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    n = len(container)
    capa = list(sum(container[i]) for i in range(n))
    balls = []
    for i in range(n):
        ball = 0
        for j in range(n):
            ball += container[j][i]
        balls.append(ball)
    
    capa.sort()
    balls.sort()
    
    if (capa == balls):
        return "Possible"
    else:
        return "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
