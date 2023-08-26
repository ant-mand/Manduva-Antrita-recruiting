#!/bin/python3
import os
import re

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    s.upper()
    ns = re.split(r"PM|AM", s)
    time = ns[0]
    if ("PM" in s and time[:2] != "12"):
        hh = int(time[:2]) + 12
        time = str(hh) + time[2:]
    elif ("AM" in s and time[:2] == "12"):
        hh = int(time[:2]) - 12
        time = "0" + str(hh) + time[2:]
    return time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()