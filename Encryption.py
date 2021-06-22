#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    l = len(s) ** (1/2)
    rows = math.trunc(l)
    cols = 0
    finalArray = []
    if rows == l:
        cols = rows
    else:
        cols = rows + 1
    if (rows * cols)<len(s):
        rows += 1
    temprow = 0
    tempcols = cols
    #print (str(rows)+"......"+str(cols))
    for i in range (rows):
        if not i==0:
            temprow += cols
            tempcols += cols
        while tempcols > len(s):
            tempcols -= 1
        
        finalArray.append(s[temprow:tempcols])
        #print (finalArray[i])
    
    mystr = ""
        
    for i in range (cols):
        for j in range (rows):
            #print (str(j)+"....."+str(i))
            try:
                mystr += finalArray[j][i]
                #print (mystr)
            except IndexError:
                break
        mystr += " "
        
    return mystr
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
