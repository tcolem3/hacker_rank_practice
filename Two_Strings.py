#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    for i, x in enumerate(s1):
        temp = x
        if (s2.find(temp)!= (-1)):
            return "YES"
        #else:
        #    for n in range (i+1,((len(s1)))):
        #        if i == n:
        #            temp = s1[i]
        #        elif n>i:
                   #temp = temp + s1[n]
        #           temp = s1[i:(n+1)]
                #else:
                #    break
                #print (temp +"........"+str(i+n))
        #        print (temp)
        #        if (s2.find(temp)>=(0)):
        #           return "YES"
        #            break
    return "NO"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
