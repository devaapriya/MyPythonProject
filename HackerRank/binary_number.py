#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    binary = format(n, 'b')
    # print(binary)
    prev_value =""
    num_of_once = {}
    counter = 0
    idx_pos = 0
    for i in range(len(binary)):
        # print(binary[i])
        # print(int(binary[i]) > 0)
        if int(binary[i]) == 1:
            # print("if")
            counter += 1
            num_of_once[idx_pos] = counter
            # print(num_of_once)
        else:
            if counter > 0:
                idx_pos += 1
            counter = 0

    # print(num_of_once)

    ones_count = 0
    for k,v in num_of_once.items():
        if num_of_once[k] > ones_count:
            ones_count = v

    print(ones_count)
