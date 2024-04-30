import turtle
import random

# Create the screen and turtle objects
screen = turtle.Screen()
ball = turtle.Turtle()

# Set ball properties
ball.speed(0)
ball.shape("circle")

# Define starting position and movement direction
ball.penup()
ball.goto(0, 100)
ball.pendown()
ball.dy = -0.5

while True:
    # Update ball position
    ball.sety(ball.ycor() + ball.dy)

    # Check for bouncing at screen edges and change color
    if ball.ycor() < -200:
        ball.dy *= -1
        # Generate a random color for the ball
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        ball.color(f"#{red:02x}{green:02x}{blue:02x}")

    # Update the screen
    screen.update()