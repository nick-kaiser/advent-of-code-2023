import string
import re

# Define input data location
input_path = './data/d1_input.txt'

# Read lines from input data
with open(input_path) as file:
    lines = [line.rstrip() for line in file]

# Reviewing the input data, it's clear that many of the letter strings spell numbers
# Instructions say to only worry about digits, so will ignore these for now

# Define a regex that will match all alpha and punctuation characters
alpha_pattern = re.compile('[' + re.escape(string.ascii_letters + string.punctuation) + ']')

# Extract non-alpha characters
clean_lines = [re.sub(alpha_pattern, '', line) for line in lines]

# Pair first and last digits and convert to int
coord_extract = [int(line[0] + line[-1]) for line in clean_lines]

# Calculate sum of all ints
sum(coord_extract)