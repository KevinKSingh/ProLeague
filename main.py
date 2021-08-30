# this is going to be the back end script for my Professional League of Legends Stat 
# tracking app where I use the CSV data obtained from Oracle Elixir to store and display
# key stats for the pros from the 2015 season onwards. 

# First working verion should be the LEC or EU LCS (pre 2019) stats 
# can expand that to start reading in LPL , LCK and NA LCS stats
# after that I can add worlds and MSI stats too
# After that can do some comparison calculations to show damage/gold efficiency
# how many games they are ahead or behind, or study trends over the years for long 
# time players such as Faker/Perkz/Bjergsen/Rookie

import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt 
import json
import csv
import glob 

# Defining Global Variables

# Database Year Start
startYear = 2015

# Database Yera End
endYear = 2021 

# Write any dictionary to json file
def write_dict_json(input_dict, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(input_dict, json_file)

# loads dict from json and returns the dict to be used
def load_json_dict(json_file):
    with open(json_file, 'r') as json_file:
        return json.load(json_file)

# Read CSV File
def read_csv_file(csv_file_name):
    print("Reading the csv file: " + str(csv_file_name) + ".....\n") 
    readFile = pd.read_csv(csv_file_name)
    print("Reading complete...")
    stats_dict = {} 
    print(readFile)
    return stats_dict 



# creating a list with the relevant filenames

spring_playoffs_files = ["LEC_"+str(x).zfill(4)+"_Spring_Playoffs.csv" for x in range(startYear,endYear)]
summer_playoffs_files = ["LEC_"+str(x).zfill(4)+"_Summer_Playoffs.csv" for x in range(startYear, endYear)]
spring_regular = ["LEC_"+str(x).zfill(4)+"_Spring_RegularSeason.csv" for x in range(startYear, endYear)]
summer_regular = ["LEC_"+str(x).zfill(4)+"_Summer_RegularSeason.csv" for x in range(startYear, endYear)]

files = spring_regular + spring_playoffs_files + summer_regular + summer_playoffs_files


for f in files:
    read_csv_file(f)




# 2015

# 2016 
