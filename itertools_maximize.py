# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

# Read input
k, m = map(int, input().split())
lists = [list(map(int, input().split()[1:])) for _ in range(k)]

# Generate all combinations
combinations = product(*lists)

# Compute the maximum value of (sum of squares) % m
max_value = 0
for combination in combinations:
    value = sum(x**2 for x in combination) % m
    max_value = max(max_value, value)

print(max_value)
