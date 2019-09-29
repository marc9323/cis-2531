"""
Marc D. Holman
CIS 2531 Introduction to Python Programming
9 / 25 / 2019
Lab 4: code functions to draw rhombus, hexagon, and pentagon
add to simple_graphics.py module
"""
# import the simple_graphics module, give it an alias
import simple_graphics as sg

# setup a window, 640 x 480
sg.t.setup(640, 480)

def drawShapes():
    # position the turtle and draw each shape
    sg.positionTurtle(-200, 0)
    sg.drawPentagon('red', 50)
    sg.positionTurtle(-100,0)
    sg.drawHexagon('blue', 50)
    sg.positionTurtle(50,0)
    sg.drawRhombus('green', 50, 66)
    
# call drawShapes to get output and sign it with placeText()
sg.placeText('Simple Shapes by Marc D. Holman', 'black', -100, -175)
sg.placeText('Pentagon, Hexagon, and Rhombus', 'black', -100, -150)
drawShapes()

# hold the window
sg.t.done()


