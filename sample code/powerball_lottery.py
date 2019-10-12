# 5 random tween 1- 29
# 1 random powerball number between 1 and 9

# POWERBALL PLAY
import random

# CONSTANTS
LOTTERY_NUMS = 6
PBALL_INDEX = 5
MIN_NUM = 1
MAX_LNUM = 29
MAX_PNUM = 29
JACKPOT = 1
WIN = 2
NO_WIN = 3

# return list of numbers
def generateLotteryNums():
    number = []
    
    for x in range(5):
        number.append(random.randint(1, 29))

    return number
    
def generateNumbers():
    lotteryList = [0] * LOTTERY_NUMS
    for i in range(PBALL_INDEX):
        lotteryList[i] = random.randint(MIN_NUM, MAX_LNUM)

    lotteryList[PBALL_INDEX] = random.randint(MIN_NUM, MAX_PNUM)

    return lotteryList

def checkRange(num, min, max):
    # print("check")
    if num < min or num > max:
        raise ValueError

def getUserNums():
    numbers = []
    for x in range(PBALL_INDEX):
        unum = int(input(f"Enter number tween {MIN_NUM} and {MAX_LNUM}: "))
        checkRange(unum, MIN_NUM, MAX_LNUM)
        numbers.append(unum)
    print(numbers)

    # get powerball number
    pbnum = int(input(f"Enter Powerball number tween {MIN_NUM} and {MAX_LNUM}:"))
    numbers.append(pbnum)
    return numbers

    
def display(numbers):
    print('Lottery numbers: ', end=' ')
    for i in range(PBALL_INDEX):
        print(numbers[i], end= ' ')
    print('\nPowerball #: ', numbers[PBALL_INDEX])
    # lotteryNumbers = numbers[0:len(numbers) - 1]

    # print('Lottery Numbers: ', end=' ')
    # for num in lotteryNumbers:
    #     print

def determineWinLevel(pball, unums):
    pballMatch = pball[PBALL_INDEX] == unums[PBALL_INDEX]
    # create tuples for pball and unums
    winTuple = tuple(pball[0:PBALL_INDEX])
    userTuple = tuple(unums[0:PBALL_INDEX])
    # track matches
    numMatches = 0
    # check for matches
    for n in winTuple:
        if n in userTuple:
            numMatches += 1

    # determine winning status
    if numMatches == len(winTuple) and pballMatch:
        return JACKPOT
    elif pballMatch:
        return WIN
    else:
        return NO_WIN

def main():
    lottery = generateNumbers()
    # display(lottery)
    # get user input
    userNumbers = getUserNums()
    display(lottery)
    winLevel = determineWinLevel(lottery, userNumbers)
    if winLevel == JACKPOT:
        print('Awesome')
    elif winLevel == WIN:
        print('Not Bad')
    else:
        print("Too bad")
   

    #numbers = lottery[0:len(lottery) - 1]

main()

# starting out with programming logic and design.  Persimmons, fifth edition