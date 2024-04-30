import turtle

# Create the screen and turtle objects
screen = turtle.Screen()
pen = turtle.Turtle()

# Set speed and pen properties
pen.speed(0)
pen.pensize(2)

# Define starting position and variables
distance = 5
angle = 0

while distance < 100:
    pen.forward(distance)
    pen.right(angle)

    # Update distance and angle for spiral effect
    distance += 5
    angle += 0.1

# Keep the window open
screen.exitonclick()
