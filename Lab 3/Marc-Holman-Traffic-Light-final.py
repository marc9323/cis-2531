"""
Marc D. Holman
CIS 2531: Introduction To Python Programming
9 / 9 / 2019
Lab 3: Create a Traffic Light Design Using Nested Loops
"""

# import turtle module, set alias
import turtle as t;

# create a tuple of colors, so drawn in order
colors = ( 'green', 'yellow', 'red' )

# set a starting Y position to approximately center the design
positionY = -150

# setup window
t.setup(640, 480)

# set the turtle speed
t.speed(10)

# nested loop structure to create traffic light
def makeTrafficLight(positionY):
    for color in colors: # colors
        t.penup()
        positionY += 100
        t.setposition(0, positionY)
        # call begin_fill
        t.pencolor(color)
        t.fillcolor(color)
        t.begin_fill()
        for side in range(4): # squares
            t.pendown()
            t.forward(50)
            t.right(90)
        t.end_fill()

# place text of chosen color at designated x, y position
def placeText(text, color, x, y):
    t.penup()
    t.setposition(x, y)
    t.pencolor(color)
    t.write(text)

# call makeTrafficLight to draw design
makeTrafficLight(positionY)

# sign it
placeText("A traffic light design by Marc Holman", 'black', -100, -175)

# hide the turtle and hold the window
t.hideturtle()
t.done()
        
        
        
    
