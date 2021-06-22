#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    marr = arr.copy()
    arr.remove(min(arr))
    marr.remove(max(marr))
    maxS = sum(arr)
    minS = sum(marr)
    print (str(minS)+" "+str(maxS))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
