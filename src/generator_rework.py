import random

import pandas as pd

# load all files
system_df = pd.read_csv("./resources/System.csv")
star_df = pd.read_csv("./resources/Star.txt", sep='\t')


def roll_system(system_df):
    # replaces 'nieudolna petla', returns dataframe row
    rand_row = random.randrange(1, 100)
    for R1 in system_df['R1']:
        if rand_row > R1:
            system_data = system_df.loc[system_df['R1'] == R1]
    return system_data


rolled_system = roll_system(system_df)
random_star = random.randrange(int(rolled_system["SR1"]), int(rolled_system["SR2"]))


def roll_star(star_df, random_star):
    # replaces second 'while' loop, returns dataframe row
    for Range1 in star_df['Range1']:
        if random_star >= Range1:
            star_data = star_df.loc[star_df['Range1'] == Range1]
    return star_data


rolled_star = roll_star(star_df, random_star)
print(rolled_star)
#print(rolled_star['Outer'].to_string(index=False))
print(rolled_star['Outer'].to_string(index=False)[1])

def outer_reach_objects(outer_flag):

    if outer_flag == 'Weak':
        outer_objects = random.randrange(1, 6) - 2
        if outer_objects < 0:
            outer_objects = 0
    elif outer_flag == 'Normal':
        outer_objects = random.randrange(1, 6)
    elif outer_flag == 'Dominant':
        outer_objects = random.randrange(1, 6) + 2
    else:
        outer_objects = 0
    return outer_objects
