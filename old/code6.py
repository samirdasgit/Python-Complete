import turtle

# Create the screen and turtle objects
screen = turtle.Screen()
pen = turtle.Turtle()

# Set speed and pen properties
pen.speed(1)
pen.pensize(3)

# Define colors for each side
colors = ["red", "blue", "green", "yellow"]

# Loop to draw the square with color change
for i in range(4):
    pen.pencolor(colors[i])
    pen.forward(100)
    pen.right(90)

# Keep the window open
screen.exitonclick()