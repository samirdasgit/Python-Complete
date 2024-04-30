import turtle

# Create the screen and turtle objects
screen = turtle.Screen()
ball = turtle.Turtle()

# Set ball properties
ball.speed(0)  # Set animation speed (0 - fastest)
ball.shape("circle")
ball.color("red")

# Define starting position and movement direction
ball.penup()
ball.goto(0, 100)
ball.pendown()
ball.dy = -0.5  # Change in y-coordinate (controls bouncing)

while True:
    # Update ball position
    ball.sety(ball.ycor() + ball.dy)

    # Check for bouncing at screen edges
    if ball.ycor() < -200:
        ball.dy *= -1  # Reverse direction when hitting bottom

    # Update the screen (redraws everything)
    screen.update()