#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxSum = 0
    col = len(arr)
    row = len(arr[0])
    for i in range (0,col):
        tempSum = 0
        for j in range (0,row):
            if (i+2>col-1) or (j+2>row-1):
                break
            else:
                tempSum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
                if (tempSum>maxSum):
                    maxSum = tempSum
                elif (i==0 and j==0):
                    maxSum = tempSum
    return maxSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    #print (arr)

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
