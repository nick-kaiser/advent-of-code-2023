import re
import pandas
import os

input_path = './day_2/data/d2_input.txt'

# Read lines from input data
with open(input_path) as file:
    lines = [line.rstrip() for line in file]

# Sets start with a space, continues through spaces, alnums, and comma.
game_set_pat = re.compile('[a-z0-9]+')
num_col_pat = re.compile('[0-9]* [a-z]')

# Remove game number
formated_lines = [re.sub('G.+: ', '', line) for line in lines]

red_count_pat = re.compile('[0-9]+(?= red)')
green_count_pat = re.compile('[0-9]+(?= green)')
blue_count_pat = re.compile('[0-9]+(?= blue)')

red_max = max(list(map(int, re.findall(red_count_pat, formated_lines[0]))))

max_colors = []

for game in range(len(formated_lines)):
    red_max = max(list(map(int, re.findall(red_count_pat, formated_lines[game]))))
    green_max = max(list(map(int, re.findall(green_count_pat, formated_lines[game]))))
    blue_max = max(list(map(int, re.findall(blue_count_pat, formated_lines[game]))))
    
    max_colors.append((red_max, green_max, blue_max))

# Goal is to find cases where game is possible with 12 red, 13 green, 14 blue

def possible_check(game, max_vals = (12, 13, 14)):
    if game[0] > max_vals[0] or game[1] > max_vals[1] or game[2] > max_vals[2]:
        return False
    else: return True

possible_results = [possible_check(game) for game in max_colors]

possible_games = [i+1 for i, x in enumerate(possible_results) if x]

sum_possible_indexes = sum(possible_games)

print(sum_possible_indexes)

# Now, calculate the product of the max required cubes for each game

cube_powers = [color[0] * color[1] * color[2] for color in max_colors]

print(sum(cube_powers))