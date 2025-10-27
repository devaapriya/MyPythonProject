#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = -63 #-9*7

    for i in range(4):
        for j in range(4):
            hour_glass_sum = (arr[i][j]+arr[i][j+1]+arr[i][j+2]+
                                        arr[i+1][j+1]+
                              arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            if hour_glass_sum > max_sum :
                max_sum = hour_glass_sum

    print(max_sum)