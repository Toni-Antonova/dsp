# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
with open('metis/prework/dsp/python/football.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    diff = 10000
    title = ''
    for row in reader:
        find = abs(int(row['Goals']) - int(row['Goals Allowed']))
        if find < diff:
            diff = find
            title = row['Team']
        else:
            pass
    print (title)
    
