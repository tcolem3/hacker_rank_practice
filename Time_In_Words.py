#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
nums = {1: 'one', 2: 'two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}
def getNum (n):
    if n in nums:
        return str(nums[n]).lower()
    else:
        return str(nums[n-(n%10)]).lower()+" "+str(nums[n%10]).lower()

def timeInWords(h, m):
    results = ""
    if m==0:
        results = (str(getNum(h))+" o' clock")
    elif m==15:
        results = ("quarter past "+getNum(h))
    elif m==45:
        results = ("quarter to "+getNum(h+1))
    elif m==30:
        results = ("half past "+getNum(h))
    elif m>=2 and m<=29:
        results = (getNum(m)+" minutes past "+getNum(h))
    elif m>=31 and m<=58:
        results = (getNum(60-m)+" minutes to "+getNum(h+1))
    elif m==1:
        results = ("one minute past "+getNum(h))
    elif m==59:
        results = ("one minute to "+getNum(h+1))
    print(results)
    return (results)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())
    
    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
