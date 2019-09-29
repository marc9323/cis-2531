"""
Marc D. Holman
CIS 2531 Introduction To Python
9 / 22 / 19
Exercise 19:  Calculate an account's future value
"""

# user enters presentValue, interestRate, numMonths
presentValue = float(input("Enter the present value of the account in dollars: "))
interestRate = float(input("Enter the monthly interest rate as a percentage (i.e. .65): "))
numMonths = float(input("Enter the number of months: "))

# use the formula to calculate interest
def calculateInterest():
    futureValue = presentValue * ((1 + interestRate / 100) ** numMonths)
    return futureValue

# calculate annual interest rate
def calculateAnnualInterestRate(interestRate):
    return interestRate * 12

# get annual interest rate and call calculateInterest
annualInterestRate = calculateAnnualInterestRate(interestRate)
futureValue = calculateInterest()

# format output
print("The information for your account is: ")
print("Present Value: ${0:.2f}".format(presentValue))
print("Annual Interest Rate {0:.2f}%".format(annualInterestRate))
print("After {0:.2f} months the value of your account will be: ${1:.2f}".format(numMonths, futureValue))

"""
SAMPLE RUN:

Enter the present value of the account in dollars: 5000
Enter the monthly interest rate as a percentage: .65
Enter the number of months: 48
The information for your account is:
Present Value: $5000.00
Annual Interest Rate 7.80%
After 48.00 months the value of your account will be: $6823.88

Enter the present value of the account in dollars: 1000
Enter the monthly interest rate as a percentage: .65
Enter the number of months: 12.5
The information for your account is:
Present Value: $1000.00
Annual Interest Rate 7.80%
After 12.50 months the value of your account will be: $1084.36

"""