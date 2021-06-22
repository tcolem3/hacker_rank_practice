#!/bin/python3

import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
    for i in range (n):
        str = "#"
        spaces = ""
        j = i+1
        for x in range (i):
            str += "#"
        while j!= n:
            spaces += " "
            j += 1
        print (spaces+str)

if __name__ == '__main__':
    n = int(input())

    staircase(n)