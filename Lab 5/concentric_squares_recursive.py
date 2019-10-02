"""
Marc D. Holman
CIS 2531 - Introduction to Python Programming
10 / 2 / 2019
Lab 5:  Draw Concentric Squares using recursive function
"""

import simple_graphics as sg

sg.t.speed(10)

# get input 
# return start x, start y, number of squares, and side length
def getInput():
    x = int(input("Enter the starting x position: "))
    y = int(input("Enter the starting y position: "))
    numSquares = int(input("Enter the number of squares: "))
    sideLength = int(input("Enter the side length: "))
    # use default offset

    return x, y, numSquares, sideLength

# main function, uses input values to draw concentric squares
def main():
    # get input
    x, y, numSquares, sideLength = getInput()

    # offset defaults to 5
    sg.drawConcentricSquares(x, y, numSquares, sideLength)

    sg.t.done()
       

main()


