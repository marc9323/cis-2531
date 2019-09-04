"""
Marc D. Holman
9 / 2 / 2019
CIS 2531 Introduction To Python Programming
User inputs desired cookie quantity and the number of
cups of each ingredient needed is displayed
"""
 
# named constants
CUPS_SUGAR = 1.5
CUPS_BUTTER = 1
CUPS_FLOUR = 2.75
BASE_QUANTITY = 48

# get cookie quantity, cast as float
quantity = float(input("How many cookies would you like to make? "))

# calculate cups flour, butter, sugar
requiredSugar = ( CUPS_SUGAR * quantity) / BASE_QUANTITY
requiredButter = ( CUPS_BUTTER * quantity ) / BASE_QUANTITY
requiredFlour = ( CUPS_FLOUR * quantity ) / BASE_QUANTITY

# output the results - cups required for each ingredient
# to 1 digit of precision after floating point decimal
print("For {0} cookies, you will require:".format(quantity))
print(format(requiredSugar, '.1f'), "cups of sugar")
print(format(requiredButter, '.1f'), "cups of butter")
print(format(requiredFlour, '.1f'), "cups of flour")

"""
SAMPLE RUN:
How many cookies would you like to make? 345
For 345.0 cookies, you will require:
10.8 cups of sugar
7.2 cups of butter
19.8 cups of flour
"""
