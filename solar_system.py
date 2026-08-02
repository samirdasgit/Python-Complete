import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Animation")

clock = pygame.time.Clock()

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

BLACK = (5, 5, 20)
WHITE = (255, 255, 255)
YELLOW = (255, 220, 0)

# Background stars
stars = []
for _ in range(250):
    stars.append((
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT),
        random.randint(1, 2)
    ))

# Planet data
planets = [
    {"name":"Mercury","radius":55,"size":6,"color":(180,180,180),"speed":0.045},
    {"name":"Venus","radius":85,"size":8,"color":(255,170,80),"speed":0.035},
    {"name":"Earth","radius":120,"size":9,"color":(0,140,255),"speed":0.030},
    {"name":"Mars","radius":155,"size":7,"color":(220,80,50),"speed":0.024},
    {"name":"Jupiter","radius":210,"size":18,"color":(230,180,120),"speed":0.018},
    {"name":"Saturn","radius":280,"size":15,"color":(230,220,120),"speed":0.015},
    {"name":"Uranus","radius":350,"size":12,"color":(120,255,255),"speed":0.012},
    {"name":"Neptune","radius":420,"size":12,"color":(70,100,255),"speed":0.010},
]

font = pygame.font.SysFont("Arial", 16)

angle = 0

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Draw stars
    for x, y, r in stars:
        pygame.draw.circle(screen, WHITE, (x, y), r)

    # Sun
    pygame.draw.circle(screen, YELLOW, (CENTER_X, CENTER_Y), 35)

    # Glow
    pygame.draw.circle(screen, (255,180,0), (CENTER_X, CENTER_Y), 45, 2)
    pygame.draw.circle(screen, (255,120,0), (CENTER_X, CENTER_Y), 55, 1)

    for planet in planets:

        orbit = planet["radius"]

        pygame.draw.circle(
            screen,
            (60,60,60),
            (CENTER_X, CENTER_Y),
            orbit,
            1
        )

        a = angle * planet["speed"]

        px = CENTER_X + math.cos(a) * orbit
        py = CENTER_Y + math.sin(a) * orbit

        pygame.draw.circle(
            screen,
            planet["color"],
            (int(px), int(py)),
            planet["size"]
        )

        # Saturn ring
        if planet["name"] == "Saturn":
            pygame.draw.ellipse(
                screen,
                (220,220,180),
                (px-22, py-8, 44, 16),
                1
            )

        label = font.render(planet["name"], True, WHITE)
        screen.blit(label, (px+10, py-10))

    angle += 1

    pygame.display.flip()

pygame.quit()