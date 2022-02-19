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
    # Write your code here
    min_sum = sorted(arr)
    max_sum = sorted(arr, reverse=True)
    
    min_sum.pop()
    max_sum.pop()
    
    print(sum(min_sum), sum(max_sum))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)