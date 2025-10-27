#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    # print(n, 1<=n<=1000)

    if 1<=n<=1000 :
        arr = list(map(int, input().rstrip().split()))
        # print(arr, len(arr))
        # arr_reversed = ""
        if 1<= len(arr) <=10000 :
            for num in arr[::-1]:
                print(num, end=" ")

        # print(arr_reversed)
