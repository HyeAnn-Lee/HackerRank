# https://www.hackerrank.com/challenges/queens-attack-2/problem

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    direc = []    
    for _ in range(8):
        # [up, up right, right, bottom right, down, bottom left, left, up left]
        direc.append([])

    for obs in obstacles:
        r_obs = obs[0]
        c_obs = obs[1]
        if (r_obs == r_q):      # horizontal
            if (c_obs < c_q):       # left
                direc[6].append(c_obs)
            else:                   # right
                direc[2].append(c_obs)
        elif (c_obs == c_q):    # vertical
            if (r_obs > r_q):       # up
                direc[0].append(r_obs)
            else:                   # down
                direc[4].append(r_obs)
        elif (r_q - r_obs == c_q - c_obs):
            if (r_obs > r_q):       # up right
                direc[1].append(r_obs)
            else:                   # bottom left
                direc[5].append(r_obs)
        elif (r_q - r_obs == c_obs - c_q):
            if (c_obs < c_q):       # up left
                direc[7].append(c_obs)
            else:                   # bottom right
                direc[3].append(c_obs)

    attack = min(direc[0] + [n+1]) - r_q - 1
    attack += min(direc[1] + [n+1, n+1 + r_q - c_q]) - r_q - 1
    attack += min(direc[2] + [n+1]) - c_q - 1
    attack += min(direc[3] + [n+1, r_q + c_q]) - c_q - 1
    attack += r_q - max(direc[4] + [0]) - 1
    attack += r_q - max(direc[5] + [0, r_q - c_q]) - 1
    attack += c_q - max(direc[6] + [0]) - 1
    attack += c_q - max(direc[7] + [0, r_q + c_q - (n+1)]) - 1
    return attack

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
