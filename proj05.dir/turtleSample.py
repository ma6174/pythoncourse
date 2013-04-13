## sample using turtle to draw some figures

## The basic concept behind the turtle is the pen. The pen is either up of down.
## When down, the turtle draws as it moves around the Cartesian graph.

## Some methods that you might find useful in the project are:
##
##
## turtle.up(),turtle.down(): Set the pen state to be up (not drawing) or
## down (drawing)
##
## turtle.right(degrees), turtle.left(degrees): Turn the direction that the
## turtle is facing. The amount of turn is indicated in degrees.
##
## turtle.forward(distance), turtle.backward(distance): Move the turtle forward
## or backward the amount of distance indicated. Depends on the direction
## the turtle is facing.  Draws a line if the pen is down, not if the pen is up.
##
## turtle.goto(x,y): Moves the turtle to a specified point, drawing a line along
## the way if the pen is down, and not drawing if the pen is up. Note: The
## turtle always starts at the point (0,0). The goto method moves to the
## indicated x,y coordinates.
##
## turtle.color(r,g,b): The color method sets the color that the pen will hold
## for all drawing until the color is changed. It takes three arguments,
## each a floating-point number between 0.0-1.0.  The first is the amount of red,
## the second, the amount of green and the third the amount of blue.
##
## turtle.cirle(radius): draw a circle of the indicated radius. The
## turtle starts its drawing at the bottom of the circle.
##
## turtle.write(string): Write a string starting at the present turtle point.
##
## turtle.begin_fill(), turtle.end_fill(): Use turtle.begin_fill() before you
## start drawing a figure. Draw the figure, then execute turtle.end_fill().
## The figure drawn between the two fill commands will be filled with the
## present color setting.
##
## turtle.hide(): Makes the turtle invisible.
##
## turtle.bye(): Close the turtle drawing window.
##
## The first thing you should do, even BEFORE running this program, is try out
## some of the commands by just typing them in the Python shell  window. 
## (Remember to first import turtle.)  You can get a much better feel for how turtle
## works by just trying it.


import turtle
import time
import random


# let's start up a Turtle Graphics window with a red turtle (pen)
turtle.color(1,0,0)

# prompt before starting to draw
print("Look for the Python Turtle Graphics window")
print("Position it and the Python Shell window side by side.")
input("Then press `Enter' to continue ...")

# put it down so all movement will show as a (red) line (until we change colors)
turtle.down()
# move forward by 100 (in direction that turtle points in, initially (0,1)
turtle.forward(100)
# rotate direction of turtle by 120 degrees
turtle.right(120)
# change the color to green
turtle.color(0,1,0)
# move forward by 100 (in direction that turtle points in, initially (0,1)
turtle.forward(100)
# rotate direction of turtle by 120 degrees
turtle.right(120)
# change the color to blue
turtle.color(0,0,1)
# move forward by 100 (in direction that turtle points in, initially (0,1)
turtle.forward(100)
# rotate direction of turtle back to its start rotation
turtle.right(120)

# to go to a new location without drawing any line
turtle.up()
turtle.goto(0, 50)

# change the pen color to a random color
turtle.color(random.random(),random.random(), random.random())
# lower the pen
turtle.down()

# this time, we'll draw a filled triangle going up
turtle.begin_fill()
turtle.forward(100)
turtle.right(-120)
turtle.forward(100)
turtle.right(-120)
turtle.forward(100)
turtle.end_fill()



def draw_rectangle(x, y, w, h, pen, color):
    """draw a rectangle"""
    pen.fillcolor(color)
    pen.setheading(0)
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.begin_fill()
    pen.goto(x+w,y)
    pen.goto(x+w,y+h)
    pen.goto(x,y+h)
    pen.goto(x,y)
    pen.end_fill()
    
draw_rectangle(-100, 0, 50, 80, turtle, 'green')
    
turtle.hideturtle()
    

# let's pause for 5 seconds
time.sleep(5)

turtle.bye()







        
