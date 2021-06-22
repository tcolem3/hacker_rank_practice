#!/bin/python3

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    #
    # Write your code here.
    #
    pos = 0
    neg = 0
    zer = 0
    for x in arr:
        if x == 0:
            zer += 1
        elif x > 0:
            pos += 1
        else:
            neg += 1
    print ("{:.6f}".format(pos/len(arr)))
    print ("{:.6f}".format(neg/len(arr)))
    print ("{:.6f}".format(zer/len(arr)))  

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
