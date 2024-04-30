import turtle

# Setting up the turtle
t = turtle.Turtle()
screen = turtle.Screen()

# Adjust screen size and background color (optional)
screen.setup(width=400, height=400)
screen.bgcolor("lightgreen")

# Pen color for the hand
t.pencolor("skyblue")
t.pensize(3)

# Drawing the arm
t.penup()
t.goto(0, -100)
t.pendown()
t.forward(80)

# Drawing the fingers
t.penup()
t.goto(40, -50)
t.pendown()
t.forward(20)
t.left(60)
t.forward(20)
t.left(60)
t.forward(20)
t.left(60)
t.forward(20)

# Holding the screen open
turtle.done()