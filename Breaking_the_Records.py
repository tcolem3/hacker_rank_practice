#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    high = low = scores[0]
    hc = 0
    lc = 0
    for i in range (1,len(scores)):
        if scores[i]>high:
            high = scores[i]
            hc += 1
        elif scores[i]<low:
            low = scores[i]
            lc += 1
    return ((hc), (lc))
        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
