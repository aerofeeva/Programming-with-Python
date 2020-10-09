# grid.py
#
# Uses Turtle Graphics to draw a grid of boxes
# Usage:
#      % python grid.py t edgeLen count
#
# Anastasia Erofeeva
# 09/19/19

import turtle


def draw_grid(t, edgeLen, count):
    """Uses the Turtle t to draw a grid with count number of boxes
       on each side. The length of each box is edgeLen"""
    t.width(5)    # Sets the pen width to 5
    lineLen = edgeLen * count
    draw_lines(t, lineLen, count)
    if count % 2 == 0:  # If count is even, move the Turtle
        t.penup()
        t.bk(lineLen)
        t.pendown()
    t.lt(90)
    draw_lines(t, lineLen, count)


def draw_lines(self, lineLength, count):
    """Uses the Turtle self to draw count number of lines
    of length line"""
    self.fd(lineLength)  # Draws a line before the loop to avoid fencepost problem
    # Moves the Turtle to the start of the next line, then draws the line,
    # alternating between drawing forwards and backwards, count number of times
    for i in range(count):
        self.penup()
        self.rt(90)
        self.fd(lineLength / count)  # edgeLen = lineLength / count
        self.rt(-90)  # A negative right turn is a left turn
        self.pendown()
        if i % 2 == 0:  # If i is even, draw the line backwards
            self.bk(lineLength)
        else:
            self.fd(lineLength)


bob = turtle.Turtle()
draw_grid(bob, 50, 4)  # A 4 x 4 grid made out of boxes with edgeLen 50
bob.hideturtle()

turtle.mainloop()
exit()