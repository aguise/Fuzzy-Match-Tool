import argparse
import sys
import csv
import utility
import xlwt
from xlwt import Workbook

def main():

    dict_type = sys.argv[1]
    dict = utility.initialize(dict_type)
    standard_list = []
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')


    file = sys.argv[2]
    file_standards = sys.argv[3]

    # reads csv files from command line
    with open(file, 'r') as csv_file, open(file_standards, 'r') as csv_file_2:
        reader = csv.reader(csv_file)
        reader_2 = csv.reader(csv_file_2)
        
        for row, row_2 in zip(reader, reader_2):
            for i in row:
                string = ''.join(filter(whitelist.__contains__, i))
                standard_list.append(utility.match(string.lower(), dict, dict_type))

        utility.final_output(row, row_2, standard_list)
        
main()