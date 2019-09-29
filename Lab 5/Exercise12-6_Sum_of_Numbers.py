"""
Marc D. Holman
CIS 2531 Introduction to Python Programming
9 / 28 / 2019
Lab 5:  Chapter 12, Exercise 6
accept an integer argument and return the sum of all
the integers from 1 up to the number passed.
"""

# sum integers from 1 to number passed - recursively
def recursiveSum(n):
    if n <= 1:  # base case
        return n
    else:  # recursive case
        return n + recursiveSum(n - 1)

# get an integer value from the user
def getInput():
    return int(input("Enter an integer value or 0 to quit: "))

# loop to get user input, sum recursively, and output sum
def main():
    n = getInput()

    while n != 0:
        print("The sum of 1 - {0} is {1:,d}".format(n, recursiveSum(n)))
        n = getInput()

    print("Exiting program...")

# call main program
main()

"""
SAMPLE RUN:

Enter an integer value or 0 to quit: 50
The sum of 1 - 50 is 1,275
Enter an integer value or 0 to quit: 2
The sum of 1 - 2 is 3
Enter an integer value or 0 to quit: 3
The sum of 1 - 3 is 6
Enter an integer value or 0 to quit: 0
Exiting program...

"""