"""
Marc D. Holman
9 / 9 / 2019
CIS 2531: Introduction to Python Programming
Lab 3: Pennies For Pay, Exercise 4
"""

# declare variables, start with day one values
total = .01
pay = .01
day = 1

# ask the user for number of days to calculate
numDays = int(input("Number of days to calculate: "))

# output table header along with day one
print("Days", "Pay", "Total", sep="\t")
print(day, "$"+str(pay), "$"+str(total), sep="\t")

# loop through each day, perform calculations, output results
while day < numDays:
    pay *= 2 # double the pay
    day += 1 # increment the days
    total += pay # keep a running total
    # output current row of table
    print(day, "$"+format(pay, '.2f'), "$"+format(total, '.2f'), sep="\t")


"""
SAMPLE OUTPUT:

Number of days to calculate: 12
Days	Pay	Total
1	$0.01	$0.01
2	$0.02	$0.03
3	$0.04	$0.07
4	$0.08	$0.15
5	$0.16	$0.31
6	$0.32	$0.63
7	$0.64	$1.27
8	$1.28	$2.55
9	$2.56	$5.11
10	$5.12	$10.23
11	$10.24	$20.47
12	$20.48	$40.95
13	$40.96	$81.91

"""
