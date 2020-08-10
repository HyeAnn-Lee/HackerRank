# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

import math
import os
import random
import re
import sys

def climbingLeaderboard(scores, alice):
    scores = list(set(scores))
    scores.sort(reverse = True)

    ir = iter(alice)
    mine = next(ir)

    result = []
    for i in range(len(scores), 0, -1):
        while (mine < scores[i-1]) and (len(result) < alice_count):
            result.append(i+1)
            if len(result) == alice_count:  # To prevent StopIteration
                break
            mine = next(ir)
    
    for _ in range(alice_count - len(result)):
        result.append(1)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
