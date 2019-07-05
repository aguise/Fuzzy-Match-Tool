from fuzzywuzzy import fuzz

# Simple fucntion for calculating
# ration of similarity between two strings
# by using their levenshstein distance

def Ratio (a, b) :
	return fuzz.ratio(a.lower(), b.lower())
