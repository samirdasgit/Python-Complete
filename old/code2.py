from turtle import *

# Set drawing speed
speed(1)

# Set background color
bgcolor('black')

# Move to starting position
penup()
goto(-50, 60)
pendown()

# Set pen color
color('blue')

# Begin filling
begin_fill()

# Draw the Windows logo
goto(100, 100)
goto(100, -100)
goto(-50, -60)
goto(-50, 60)

# End filling
end_fill()

# Set pen color to black
color('black')

# Cut the figure into two equal parts
goto(15, 100)
goto(15, -100)

# Set pen width
width(10)

# Draw the cut line
goto(100, 0)
goto(-100, 0)

# Finish drawing
done()

# Print success message
print("Windows logo drawn successfully using Python Turtle.")