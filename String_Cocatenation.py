def merge_the_tools(s, k):
    # your code goes here
    # Loop over the range of length of the string with step size k
    for i in range(0, len(s), k):
        substring = s[i:i+k]
        unique_substring = "".join(dict.fromkeys(substring))
        print(unique_substring)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
