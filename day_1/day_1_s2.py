import string
import re

# Define input data location
input_path = './data/d1_input.txt'

# Read lines from input data
with open(input_path) as file:
    lines = [line.rstrip() for line in file]

# Part two instructions ask to convert number strings 1 through 9 to digits before performing the rest

num_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

# Define a regex that will match all alpha and punctuation characters
alpha_pattern = re.compile('[' + re.escape(string.ascii_letters + string.punctuation) + ']')

# Encountered an issue when strings like 'oneight' are present. This should be extracted as '18'
# Lets change tactics

first_digits = []
last_digits = []

def get_digit(input, dir = 'forwards'):
    
    sub_str = ''

    if dir not in ['backwards', 'forwards']:
        print("Direction not recognized!")
        return None

    for i in range(len(input)):
        if dir == 'forwards':
            sub_str = input[:i+1]
        elif dir == 'backwards':
            sub_str = input[-(i+1):]
        # First check if we've spelled a digit
        for word, digit in num_dict.items():
            if re.search(word, sub_str):
                return re.sub(alpha_pattern, '', re.sub(word, str(digit), sub_str))
        # Next check if we have a true digit
        if re.sub(alpha_pattern, '', sub_str):
            return re.sub(alpha_pattern, '', sub_str)

first_digits = [get_digit(line, 'forwards') for line in lines]
last_digits = [get_digit(line, 'backwards') for line in lines]

combined = [int(fdig + ldig) for fdig, ldig in zip(first_digits, last_digits)]

# Calculate sum of all ints
sum(combined)