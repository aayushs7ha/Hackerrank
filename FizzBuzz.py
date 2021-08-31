#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n=100):
    for i in range(1,n+1):
            if (i % 3 == 0) and (i % 5 == 0):
                print('FizzBuzz')
                continue
            elif (i % 3 == 0):
                print("Fizz")
                continue
            elif (i % 5 == 0):
                print('Buzz')
                continue
            else:
                print(i)

if __name__ == '__main__':
