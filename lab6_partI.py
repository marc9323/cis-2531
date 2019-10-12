"""
Marc D. Holman
CIS 2531 Introduction to Python Programming
10 / 7 / 2019
Lab 6 Part I:
Create a program that asks for the following data from the user:
player first and last name -> strings
games played -> integer
home runs --> integer
batting average --> floating point
Records it in a sequential text file
"""

# gets user input and returns a dictionary
def getInput():
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    numGames = int(input("Number of games played: "))
    homeRuns = int(input("Number of home runs: "))
    batAvg = float(input("Batting average: "))

    data =  {'firstName':firstName,
            'lastName':lastName, 
            'numGames':numGames,
            'homeRuns':homeRuns,
            'batAvg': batAvg}

    return data

# allows the user to enter data and writes it to txt file
def enterData():
    fileName = input("Enter filename for entering player data: ")
    # open file, get reference
    playerFile = open(fileName, 'w')

    numEntries = int(input("Number of Player Entries: "))

    # loop numEntries times, get input, write to file
    # use : as delimiter
    for record in range(numEntries):
        # get user input
        data = getInput()
        # write to file
        playerFile.write(data['firstName']+':')
        playerFile.write(data['lastName']+':')
        playerFile.write(str(data['numGames'])+':')
        playerFile.write(str(data['homeRuns'])+':')
        # add a linebreak for neatness
        playerFile.write(str(data['batAvg'])+'\n')

    # close the file
    print("Data recorded... closing file...")
    playerFile.close()

# main method
def main():
    enterData()

main()

"""
SAMPLE RUN:
Enter filename for entering player data: baseball.txt
Number of Player Entries: 4
Enter first name: Marc
Enter last name: Holman
Number of games played: 721
Number of home runs: 321
Batting average: 84.5
Enter first name: Zebediah
Enter last name: Smith
Number of games played: 890
Number of home runs: 12
Batting average: 12.34
Enter first name: Donald
Enter last name: Trump
Number of games played: 445
Number of home runs: 200
Batting average: 18.9
Enter first name: Camel
Enter last name: Joe
Number of games played: 891
Number of home runs: 498
Batting average: 99.9
Data recorded... closing file...

Sample Generated File:
Marc:Holman:721:321:84.5
Zebediah:Smith:890:12:12.34
Donald:Trump:445:200:18.9
Camel:Joe:891:498:99.9
"""





