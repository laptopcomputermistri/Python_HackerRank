# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

def is_valid_integer_string(string):
    for char in string:
        if not (char.isdigit() or char == '-'):
            return False
    return True
    
def split_string(string):
    if '-' in string:
        segments = string.split('-')
    else:
        segments = [string[i:i+4] for i in range(0, len(string), 4)]
    
    return segments

def check_repeated_digits(string):
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
            if count >= 4:
                return False
        else:
            count = 1
    return True
    
def main():    
    n=int(input())
    for i in range(n):
        cr_ca_num=input()
        if(cr_ca_num[0] in '456'):
            if(len(cr_ca_num)== 16 or len(cr_ca_num)==19):
                if(is_valid_integer_string(cr_ca_num)):
                    segments=split_string(cr_ca_num)
                    card_num=segments[0]+segments[1]+segments[2]+segments[3]
                    if(check_repeated_digits(card_num)):
                        if(all(len(segment) == 4 for segment in segments)):
                            print("Valid")
                        else:
                            print("Invalid")
                    else:
                        print("Invalid")
                else:
                    print("Invalid")
            elif(len(cr_ca_num)!=16 or len(cr_ca_num)!=19):
                print("Invalid")
        elif((cr_ca_num[0]) in '1237890'):
            print("Invalid")            
if __name__ == "__main__":
    main()
