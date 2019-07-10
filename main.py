import argparse
import sys
import csv
import utility
import openpyxl

def main():

    rows = []

    # reads csv files from command line
    readCSV = csv.reader(sys.argv, delimiter=',')
    print(readCSV)
    for row in readCSV:
        rows.append(row)
        
    for row in rows:
        for col in row:
            print(col)
return

main()