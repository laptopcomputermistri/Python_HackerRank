def minion_game(string):
    # your code goes here
# Initialize scores
    stuart_score = 0
    kevin_score = 0
    string_length = len(string)
    
    # Iterate over each character in the string
    for i in range(string_length):
        if string[i] in 'AEIOU':
            kevin_score += string_length - i
        else:
            stuart_score += string_length - i

    # Determine the winner and print the result
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
