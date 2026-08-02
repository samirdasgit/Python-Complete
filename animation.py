import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Animation Example")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)

# Ball properties
x = 100
y = 100
radius = 30
speed_x = 5
speed_y = 4

# FPS
clock = pygame.time.Clock()

running = True

while running:
    clock.tick(60)  # 60 FPS

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move ball
    x += speed_x
    y += speed_y

    # Bounce from walls
    if x + radius >= WIDTH or x - radius <= 0:
        speed_x *= -1

    if y + radius >= HEIGHT or y - radius <= 0:
        speed_y *= -1

    # Draw
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (x, y), radius)

    pygame.display.update()

pygame.quit()
sys.exit()