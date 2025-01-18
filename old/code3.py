import turtle

# Setting up the turtle
t = turtle.Turtle()
screen = turtle.Screen()

# Adjust screen size and background color (optional)
screen.setup(width=600, height=400)
screen.bgcolor("lightblue")

# Pen color for the scales
t.pencolor("black")
t.pensize(3)

# Drawing the left pan
t.penup()
t.goto(-100, 50)
t.pendown()
t.forward(200)

# Drawing the right pan
t.penup()
t.goto(100, 50)
t.pendown()
t.forward(200)

# Drawing the base
t.penup()
t.goto(0, -50)
t.pendown()
t.forward(100)
t.left(90)
t.forward(20)

# Holding the screen open
turtle.done()