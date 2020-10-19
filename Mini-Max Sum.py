#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    
    minimum = sum(x for x in arr[:-1])
    maximum = sum(x for x in arr[1:])
    print("{} {}".format(minimum,maximum))
   


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
