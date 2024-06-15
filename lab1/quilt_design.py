"""
file: quilt_design.py
description: designing blocks for a quilt.
language: python3
author: Mariam Abidi, ma6267@rit.edu

"""
import turtle

# Setup the window size
turtle.setup(1000, 500)
turtle.speed(10)


""" 
This function draws the whole border with the help of the rectangles drawn in
 the border_rectangles function. 
"""


def border():
    turtle.pendown()
    turtle.left(90)
    border_rectangles()
    turtle.left(90)
    border_rectangles()
    turtle.left(90)
    border_rectangles()


""" 
This function draws rectangles for the main border to build on it. 
"""


def border_rectangles():
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(100)
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)


""" 
The border drawn for the first block in the middle
"""


def first_border():
    border_rectangles()
    border()
    first_pattern()


""" 
This function draws a square for the first to build on it.
"""


def square():
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.end_fill()


""" 
This function is used to draw the whole first pattern
"""


def first_pattern():
    turtle.fillcolor("blue")
    turtle.penup()
    turtle.forward(20)
    square()

    turtle.pendown()
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()

    # A for loop to call the triangles four times.
    for _ in range(4):
        turtle.left(90)
        triangles()
        turtle.right(90)
        turtle.forward(40)

    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(240)
    turtle.pendown()


""" 
This function draws the triangles require for the second design
"""


def triangles():
    # Draws the pink triangles
    turtle.fillcolor("pink")
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(135)
    turtle.forward(56)
    turtle.right(135)
    turtle.forward(40)
    turtle.right(135)
    turtle.forward(57)
    turtle.right(45)
    turtle.end_fill()

    # Draws the red triangles
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(40)
    turtle.right(135)
    turtle.forward(28)
    turtle.right(90)
    turtle.forward(28)
    turtle.end_fill()

    turtle.right(45)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)


""" 
This function draws the whole border for the second block which on the left. 
"""


def second_border():
    border_rectangles()
    border()
    second_pattern()


""" 
This function draws the second pattern for the quilt.
"""


def second_pattern():
    turtle.pendown()
    turtle.right(90)
    turtle.penup()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)

    # The purple square is drawn for the second design
    turtle.fillcolor("purple")
    turtle.begin_fill()
    for _ in range(4):
        turtle.pendown()
        turtle.right(90)
        turtle.forward(60)
    turtle.end_fill()

    turtle.penup()
    turtle.right(180)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.right(180)
    right_triangles()
    turtle.penup()
    turtle.forward(520)


""" 
This function draws the green triangles which overlap on the purple square in
the second design. 
"""


def right_triangles():
    # A for loop to draw a green triangle four times.
    for _ in range(4):
        turtle.fillcolor("green")
        turtle.begin_fill()
        turtle.forward(60)
        turtle.left(135)
        turtle.forward(42.42)
        turtle.left(90)
        turtle.forward(42.42)
        turtle.right(135)
        turtle.end_fill()


""" 
This function draws the whole border for the third block on the right. 
"""


def third_border():
    border_rectangles()
    border()
    third_pattern()


""" 
This function draws the pattern inside the third block. 
"""


def third_pattern():
    turtle.penup()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)

    # A big dark blue square is drawn
    turtle.fillcolor("dark blue")
    turtle.begin_fill()

    for _ in range(4):
        turtle.pendown()
        turtle.left(90)
        turtle.forward(80)
    turtle.end_fill()

    # The green slope is drawn inside the blue square.
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.right(180)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.end_fill()

    turtle.right(90)
    turtle.forward(15)

    # The white slope is drawn inside the blue square.
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.right(180)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.end_fill()

    turtle.right(90)
    turtle.forward(15)

    # The brown slope is drawn inside the blue square.
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.right(180)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.end_fill()

    turtle.right(90)
    turtle.forward(15)

    # The yellow slope is drawn inside the blue square.
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.right(180)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.end_fill()


if __name__ == '__main__':
    first_border()
    second_border()
    third_border()
    turtle.mainloop()
