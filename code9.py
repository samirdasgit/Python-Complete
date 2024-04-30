import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)

# Create an empty line object
line, = ax.plot([], [], lw=2)

# Initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# Animation function: this is called sequentially
def animate(i):
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(x + 0.1*i)  # Vary the phase for animation
    line.set_data(x, y)
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, init_func=init, interval=20, blit=True)

# Display the animation
plt.show()