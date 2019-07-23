import argparse
import sys
import csv
import utility
import xlwt
from xlwt import Workbook
import pickle

def main():

    dict_type = sys.argv[1]
    filename = 'dictionaries\\' + dict_type + '_dictionary'
    dict = utility.initialize_dict(dict_type, filename)
    results = []
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
                results.append(utility.match(string.lower(), dict))

        utility.final_output(row, row_2, results, dict)

    outfile = open(filename, 'wb')

    pickle.dump(dict, outfile)
    outfile.close()


main()