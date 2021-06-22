#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    i=0
    final = []
    while i != (len(ranked)-1):
        if (ranked[i]==ranked[i+1]):
            ranked.pop(i+1)
            i -= 1
        i += 1
    t = 0
    t = len(ranked)
    for x in player:
        #while t>=len(ranked) and x<ranked[t]:
        while t!=0 and x>=ranked[t-1]:
            t -= 1
        ranked.insert(t,x)
        final.append(t+1)
    return (final)
            
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
