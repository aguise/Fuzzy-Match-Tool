from fuzzywuzzy import fuzz
import csv

# Simple fucntion for calculating
# ration of similarity between two strings
# by using their levenshstein distance

def Ratio (a, b) :
	return fuzz.ratio(a.lower(), b.lower())

def CSV (file):
	  
    # reads csv files from command line
    with open(file, 'r') as csvFile:
        reader = csv.reader(csvFile)

        for row in reader:
            print(row)
    
    return
