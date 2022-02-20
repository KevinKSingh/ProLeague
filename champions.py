import numpy as np
import pandas as pd
import json
import csv
import glob
import os
import shutil

def generate_champion_stats(filename, region):
	player_names = [] 
	# opening the csv file
	print("Reading the csv file: " + str(filename) + "......\n") 
	readFile = pd.read_csv(filename)

	# Algorithm to build a player's champion database
	# 1) go through year csv file with the list of games
	# 2) Filter by region, if the player is in a region then add that match
	# 3) Filter by game , if player is in the game, look at the champion
	# 4) If champion record has not been created, create one, if champion exists append to that database
	# 5) store the stats appropriately , read in all the numbers

	# Filtering the database by Region
	data = readFile[readFile['league'] == region]

	# Fetching the list of players
	player_list = find_player_list(region)
    
	# Debugging, taking one player to see if I can fetch a list of games they have played in for that year
	player_name = "caPs"
	
	# creating an empty list of champions played 
	player_data = []

	# Obtain the index of the games featuring that player and storing that in player_data
	player_data = data.index[data['playername'] == player_name].tolist()
	# Finding the number of unique champions played by the player and storing that in a list
	champion_list = get_unique_champions_played(data, player_data)
	get_champion_stats(data, champion_list)

def get_champion_stats(data, champion_list, player_data):
	champion_stats = {}
	list_of_keys = [column for column in data.columns][24:-1]
	# Have to break it down into a dictionary with 3 layers. 
	# First layer key is the Champion and the value is the match_id
	# Second Layer the key is the match id which leads to all the information
	# Third Layer the keys are teh stat column headings and the values are the stats for that given game
	
	#return 0

def get_unique_champions_played(data, player_data):
	champion_list = []
	for index in player_data:
		champion = data.loc[index]['champion']
		if champion not in champion_list:
			champion_list.append(champion)	
	return champion_list

def find_player_list(region):
	folder = "/home/kevin/Documents/Kevin/Personal/Learning/Programming Projects/ProLeague/ProLeague-main/JSON/" + region + "/"
	subfolders = [ f.path for f in os.scandir(folder) if f.is_dir() ]
	player_list = []
	for item in subfolders:
		player_name = item.replace(folder,'')
		player_list.append(player_name)
	return player_list

		

