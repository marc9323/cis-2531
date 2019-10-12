"""
Marc D. Holman
CIS 2531 Introduction to Python Programming
10 / 7 / 2019
Lab 6 Part II:
Create a program that reads and displays
the baseball stats written to a file
in part I.
"""

# output formatted contents of file to console
def displayData():
    # get filename, open file to read
    filename = input("Enter the filename for reading player statistics: ")
    playerFile = open(filename, 'r')

    # initialize accumulators
    totalPlayers = 0
    totalGamesPlayed = 0
    totalHomeRuns = 0

    # use format function to print headers
    print(format('Player Name', '30s'), format('Games Played', '15s'), format('Home Runs', '10s'))

    # read data from file and track necessary data (i.e. totalGamesPlayed, totalHomeRuns, 
    # firstAndLastName, totalPlayers)
    for player in playerFile:
        record = player.split(':')
        firstName = record[0]
        lastName = record[1]
        gamesPlayed = int(record[2])
        totalGamesPlayed += gamesPlayed
        homeRuns = int(record[3])
        totalHomeRuns += homeRuns
        batAvg = float(record[4])
        firstAndLastName = firstName + " " + lastName
        
        totalPlayers += 1
        
        # use format string function to output table contents
        # '<' indicates left alignment
        print("{0:<30} {1:<15d} {2:<10d}".format(firstAndLastName, gamesPlayed, homeRuns))

    # close the file
    playerFile.close()

    # calculate the averages
    avgNumGames = (totalGamesPlayed / totalPlayers)
    avgNumHomeRuns = (totalHomeRuns / totalPlayers)

    # output summary statistics
    print("*** Summary Statistics ***")
    print(f"Total number of players: {totalPlayers}")
    print("Average number of games played: {0:.3f}".format(avgNumGames))
    print("Average number of home runs: {0:.3f}".format(avgNumHomeRuns))

# main method
def main():
    displayData()

main()

"""
Sample Run:
Enter the filename for reading player statistics: players.txt
Player Name                    Games Played    Home Runs
Marc Holman                    721             34
Jack  Daniels                  98              32
Donald Trump                   32              18
Zebediah S                     324             18
*** Summary Statistics ***
Total number of players: 4
Average number of games played: 293.750
Average number of home runs: 25.500

Enter the filename for reading player statistics: baseball.txt
Player Name                    Games Played    Home Runs
Marc Holman                    721             321
Zebediah Smith                 890             12
Donald Trump                   445             200
Camel Joe                      891             498
*** Summary Statistics ***
Total number of players: 4
Average number of games played: 736.750
Average number of home runs: 257.750

"""