# write stock records

import stock as s

def writeStockRecords():
    numStocks = int(input("Enter number of stocks to write: "))
    filename = input("Enter filename: ")

    stkFile = open(filename, 'w')

    for stk in range(numStocks):
        ticker = input("Enter symbol: ")
        compName= input("Company Name: ")
        ytdPerformance = int(input("YTD percentage change: "))
        closingPrice = float(input("Closing price: "))

        stkFile.write("{0}:{1}:{2}:{3}\n".format(ticker, compName, str(ytdPerformance), str(closingPrice)))

    stkFile.close()
    print('Stock data written. Success.')

def readStockRecords():
    stkCounter = 0
    totalPercent = 0

    filename = input("Filename: ")
    stkFile = open(filename, 'r')

    # column headings 10 30 10 tickr company name ytd
    #print("Ticker Symbol\tCompany Name\tYTD Performance\tClosing Price")

    #f string with constants
    print(f'{s.TICKER:{s.TICKER_WIDTH}s} {s.CMP_NAME:{s.NAME_WIDTH}s} {s.YTD_PERCENT:{s.YTD_WIDTH}s}')

    # regular format
    #print(format('Ticker', '10s'), format('Company Name', '30s'), format('YTD %', '10s'))

    for stk in stkFile:  # reads first record as part of the loop
        record = stk.split(':')
        stkCounter += 1
        totalPercent += int(record[2])
        ticker = record[0]
        compName = record[1]
        ytdPerf = int(record[2])
        #closePrice = float(record[3])
       # print(f'{ticker:{s.TICKER_WIDTH}s} {compName:{s.NAME_WIDTH}s} {ytdPerf:>{s.YTD_WIDTH}d}')

        print(f'{ticker:{s.TICKER_WIDTH}s} {compName:{s.NAME_WIDTH}s} {str(ytdPerf):{s.YTD_WIDTH}s}')

        #print(format('Ticker', '10s'), format('Company Name', '30s'), format('YTD %', '10s'))

        # regular format function
        #print(format(ticker, '10s'), format(compName, '30s'), format(ytdPerf, '<10d'))


# numbers by default are right aligned

        #print("{0}\t\t\t{1}\t\t\t{2}\t\t\t{3}".format(record[0], record[1], record[2], record[3]))


    stkFile.close()

    print("Num stocks read: " + str(stkCounter))
    print("Average YTD is ", format(totalPercent / stkCounter, '.2f'))


readStockRecords()







