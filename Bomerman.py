#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def cycleBomb(grid, full, cols, rows):
    for i in range (rows):
        for j in range (cols):
            if grid[i][j] == "O":
                full [i,j] = "."
                try:
                    full [i,j-1] = "."
                except IndexError:
                    pass
                try:
                    full [i,j+1] = "."
                except IndexError:
                    pass
                try:
                    full [i+1,j] = "."
                except IndexError:
                    pass
                try:
                    full [i-1,j] = "."
                except IndexError:
                    pass
    newIntial = []
    for i in range (rows):
        temp = ""
        for j in range (cols):
            temp += str(full[i,j])
        newIntial.append(temp)
    return (newIntial)

def bomberMan(n, grid):
    cols = len(grid[0])
    rows = len(grid)
    tempfull = { (i,j):"O" for i in range(rows) for j in range(cols) }
    full = tempfull.copy()
    
    if (n)==1:
        grid = grid
    elif n%2 == 0:
        returnFull = []
        for i in range (rows):
            temp = ""
            for j in range (cols):
                temp += str(full[i,j])
            returnFull.append(temp)
        grid = returnFull
    elif n%4 == 3:
        grid = (cycleBomb(grid, full, cols, rows))
    else:
        grid = (cycleBomb(grid, full, cols, rows))
        full = tempfull.copy()
        grid = (cycleBomb(grid, full, cols, rows))
    
    full = tempfull.copy()
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
