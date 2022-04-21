# mortgage.py
#
# Exercise 1.7

### Exercise 1.8: Extra payments

# Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?

# Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of months required.

# When you run the new program, it should report a total payment of `929,965.62` over 342 months.

# principal = 500000
# rate = 0.05
# init_payment = 2684.11
# total_paid = 0.0
# months = 0
# extra_payment = 1000.0
# extra_payment_months = 12

# while principal > 0:
#     payment = init_payment + ((months < extra_payment_months)*extra_payment)
#     principal = principal * (1 + rate / 12) - payment 
#     total_paid = total_paid + payment
#     months = months + 1

# total_paid = round(total_paid,2)
# print('Total paid:', total_paid)
# print('Number of months:', months)

# Code checks out after debugging.

### Exercise 1.9: Making an Extra Payment Calculator

# Modify the program so that extra payment information can be more generally handled.
# Make it so that the user can set these variables:

# ```python
# extra_payment_start_month = 61
# extra_payment_end_month = 108
# extra_payment = 1000
# ```

# Make the program look at these variables and calculate the total paid appropriately.

# How much will Dave pay if he pays an extra $1000/month for 4 years starting after the first
# five years have already been paid?

# principal = 500000
# rate = 0.05
# init_payment = 2684.11
# total_paid = 0.0
# months = 0

# extra_payment = 1000.0
# extra_payment_start_month = 12
# extra_payment_end_month = 108

# while principal > 0:
#     payment = init_payment + (((months >= extra_payment_start_month) and (months < extra_payment_end_month))  * extra_payment)
#     principal = principal * (1 + rate / 12) - payment 
#     total_paid = total_paid + payment
#     months = months + 1

# total_paid = round(total_paid,2)
# print('Total paid:', total_paid)
# print('Number of months:', months)

### Exercise 1.10: Making a table

# Modify the program to print out a table showing the month, total paid so far, and the remaining principal.
# The output should look something like this:

# ```bash
# 1 2684.11 499399.22
# 2 5368.22 498795.94
# 3 8052.33 498190.15
# 4 10736.44 497581.83
# 5 13420.55 496970.98
# ...
# 308 874705.88 3478.83
# 309 877389.99 809.21
# 310 880074.1 -1871.53
# Total paid 880074.1
# Months 310
# ```
principal = 500000
rate = 0.05
init_payment = 2684.11
total_paid = 0.0
months = 0

extra_payment = 1000.0
extra_payment_start_month = 12
extra_payment_end_month = 108

print ("Month\tPaid so far\tRemaining Principal")

while principal > 0:
    payment = init_payment + (((months >= extra_payment_start_month) and (months < extra_payment_end_month))  * extra_payment)
    principal = principal * (1 + rate / 12)
    if payment > principal:
        payment = principal
    principal = principal - payment
    total_paid = total_paid + payment
    months = months + 1
    print(f"Month: {months}\tTotal paid: {round(total_paid,2)}\tRemaining principal: {round(principal,2)}")

total_paid = round(total_paid,2)
print('Total paid:', total_paid)
print('Number of months:', months)

# Exercise 1.11: Bonus
# While you’re at it, fix the program to correct for the overpayment that occurs in the last month.

# Modify the mortgage.py program from Exercise 1.10 to create its 
# output using f-strings. Try to make it so that output is nicely aligned.