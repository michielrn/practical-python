# pcost.py
#
# Exercise 1.27
# Exercise 1.27: Reading a data file
# Now that you know how to read a file, let’s write a program to perform a simple calculation.

# The columns in portfolio.csv correspond to the stock name, number of shares, 
# and purchase price of a single stock holding. 
# Write a program called pcost.py that opens this file, reads all lines, 
# and calculates how much it cost to purchase all of the shares in the portfolio.

# Hint: to convert a string to an integer, use int(s). 
# To convert a string to a floating point, use float(s).

# Your program should print output such as the following:

# Total cost 44671.15

# Exercise 1.30 
# Take the code you wrote for the pcost.py program in Exercise 1.27 
# and turn it into a function portfolio_cost(filename). 
# This function takes a filename as input, reads the portfolio data in that file, 
# and returns the total cost of the portfolio as a float.



def portfolio_cost(filename):

    total_cost = 0.0
    with open(filename, 'rt') as f:
        next(f)
        ln=2
        for line in f:
            purchase = line.split(',')
            try:
                total_cost = total_cost + int(purchase[1]) * float(purchase[2])
            except ValueError:
                print('Missing data, ignoring line', ln)
            ln +=1
    return total_cost

cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)
