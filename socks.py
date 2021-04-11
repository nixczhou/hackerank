#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    ar.sort()
    i = 0
    print("now: ", ar)
    while(len(ar)>0):
        if(len(ar) == 1):
            ar.pop(i)
            break
        elif (ar[i] == ar[i+1]):
            count = count + 1
        print("count: ", count)
        if(ar[i+1]>ar[i]):
            ar.pop(i)
        else:
            ar.pop(i+1)
            ar.pop(i)
        print("now : ", ar) 
    return count

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
