#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    print(N%2 == 1)
    print(6<=N<=20)
    print(2<=N<=5)
    print(N>20)
    if N%2 == 1 or 6<=N<=20:
        print("Weird")
    elif (2<=N<=5 or N>20) :
        print("Not Weird")

