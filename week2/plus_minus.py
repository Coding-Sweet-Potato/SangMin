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
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    for elem in arr:
        if elem > 0:
            positive += 1
        elif elem < 0 :
            negative += 1
        else:
            zero += 1
    
    po_latio = positive / len(arr)
    ne_latio = negative / len(arr)
    zero_latio = zero / len(arr)
    
    print("{0:.6f}".format(po_latio))
    print("{0:.6f}".format(ne_latio))
    print("{0:.6f}".format(zero_latio))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
