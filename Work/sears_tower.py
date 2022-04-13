# sears.py
bill_thickness = 0.11 * 0.001 # 0.11 mm
sears_height = 442 # m
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print (day, num_bills, num_bills * bill_thickness)
    num_bills = num_bills * 2
    day = day +1
    

print ('Number of days:',day)
print ('Number of bills:', num_bills)
print ('Final height:', num_bills * bill_thickness)