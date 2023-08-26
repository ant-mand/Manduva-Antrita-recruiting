#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    
    for n in arr:
        if n > 0:
            positive += 1
        elif n < 0:
            negative += 1
        else:
            zero += 1
    
    size = len(arr)
    print("{:.6f}".format(positive / size))
    print("{:.6f}".format(negative / size))
    print("{:.6f}".format(zero / size))
    

if __name__ == '__main__':
    try:
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        assert (0 < n <= 100)
        assert (0 <= len(arr) <= 200)
        plusMinus(arr)
    except EOFError as e:
        print(e)
    except AssertionError as ae:
        print(ae)