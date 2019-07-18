from fuzzywuzzy import fuzz
import csv
import dictionary
import xlwt
import currencies
from xlwt import Workbook

# Simple fucntion for calculating
# ration of similarity between two strings
# by using their levenshstein distance
def ratio (a, b) :
        return fuzz.partial_ratio(a.lower(), b.lower())

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
def match(string, dict, dict_type):
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

        dictionary = find_dict(dict_type)
        dict_1 = dictionary[dict[key_string]]
        dict_2 = dictionary[dict[key_string_2]]

        high = 0
        dict_num = 0

        # Loop through more specific dictionaries to get exact match
        for i, j in zip(dict_1, dict_2):
                string_ratio_1 = ratio(string, i)
                string_ratio_2 = ratio(string, j)

                if string_ratio_1 > string_ratio_2:
                        if string_ratio_1 > high:
                                high = string_ratio_1
                                dict_num = 1
                else:
                        if string_ratio_2 > high:
                                high = string_ratio_2
                                dict_num = 2
        
        if dict_num == 1:
                return dict[key_string]
        else:
                return dict[key_string_2]

#  Outputs raw input and standardized form to excel sheet
def final_output(raw, standard, result):
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
                count += 1

        ws.write(1, 4, 100*(correct / (count-1)))
        wb.save('output.xls')   

def find_dict(dict_type):
        if dict_type == "currency":
                return currencies.currency