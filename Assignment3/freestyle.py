# freestyle.py
#
# Uses Turtle Graphics to draw the Olympic flag on a blue background
# Usage:
#      % python freestyle.py t radius penWidth
#
# Anastasia Erofeeva
# 09/19/19
#
# I used the following sources to see how to change the screen's background color:
# https://docs.python.org/3/library/turtle.html#turtle.bgcolor
# https://stackoverflow.com/questions/5813135/is-there-a-way-can-set-the-background-color-for-python-turtle


import turtle


def draw_olympic_flag(t, radius, penWidth):
    """Uses the Turtle t to draw the Olympic flag.
    The size of the rings is determined by the given radius.
    The pen width is determined by th given penWidth."""
    t.width(penWidth)
    draw_box(t, radius)
    t.penup()
    t.goto(radius * -3.3, radius * - 3.5)    # Moves Turtle to a more or less correct location, found by trial and error
    t.pendown()
    # Draws 5 circles of different colors
    for i in range(5):
        change_color(t, i)
        if i == 3:    # After the third circle, the Turtle needs to be moved down to the second row
            t.penup()
            t.bk(radius * 5.6)    # The amount the Turtle should move was found by trial and error
            t.rt(90)
            t.fd(4 * radius / 3)
            t.lt(90)
            t.pendown()
        draw_circle(t, radius)


def draw_box(self, radius):
    """Uses the Turtle self to draw a white rectangle.
    The dimensions of the rectangle are based on the radius of the circles."""
    self.fillcolor('white')
    self.begin_fill()
    self.bk(radius * 6)    # Moves the Turtle backwards before drawing the rectangle
    # Draws a rectangle by turning the turtle and then drawing lines
    for i in range(2):
        self.rt(90)
        self.fd(radius * 6)
        self.rt(90)
        self.bk(radius * 10)
    self.end_fill()


def draw_circle(self, radius):
    """Uses the Turtle self to draw a circle with the given radius.
    Then moves the Turtle to prepare for drawing the next circle."""
    self.circle(radius)
    self.penup()
    self.fd(9 * radius / 4)    # The amount the Turtle should move was found by trial and error
    self.pendown()


def change_color(self, count):
    """Uses the Turtle self to change the pen color count number of times.
    Count is updated in the for loop of the draw_olympic_flag function."""
    if count == 0:
        self.pencolor('blue')
    elif count == 1:
        self.pencolor('black')
    elif count == 2:
        self.pencolor('red')
    elif count == 3:
        self.pencolor('gold')
    else:
        self.pencolor('green')


bob = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('blue')    # Changes the screen's background color
draw_olympic_flag(bob, 50, 10)    # Olympic flag with rings of radius 50 and penWidth of 10
bob.hideturtle()

turtle.mainloop()
exit()
