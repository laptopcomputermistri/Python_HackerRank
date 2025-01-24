#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Decoding the script by reading column-wise
decoded_script = ''.join([''.join(row[i] for row in matrix) for i in range(m)])

# Replace non-alphanumeric characters between alphanumeric characters with a single space
final_script = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded_script)

print(final_script)

'''Also 2nd format
import re

# Input dimensions
n, m = map(int, input().split())

# Reading the matrix
matrix = [input() for _ in range(n)]

# Decoding the script by reading column-wise
decoded_script = ''.join([''.join(row[i] for row in matrix) for i in range(m)])

# Replace non-alphanumeric characters between alphanumeric characters with a single space
final_script = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded_script)

print(final_script)
'''
