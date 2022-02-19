import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import json
import csv
import glob
import os 
import shutil

# Defining Global Variables

# Database Year Start
startYear = 2015

# Database Year End
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
    player_name = readFile["Player"]
    print(readFile.ix[0])
    #print(player_name)   	
    return stats_dict 

def new_csv_reader(csv_file_name, year, stats_dict, player_names,flag):
    with open(csv_file_name) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for player_dict in csv_reader:
            player_name = player_dict['Player']
            player_stats = player_dict 
            exclude_keys = ['Player']
            updated_dict = {k: player_dict[k] for k in set(list(player_dict.keys())) - set(exclude_keys)}  
            #print(updated_dict)
            if player_name not in player_names:
                #print("New player detected")
                player_names.append(player_name)
                stats_dict = {}
                stats_dict[year] = updated_dict
            else:
                #stats_dict = load_dict_json(player name) 
                stats_dict = load_json_dict("JSON/"+flag+"/"+str(player_name)+".json")
                stats_dict[year] = updated_dict
            write_dict_json(stats_dict, "JSON/"+flag+"/"+str(player_name)+".json")
    return stats_dict

def create_database(flag):
    print("Creating files for: " + flag)
    path = "data/"+flag+"/*.csv" 
    files = glob.glob(path) 
    player_names = []
    springCount = 0
    summerCount = 0
    msiCount = 0
    worldsCount = 0
    for f in files:
        #year = f[8:12]
        year = f[8:-4]
        #print(year)
        stats_dict = {}
        new_csv_reader(f,year,stats_dict, player_names,flag)
        springCount += 1
    print("JSON file process completed....")    
    return player_names

def make_player_directories(player_names, flag):
    for player in player_names:
        directory = player
        parent_dir = "/home/kevin/Documents/Kevin/Personal/Learning/Programming Projects/ProLeague/ProLeague-main/JSON/" + flag + "/"
        path = os.path.join(parent_dir,directory)
        os.mkdir(path)

def move_json(player_names,flag):
    for player in player_names:
        initial_location = "/home/kevin/Documents/Kevin/Personal/Learning/Programming Projects/ProLeague/ProLeague-main/JSON/"+flag+"/"+player+".json"
        final_location = "/home/kevin/Documents/Kevin/Personal/Learning/Programming Projects/ProLeague/ProLeague-main/JSON/"+flag+"/"+player+"/"+player+".json"
        shutil.move(initial_location,final_location)