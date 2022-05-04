# report.py
#
# Exercise 2.5: A list of dictionaries
# Take the function you wrote in Exercise 2.4 and modify 
# to represent each stock in the portfolio with a dictionary 
# instead of a tuple. In this dictionary use the 
# field names of "name", "shares", and "price" 
# to represent the different columns in the input file.

import sys
import csv

def read_portfolio(filename):
    '''
    Read a portfolio from a file into a list of tuples
    '''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        line_number = 2

        for row in rows:
            try:
                holding = {headers[0]: row[0], 
                            headers[1]: int(row[1]), 
                            headers[2]: float(row[2])}
                portfolio.append(holding)
            except ValueError:
                print(f'Missing data, ignoring line {line_number}')
            line_number += 1

    return portfolio

# Check if the program is called with an extra argument 
# (first argument is __self__) <-- Check this later:
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

