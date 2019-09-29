import simple_graphics as sg

sg.t.speed(10)

# get input 
# return start x, start y, number of squares, and side length
def getInput():
    x = int(input("Enter the starting x position: "))
    y = int(input("Enter the starting y position: "))
    numSquares = int(input("Enter the number of squares: "))
    sideLength = int(input("Enter the side length: "))
    #offset = int(input("Enter an offset ( 'Enter' defaults to 5 ):"))

    return x, y, numSquares, sideLength

# main function, uses input values to draw concentric squares
def main():
    x, y, numSquares, sideLength = getInput()

    # offset defaults to 5
    sg.drawConcentricSquares(x, y, numSquares, sideLength)

    sg.t.done()
       

main()


