ProLeague
This repository is for my project where I have taken CSV files from the Oracle Elixir website which contains information from professional League of Legends games taken from the official Riot Games API. 

I am going to use Python to store, post process the data and potentially look to create a cross platform app (iOS and Android) using React Native or a website. This would be so that I get experience in learning how to do full stack development, management of a database and creation + deployment of a working app. 

Link to the website I got the LEC csv files from: https://oracleselixir.com/stats/players/byTournament

 Current Stage:
 
 1 commit, initial commit where I read all the regular season and play offs stats from the different CSV files 2015-2021 seasons are covered. 
 
 Features I would like to add to the Python side:
 
 - LCK, LPL and NA LCS, MSI, Worlds data
 - Player Champion stats across seasons
 - calculations to assess performance relative to peer/region/postition at the time
 - Cross region comparison per lane 
 - performance characteristics variation in time for long time players (Faker, Bjergsen, Rookie etc) 
 - Per Player Champion statistics with a match by match repository as well as global, annual averages for each tournament they played in. 
 - Finish LEC players first then add LEC players at worlds then add the other major regions in. 


Project Status:

Created a separate script called databases.py to handle the creation of the players JSON files and folder structure. Currently, the code works for LEC from 2015-2021 end and creates a JSON file for each player that has played in EU LCS or LEC (post rebrand) and gives their average stats per split (regular season and playoffs included) 

I have added the raw data files for LCK from 2013 onwards (including various renames). I tried to create a script to handle the automation of file renaming so the database part of the scripty which expects the file names in a certain format to work as intended, as of 19/02/2022, this is not working. Once this is done, I can repeat for LPL and LCS for the same timelines.Then I will be able to run the database script to generate the player stats for the splits. 

Features to Add:

Player Match History database and Champion specific stats. Breakdown stats by Split, by year, Playoffs vs Regular Season. Then stat specific stuff like win rates per split, win rates by year, by team. 


