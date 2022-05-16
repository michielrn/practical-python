#report.py

import sys
import csv
# from pprint import pprint #(only for printing section)


def read_portfolio(filename):
    '''
    Reads a portfolio from a CSV file 
    Takes filename as argument
    First row gives field names for dict entries
    Returns a list of dictionaries 
        with 'name', 'shares' and 'price' as keys
    
    '''
    print('\n\nReading portfolio...')
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        err_count = 0
        
        for rowno, row in enumerate(rows, start = 1):
            record = dict(zip(headers, row))
            try:
                holding = {'name': record['name'], 
                            'shares': int(record['shares']), 
                            'price': float(record['price'])}
                portfolio.append(holding)
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
                err_count+=1
            
    print(f'\tReading completed. {err_count} errors.')
    return portfolio


def read_prices(filename):
    '''
    Read prices from a CSV file into a dictionary
    with structure {'name0': price0,
                    'name1': price1,
                    ...}
    The file has no headers
    structured 'name', price [str, float]
    '''
    print('\n\nReading prices..')
    prices_ = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        
        err_count = 0
        for rowno, row in enumerate(rows, start=1):
            try:
                prices_[row[0]] = float(row[1])
            except IndexError:
                print(f'Row {rowno}: Bad row: {row}')
                err_count += 1

    print(f'\tReading completed. {err_count} errors.')
    return prices_

def make_report(portfolio, prices):
    rows = []
    for asset in portfolio:
        rows.append(
                (asset['name'], 
                    asset['shares'], 
                    '$'+str(prices[asset['name']]), 
                    (prices[asset['name']]-asset['price'])
                    )
        )
    return rows


# Check if the program is called with an extra argument 
# (first argument is __self__) <-- Check this later:
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

# Generate a growth report
# Use original portfolio and prices
# to calculate the gain and loss of each stock
# and the total capital gains

portfolio = read_portfolio('Data/portfoliodate.csv')
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
    print(f' {name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')

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