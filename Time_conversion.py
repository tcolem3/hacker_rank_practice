#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    temp = list(s)
    num = int(s[0]+""+s[1])
    if (temp[len(s)-2]=="P"):
        num += 12
        if num == 24:
            num = 12
        numTemp = list(str(num))
        temp[0] = numTemp[0]
        temp[1] = numTemp[1]
    else:
        if (num == 12):
            temp[0] = "0"
            temp[1] = "0"
    temp.pop()
    temp.pop()
    return ("".join(temp))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
