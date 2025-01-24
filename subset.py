# Enter your code here. Read input from STDIN. Print output to STDOUT
# Function to check if A is a subset of B
def is_subset(A, B):
    return A.issubset(B)

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read set A
    n_A = int(input())
    set_A = set(map(int, input().split()))

    # Read set B
    n_B = int(input())
    set_B = set(map(int, input().split()))

    # Check if A is a subset of B and print the result
    print(is_subset(set_A, set_B))
