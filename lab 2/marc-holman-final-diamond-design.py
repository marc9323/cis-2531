"""
Marc D. Holman
2 / 3/ 2019
CIS 2531 Introduction To Python
Create a colorful diamond design with turtle graphics 
"""

# import turtle module, set an alias for the turtle
import turtle as t

# setup window, set turtle to max speed
t.setup(640, 480)
t.speed(10)

# set an initial heading of 45 degrees
t.setheading(45)

# create a list of colors
colors = [ 'black', 'blue', 'red', 'green' ]

# creates the squares that comprise our design
def makeDiamond(color):
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.end_fill()

# place text of chosen color at designated x, y position
def placeText(text, color, x, y):
    t.penup()
    t.setposition(x, y)
    t.pencolor(color)
    t.write(text)
    
# loop through the colors and create diamonds 
for i in range(0,4):
    makeDiamond(colors[i])

# sign the design
placeText('a colorful diamond square by Marc D. Holman', 'black', -125, -125)

# hide the turtle for viewing finished product
t.hideturtle()


    
