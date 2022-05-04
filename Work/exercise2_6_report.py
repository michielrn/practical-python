# read_prices(filename)
#
# Exercise 2.6: A list of dictionaries
# Includes 2.7 Finding out if you can retire
# Take the function you wrote in Exercise 2.4 and modify 
# to represent each stock in the portfolio with a dictionary 
# instead of a tuple. In this dictionary use the 
# field names of "name", "shares", and "price" 
# to represent the different columns in the input file.

import sys
import csv
from pprint import pprint


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

# Write a function read_prices(filename) that 
# reads a set of prices such as this into a dictionary 
# where the keys of the dictionary are the stock names 
# and the values in the dictionary are the stock prices.

# To do this, start with an empty dictionary 
# and start inserting values into it just as you did above. 
# However, you are reading the values from a file now.

# We’ll use this data structure to quickly lookup the price of a given stock name.
def read_prices(filename):
    '''
    Read prices from a file into a dictionary
    The file has no headers
    structured 'name', price [str, float]
    '''
    prices_ = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        line_number = 1
        err_count = 0
        for row in rows:
            try:
                prices_[row[0]] = float(row[1])
            except IndexError:
                print(f'\tMissing data, ignoring line {line_number}')
                err_count += 1

            line_number += 1
    print(f'\tReading completed. {err_count} errors.')
    return prices_



# Check if the program is called with an extra argument 
# (first argument is __self__) <-- Check this later:
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

# Generate a growth report
# Use original portfolio and prices
# to calculate the gain and loss of each stoch
# and the total capital gains

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

start_total_value = 0.0
present_total_value = 0.0
capital_gains = 0.0

print('name\tshares\tbuy price\tCurrent value')

for holding in portfolio:
    # Calculate portfolio elements delta for each holding
    invested = holding['shares'] * holding['price']
    present_value = holding['shares'] * prices[holding['name']]
    capital_delta = present_value - invested
    
    # Update totals
    start_total_value += invested
    capital_gains += capital_delta
    present_total_value += present_value
    print(holding['name'], '\t', holding['shares'], '\t', round(invested, 2), '\t', round(capital_delta,2))

print(f'Start value\t{start_total_value}')
print(f'Present value\t{present_value}')
print(f'Capital gains\t{capital_gains}')

# These lines are from the interactive session.
# Comment out if used only for the function.

### start comment/uncomment block
###
# portfolio = read_portfolio('Data/portfolio.csv')
# pprint(portfolio)

# total = 0.0
# for s in portfolio:
#     total += portfolio['shares']* portfolio['price']

# print(total)
###
# ### End comment/uncomment block