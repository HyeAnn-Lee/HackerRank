// https://www.hackerrank.com/challenges/time-conversion/problem

import os
import sys

def timeConversion(s):
    time = s.split(':')
    PM = False
    if time[2][2] == 'P':
        PM = True
    time[2] = time[2][:2]
    
    if time[0] == '12':
        if not PM:
            time[0] = '00'
    else:
        if PM:
            hour = int(time[0])
            hour += 12
            time[0] = str(hour)

    result = ':'.join(time)
    return result

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
