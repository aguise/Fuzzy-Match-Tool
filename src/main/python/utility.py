from fuzzywuzzy import fuzz
import csv
import initialize
import xlwt
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
        infile = open(filename, 'rb')
        dict = pickle.load(infile)
        infile.close()

        return dict

# Performs matching of words using ration calculation
def match(string, dict):
        high_1 = 0
        high_2 = 0

        # Loop through base dictionary to narrow search
        for key in dict:
                string_ratio = ratio(string, key)
                string_ratio_2 = ratio(string, dict[key])

                if string_ratio == 100:
                        return dict[key]
                elif string_ratio_2 == 100:
                        return dict[key]
                if string_ratio > high_1:
                        high_1 = string_ratio
                        key_string_1 = key
                if string_ratio_2 > high_2:
                        high_2 = string_ratio_2
                        key_string_2 = dict[key]

        if high_1 > high_2:
                return dict[key_string_1]
        else:
                return key_string_2
                

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
                        dict[i] = j
                        
                count += 1
        
        ws.write(1, 4, 100*(correct / (count-1)))
        wb.save('src\main\python\output.xls')   

def contains_multiple_words(s):
        return len(s.split()) > 1