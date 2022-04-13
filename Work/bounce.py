# bounce.py
#
# Exercise 1.5
# A rubber ball is dropped from a height of 100 meters and each time it hits the ground, 
# it bounces back up to 3/5 the height it fell. Write a program bounce.py that 
# prints a table showing the height of the first 10 bounces.

height = 100 # meters
bounce_efficiency = 0.6 # dimensionless

print ("aant\thoogte (m)")

for n in range(11):
    print (n, "\t", height)
    height = round((height * bounce_efficiency), 4)
    