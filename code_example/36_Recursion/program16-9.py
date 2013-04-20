# Draw Sierpinski figure

from turtle import *

def sierpinski(length, depth): 
    if depth > 1: dot()  # mark position to better see recursion
    if depth == 0:       # base case
        stamp() # stamp a triangular shape
    else:
        forward(length)
        sierpinski(length/2, depth-1)  # recursive call
        backward(length)
        left(120)
        forward(length)
        sierpinski(length/2, depth-1)   # recursive call
        backward(length)
        left(120)
        forward(length)
        sierpinski(length/2, depth-1)  # recursive call
        backward(length)
        left(120)

sierpinski(200,6)

