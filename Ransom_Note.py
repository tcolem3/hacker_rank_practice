#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    #magSet = set(magazine)
    #noSet = set(note)
    #if noSet.issubset(magSet):
    #    print ("Yes")
    #else:
    #    print("No")
    
    magDic = {}
    noDic = {}

    for x in magazine:
        temp = magDic.get(x)
        if temp is None:
            magDic.update({x : 1})
        else:
            magDic.update({x : temp+1})
    
    for x in note:
        temp = noDic.get(x)
        if temp is None:
            noDic.update({x : 1})
        else:
            noDic.update({x : temp+1})
    
    final = True
    
    for x in noDic:
        if not x in magDic:
            final = False
            break
        elif noDic[x] > magDic [x]:
            final = False
            break
    if final == True:
        print ("Yes")
    else:
        print ("No")
        
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
