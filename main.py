# this is going to be the back end script for my Professional League of Legends Stat 
# tracking app where I use the CSV data obtained from Oracle Elixir to store and display
# key stats for the pros from the 2015 season onwards. 

# First working verion should be the LEC or EU LCS (pre 2019) stats 
# can expand that to start reading in LPL , LCK and NA LCS stats
# after that I can add worlds and MSI stats too
# After that can do some comparison calculations to show damage/gold efficiency
# how many games they are ahead or behind, or study trends over the years for long 
# time players such as Faker/Perkz/Bjergsen/Rookie

# Update 31st August 
# Progress, the script can now read all the csv files and creates a JSON file for each 
# player for all the years. Now we can use the JSON files to post process the data 
# and do some statistical studies to get totals. One problem with the current data set is 
# that only one of the two splits Spring/Summer 
# I also have to break down the JSON files per year into per split and then per Regular 
# And Playoffs 

# Update 19th Feb
# Progress Tried to add LCK data and make a file called rename_file.py where it can mass rename all the files into the format that I want
# This failed.
# Created a separate script called database.py which contains all the functions to create the JSON files for the player's average season stats. 

from database import *
from rename_file import *

region_list = ["LEC", "LCK", "LPL", "LCS"]
#for region in region_list:
#    create_database(region)
#rename_csv("LCK")



# Test commit from terminal
