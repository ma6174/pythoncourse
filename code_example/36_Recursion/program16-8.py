# Breadth-first tree

from turtle import *

def branch(length, level):
    if level <= 0:              # base case
        return
    forward(length)
    left(45)
    branch(0.6*length, level-1) # recursive case
    right(90)
    branch(0.6*length, level-1) # recursive case
    left(45)
    backward(length)
    return

# turn to get started
left(90)
branch(100,5)
