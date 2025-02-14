# pcost.py
#


import sys
import csv

def portfolio_cost(filename):
    '''
    Calculates the cost of a portfolio file
    '''
    total_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        ln=2
        for row in rows:
            try:
                total_cost = total_cost + int(row[1]) * float(row[2])
            except ValueError:
                print('Missing data, ignoring line', ln)
            ln +=1
    return total_cost

# Check if the program is called with an extra argument 
# (first argument is __self__) <-- Check this later:
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
