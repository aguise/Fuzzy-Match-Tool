from fuzzywuzzy import fuzz
import csv
import dictionary
from openpyxl import Workbook

# Simple fucntion for calculating
# ration of similarity between two strings
# by using their levenshstein distance
def ratio (a, b) :
        return fuzz.ratio(a.lower(), b.lower())

# Initializes dictionary with values corresponding to data types
def initialize(data):
        
        if data == "currency":
                dict = dictionary.currency()

        elif data == "country":
                dict = dictionary.country()
        
        else:
                dict = []
        
        return dict

# Performs matching of words using ration calculation
def match(string, dict):
        key_high = 0
        value_high = 0

        for key in dict:
                ratio_1 = ratio(string, key)
                ratio_2 = ratio(string, dict[key])

                if ratio_1 > ratio_2:
                        if ratio_1 > key_high:
                                key_high = ratio_1
                                key_string = key
                else:
                        if ratio_2 > value_high:
                                value_high = ratio_2
                                value_string = dict[key]

        if key_high > value_high:
                 print(dict[key_string])
        else:
                print(value_string)

#  Outputs raw input and standardized form to excel sheet
# def output(raw, standard):
#         wb = Workbook()
#         ws = wb.active

#         for i, j in zip(raw, standard):
#                 ws.append(i, j)

#         wb.save('output.xls')

