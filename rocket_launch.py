import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket Launch Animation")

clock = pygame.time.Clock()

# Colors
BLACK = (10, 10, 30)
WHITE = (255, 255, 255)
RED = (255, 60, 0)
ORANGE = (255, 150, 0)
YELLOW = (255, 255, 0)
GRAY = (180, 180, 180)
LIGHTGRAY = (220, 220, 220)
BLUE = (70, 170, 255)

# Rocket
rocket_x = WIDTH // 2
rocket_y = HEIGHT - 120
speed = 2

# Stars
stars = []
for _ in range(120):
    stars.append([
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT),
        random.randint(1, 3)
    ])

# Smoke particles
particles = []


def draw_rocket(x, y):
    # Body
    pygame.draw.rect(screen, LIGHTGRAY, (x-15, y-60, 30, 70))

    # Nose
    pygame.draw.polygon(screen, RED, [
        (x, y-90),
        (x-20, y-60),
        (x+20, y-60)
    ])

    # Wings
    pygame.draw.polygon(screen, BLUE, [
        (x-15, y-10),
        (x-35, y+20),
        (x-15, y+15)
    ])

    pygame.draw.polygon(screen, BLUE, [
        (x+15, y-10),
        (x+35, y+20),
        (x+15, y+15)
    ])

    # Window
    pygame.draw.circle(screen, BLUE, (x, y-35), 8)

    # Flame animation
    flame = random.randint(25, 45)

    pygame.draw.polygon(screen, ORANGE, [
        (x-10, y+10),
        (x+10, y+10),
        (x, y+flame)
    ])

    pygame.draw.polygon(screen, YELLOW, [
        (x-5, y+10),
        (x+5, y+10),
        (x, y+flame-10)
    ])


running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Draw stars
    for star in stars:
        pygame.draw.circle(screen, WHITE, (star[0], star[1]), star[2])

    # Smoke particles
    particles.append([
        rocket_x + random.randint(-8, 8),
        rocket_y + 15,
        random.randint(6, 12),
        random.randint(40, 70)
    ])

    new_particles = []

    for p in particles:
        pygame.draw.circle(screen, GRAY, (int(p[0]), int(p[1])), int(p[2]))
        p[1] += 2
        p[0] += random.randint(-1, 1)
        p[2] += 0.15
        p[3] -= 1

        if p[3] > 0:
            new_particles.append(p)

    particles = new_particles

    draw_rocket(rocket_x, rocket_y)

    rocket_y -= speed

    if rocket_y < -120:
        rocket_y = HEIGHT + 120
        particles.clear()

    pygame.display.flip()

pygame.quit()