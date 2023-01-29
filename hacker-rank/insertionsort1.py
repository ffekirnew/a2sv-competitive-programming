#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # use insertion sort to find the minimum number
    swap_idx = n - 1
    temp = arr[swap_idx]
    while swap_idx > 0 and temp < arr[swap_idx - 1]:
        arr[swap_idx] = arr[swap_idx - 1]
        swap_idx -= 1
        print(*arr)
    
    arr[swap_idx] = temp
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
