from fuzzywuzzy import fuzz
import csv
import initialize
import xlwt
import data
from xlwt import Workbook
import pickle

# Simple fucntion for calculating
# ration of similarity between two strings
# by using their levenshstein distance
def ratio (a, b) :
        if contains_multiple_words(a):
                return fuzz.partial_ratio(a.lower(), b.lower())
        else :
                return fuzz.ratio(a.lower(), b.lower())

# Initializes dictionary with values corresponding to data types
def initialize_dict(dict_type, filename):
        dict = []
        if dict_type == "currencies":
                infile = open(filename, 'rb')
                dict = pickle.load(infile)
                infile.close()
        elif dict_type == "countries":
                infile = open(filename, 'rb')
                dict = pickle.load(infile)
                infile.close()
                print(dict["au"])
        elif dict_type == "languages":
                dict = initialize.languages()
        
        return dict

# Performs matching of words using ration calculation
def match(string, dict):
        high = 0
        second_highest = 0

        # Loop through base dictionary to narrow search
        for key in dict:
                string_ratio = ratio(string, key)

                if string_ratio > high:
                        high = string_ratio
                        key_string = key
                elif string_ratio > second_highest:
                        second_highest = string_ratio
                        key_string_2 = key

        dict_1 = dict[key_string]
        dict_2 = dict[key_string_2]

        high = 0
        dict_num = 0

        # Loop through more specific dictionaries to get exact match
        for i in dict_1:
                string_ratio = ratio(string, i)

                if string_ratio > high:
                        high = string_ratio
                        dict_num = 1
                        key_string = i
        for i in dict_2:
                string_ratio = ratio(string, i)

                if string_ratio > high:
                        high = string_ratio
                        dict_num = 2
                        key_string = i
        
        if dict_num == 1:
                return dict_1[key_string]
        else:
                return dict_2[key_string]

#  Outputs raw input and standardized form to excel sheet
def final_output(raw, standard, result, dict):
        wb = Workbook()
        ws = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)

        ws.write(0, 0, 'raw')
        ws.write(0, 1, 'standard')
        ws.write(0, 2, 'result')
        ws.write(0, 3, 'correct')
        ws.write(0, 4, 'percent')

        count = 1
        correct = 0
        for i, j, k in zip(raw, standard, result):
                ws.write(count, 0, i)
                ws.write(count, 1, j)
                ws.write(count, 2, k)
                
                if j == k:
                        ws.write(count, 3, 'TRUE')
                        correct += 1
                else:
                        ws.write(count, 3, 'FALSE')
                        dict[j][i] = j
                        
                count += 1
        
        ws.write(1, 4, 100*(correct / (count-1)))
        wb.save('output.xls')   

def contains_multiple_words(s):
        return len(s.split()) > 1