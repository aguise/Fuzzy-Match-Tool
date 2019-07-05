import argparse
import sys
import csv
import utility
import openpyxl

def main():
    for i in sys.argv:

        # reads csv files from command line
        readCSV = csv.reader(sys.argv, delimiter=',')
        print(readCSV)
        for row in readCSV:
            for column in readCSV:

                # prints the ratio of similarity for each word in csv file
                print(utility.Ratio(readCSV, "usd"))
    return

main()