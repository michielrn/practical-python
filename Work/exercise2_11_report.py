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
# from pprint import pprint #(only for printing section)


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

def make_report(portfolio, prices):
    rows = []
    for asset in portfolio:
        rows.append(
                (asset['name'], 
                    asset['shares'], 
                    prices[asset['name']], 
                    (prices[asset['name']]-asset['price'])
                    )
        )
    return rows


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
report = make_report(portfolio, prices)


# Print the report header

header = ''
separator = ''
column_names = ['Name', 'Shares', 'Price', 'Change']
for name in column_names:
    header = header +(f'{name:>10s}')
    header = header + (' ')
    separator = separator + ('---------- ')
print('\n\n\n', header,'\n', separator)

# for r in report:
#     print(f' {r[0]:>10s} {r[1]:>10n} {r[2]:>10.2f} {r[3]:>10.2f}')

for name, shares, price, change in report:
    print(f' {name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

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