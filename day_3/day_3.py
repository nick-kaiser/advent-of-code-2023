# Goal is to read the input data file and calculate the sum of all values that have an adjacent symbol
# Periods are not counted as symbols

import re

input_path = './day_3/data/d3_input.txt'

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

# Now, if there are two numbers adjacent to a * multiply the two numbers and sum all these products

# First, detect the location of all *'s

gear_iter = [re.finditer('[\*]', line) for line in lines]

gear_list = list(map(list, gear_iter))

gear_pos = []

for row in gear_list:
    if len(row) == 0:
        gear_pos.append([])
    else:
        gear_indexes = []
        for match in row:
            gear_indexes.append(match.start())
        gear_pos.append(gear_indexes)

# Calculate valid gear products going through the rows for each gear

gear_products = []

for num, row in enumerate(gear_pos):
    # If there are no gears in the row, return an empty list
    if len(row) == 0:
        gear_products.append([])
    else:
        # valid_row_nums tracks valid products associated with gears
        valid_row_prods = []
        for gear in row:
            # num_adjacent tracks numbers adjacent to each gear
            num_adjacent = []
            # Look for matches in the prior row if row number > 0
            if num > 0:
                for vals in num_pos[num - 1]:
                    if gear in vals[0]:
                        num_adjacent.append(vals[1])
            # Always look for matches in the current row
            for vals in num_pos[num]:
                if gear in vals[0]:
                    num_adjacent.append(vals[1])
            # Look for matches in the next row if row number < 139
            if num < 139:
                for vals in num_pos[num + 1]:
                    if gear in vals[0]:
                        num_adjacent.append(vals[1])
            # Once adjacent numbers are identified, check if we have exactly two and calculate
            # and append the product if we do
            if len(num_adjacent) == 2:
                valid_row_prods.append(num_adjacent[0] * num_adjacent[1])
        # Append valid row prods to gear products (empty if none are found)
        gear_products.append(valid_row_prods)

gear_row_sums = [sum(gear_prods) for gear_prods in gear_products]

total_gear_sum = sum(gear_row_sums)

print(total_gear_sum)