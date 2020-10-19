#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n = float(len(arr))
    p_f = (len([x for x in arr if x > 0])/n)
    n_f = len([x for x in arr if x < 0])/n
    z_f = len([x for x in arr if x == 0])/n

    print("{:.6f}".format(p_f))
    print("{:.6f}".format(n_f))
    print("{:.6f}".format(z_f))
    
   

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
