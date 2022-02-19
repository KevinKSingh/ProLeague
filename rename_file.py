import json
import csv
import glob 
import os

def rename_csv(flag):
    path = "data/"+flag+"/*.csv" 
    leading_path = "data/"+flag+"/"
    files = glob.glob(path)
    words = ["Spring", "Summer", "Player Stats", "Playoffs"]
    for f in files:
        filename = f.replace(leading_path,'')
        year = f[13:17]
        tail = f[17:len(f)]
        new_name = ""
        if(words[0] in filename and words[2] in filename):
            new_name = leading_path + flag + "_" + year + "_" + words[0] + "_RegularSeason.csv" 
        elif(words[0] in filename and words[3] in filename):
            new_name = leading_path + flag + "_" + year + "_" + words[1] + "_Playoffs.csv" 
        elif(words[1] in filename and words[2] in filename):
            new_name = leading_path + flag + "_" + year + "_" + words[0] + "_RegularSeason.csv" 
        elif(words[1] in filename and words[3] in filename):
            new_name = leading_path + flag + "_" + year + "_" + words[1] + "_Playoffs.csv"   
        else:
            new_name = f
        os.rename(f,new_name)