#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    ctr = s.count('a')
    ctr *= (n // len(s))
    ctr += s[0:(n%len(s))].count('a') 
    return ctr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    n = int(input())

    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')

    fptr.close()
