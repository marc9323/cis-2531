"""
Marc D. Holman
CIS 2531 Introduction To Python Programming
Lab 4
Check a range of numbers for Primes
"""
# check for prime, return Boolean 
def isPrime(num):
    # a prime number is a positive integer that has no positive integer divisors
    # other than 1 and itself
    # 1 is a 'special case': ( http://mathworld.wolfram.com/PrimeNumber.html )
    if num == 1: return False
    elif num == 2: return True
    else:
        # 2 and up
        for i in range(2, num):
            if num % i == 0: return False
        return True

# get upper limit
upperLimit = int(input("Enter the upper range to check for Prime Numbers: "))

def checkRangeForPrimes():
    # output, use f string
    print(f"The Prime Numbers in the range of 1 to {upperLimit} are:")

    # initialize the total
    total = 0
    
    # loop through range, check for primes
    for i in range(1, upperLimit+1):
        if isPrime(i):
            total += 1
            # output primes to same row, with space between them
            print(i, " ", end="") 
    
    # use a f string for output
    print(f"\nThis is a total of {total} Prime Numbers.")

# execute
checkRangeForPrimes()

"""
SAMPLE RUN:

Enter the upper range to check for Prime Numbers: 11
The Prime Numbers in the range of 1 to 11 are:
2  3  5  7  11
This is a total of 5 Prime Numbers.

Enter the upper range to check for Prime Numbers: 59
The Prime Numbers in the range of 1 to 59 are:
2  3  5  7  11  13  17  19  23  29  31  37  41  43  47  53  59
This is a total of 17 Prime Numbers.

"""

