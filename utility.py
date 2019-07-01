import fuzzywuzzy as fuzz

''' Simple fucntion for calculating
ration of similarity between two strings
by using their levenshstein distance '''

def Ratio (a, b) {
	ratio = fuzz.ratio(a.lower(), b.lower())

	print(ratio)
}