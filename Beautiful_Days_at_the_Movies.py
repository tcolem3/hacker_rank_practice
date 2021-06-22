#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    c = 0
    for x in range (i, j+1):
        #temp = ((x-int("".join(reversed(list(str(x))))))/k)
        if ((x-int("".join(reversed(list(str(x))))))/k).is_integer():
            c+=1
        
    return (c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
