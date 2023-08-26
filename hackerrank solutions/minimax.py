#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort() # sort the numbers in ascending order
    min_arr = arr[:4]
    max_arr = arr[len(arr)-4:len(arr)+1]
    print(sum(min_arr), sum(max_arr))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
