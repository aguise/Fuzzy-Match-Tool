import argparse
import sys
import csv
import utility

def main():
    for i in sys.argv:
        readCSV = csv.reader(sys.argv, delimiter=',')
        print(readCSV)
        for row in readCSV:
            for column in readCSV:
                print(utility.Ratio(readCSV, "usd"))
    return

main()