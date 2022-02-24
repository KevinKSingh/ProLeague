import glob 
import os
from posixpath import split

def rename_csv(flag):
    path = "data/"+flag+"/*.csv" 
    leading_path = "data/"+flag+"/"
    files = glob.glob(path)
    words = ["Spring", "Summer", "Player Stats", "Playoffs"]
    for f in files:
        filename = f.replace(leading_path,'')
        year = "".join([x for x in filename if x in "1234567890"])
        print(type(filename))
        split_index = filename.index(year)+5
        split = filename[split_index:split_index+6]
        season = ""
        if "Playoff" in filename:
            season += "Playoffs.csv"
        else:
            season += "RegularSeason.csv"
        new_name = leading_path + flag + "_" + year + "_" + split + "_" + season
        os.rename(f,new_name)