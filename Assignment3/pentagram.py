# pentagram.py
#
# Draws a pentagram with a given edge length and pen width
# Usage:
#      % python pentagram.py t edgeLen penWidth
#
# Anastasia Erofeeva
# 09/19/19

import turtle

ANGLE = 144    # Pentagrams have angles of 36 degrees. 180 - 36 = 144 degrees.


def draw_pentagram(t, edgeLen, penWidth):
    """Uses the Turtle t to draw a pentagram with edges
    that are edgeLen long and a line thickness of penWidth"""
    t.width(penWidth)
    for i in range(5):    # Pentagrams have 5 angles, so the loop runs 5 times
        t.fd(edgeLen)
        t.rt(ANGLE)


bob = turtle.Turtle()
draw_pentagram(bob, 300, 10)    # AA pentagram with edgeLen 300, and penWidth 10
bob.hideturtle()

turtle.mainloop()
exit()
