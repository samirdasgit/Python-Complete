import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smooth 60 FPS Animation")

clock = pygame.time.Clock()

angle = 0.0
rotation_speed = 2.0      # radians per second

running = True

while running:

    # Limit to 60 FPS and get elapsed time
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animation using delta time
    angle += rotation_speed * dt

    screen.fill((10, 10, 20))

    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    # Draw animated circles
    for i in range(40):
        y = 80 + i * 12

        x = center_x + math.sin(angle + i * 0.25) * 120

        pygame.draw.circle(
            screen,
            (70, 170, 255),
            (int(x), y),
            6
        )

    pygame.display.flip()

pygame.quit()