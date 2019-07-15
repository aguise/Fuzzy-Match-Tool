import argparse
import sys
import csv
import utility
import openpyxl

def main():

    dict = utility.initialize(sys.argv[1])
    standard_list = []
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')


    file = sys.argv[2]

    # reads csv files from command line
    with open(file, 'r') as csvFile:
        reader = csv.reader(csvFile)
    
        for row in reader:
            for i in row:
                string = ''.join(filter(whitelist.__contains__, i))
                utility.match(string, dict)
        

main()
