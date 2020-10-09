# hopscotch.py
#
# Draws a schoolyard hopscotch court with a given edge length and pen width
# Usage:
#      % python hopscotch.py t edgeLen penWidth
#
# Anastasia Erofeeva
# 09/19/19

import turtle


def hopscotch_court(t, edgeLen, penWidth):
    """Uses the Turtle t to draw a hopscotch court made out of squares
     with edges that are edgeLen long and a line thickness of penWidth"""
    t.width(penWidth)
    # Repeatedly draws a square and moves to the correct location
    # before drawing the next square
    for i in range(4):
        # For iterations 0, 1, and 3, a square is drawn before moving the Turtle
        if i <= 1 or i == 3:
            square(t, edgeLen)
        t.penup()
        t.bk(edgeLen / 2)
        turn(t, -90, 90, edgeLen)  # lt(-90) is a right turn, lt(90) is a left turn
        t.fd(edgeLen)
        t.pendown()
        square(t, edgeLen)
        # For iterations 0 and 2, the Turtle needs to be moved back after drawing the square
        if i == 0 or i == 2:
            t.penup()
            t.bk(edgeLen)
            t.pendown()
        # For iteration 3, two squares are drawn to finish the hopscotch court
        elif i == 3:
            for j in range(2):  # Draws the last two squares
                turn(t, -90, 90, edgeLen)
                square(t, edgeLen)


def square(self, size):
    """Draws a square of the given size, using 4 left turns and 4 lines"""
    for i in range(4):
        self.lt(90)
        self.fd(size)


def turn(self, angle1, angle2, size):
    """Turns the Turtle (self) angle1 degrees to the left,
    moves the Turtle in that direction for one edge length (size),
    then turns the Turtle angle2 degrees to the left"""
    self.penup()
    self.lt(angle1)
    self.fd(size)
    self.lt(angle2)
    self.pendown()


bob = turtle.Turtle()
hopscotch_court(bob, 40, 5)    # A hopscotch court made out of boxes with edgeLen 40 and penWidth 5
bob.hideturtle()

turtle.mainloop()
exit()
