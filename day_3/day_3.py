# Goal is to read the input data file and calculate the sum of all values that have an adjacent symbol
# Periods are not counted as symbols

import re

input_path = './day_3/data/d2_input.txt'

with open(input_path) as file:
    lines = [re.sub('\n', '', line) for line in file]

symbol_iter = [re.finditer('[^0-9.]', line) for line in lines]
num_iter = [re.finditer('[0-9]+', line) for line in lines]

symbol_list = list(map(list, symbol_iter))
num_list =  list(map(list, num_iter))

symbol_pos = []

for row in symbol_list:
    if len(row) == 0:
        symbol_pos.append([])
    else:
        symbol_indexes = []
        for match in row:
            symbol_indexes.append(match.start())
        symbol_pos.append(symbol_indexes)

num_pos = []

for num, row in enumerate(num_list):
    if len(row) == 0:
        num_pos.append([])
    else:
        num_indexes = []
        for match in row:
            # Create a list of the number start position, number end position, and the number itself
            num_indexes.append([list(range(match.start() - 1, match.end() + 1)), int(lines[num][match.start():match.end()])])
        num_pos.append(num_indexes)

valid_nums = []

for num, row in enumerate(num_pos):
    if len(row) == 0:
        valid_nums.append([])
    else:
        valid_row_nums = []
        for val in row:
            if (num > 0 and any(x in symbol_pos[num - 1] for x in val[0])) or \
                  any(x in symbol_pos[num] for x in val[0]) or \
                  (num < 139 and any(x in symbol_pos[num + 1] for x in val[0])):
                valid_row_nums.append(val[1])
        valid_nums.append(valid_row_nums)

row_sums = [sum(row) for row in valid_nums]

total_sum = sum(row_sums)

print(total_sum)

