'''
Author:
Date:   10/03/2019
Prog:   ReadWriteCounts.py
Descr:
In class exercise to demonstrate writing/reading numeric data to/from file.
'''


def checkNegCount(valToCheck):
    if valToCheck < 0:
        raise ValueError('Error:  no negative counts')

# write numeric data to file
def writeCounts():
    # prompt for the filename
    fileName = input('Enter the name of the file to create: ')
    # open file
    try:
        outFile = open(fileName, 'w')
        countToday = int(input('How many students in class today? '))
        checkNegCount(countToday)
        countYesterday = int(input('How many students in class yesterday? '))
        checkNegCount(countYesterday)
    except FileNotFoundError:
        print("File Not Found Error - Unable to open file for output.")
    except ValueError as err:
        print('Error: ', err)
    except:
        print('ERROR - some error happened')
    else:
        # process the file with counts read from user
        outFile.write(str(countToday) + '\n')
        outFile.write(str(countYesterday) + '\n')
        # close file
        outFile.close()
        # let user know writing is finished
        print('Student counts written to ', fileName)
    finally:  # runs regardless
        print("End of program")
        outFile.close()

# read numeric data from file
def readCounts():
    # prompt for the filename
    fileName = input('Enter the name of the file to open: ')
    # open file
    inFile = open(fileName, 'r')
    # process the file with counts read from file
    countToday = int(inFile.readline())
    countYesterday = int(inFile.readline())
    # close file
    inFile.close()
    # display total number of counts
    print('Total number of students today and yesterday = ', countToday + countYesterday)

def main():
    writeCounts()
    #readCounts()

# start program
main()