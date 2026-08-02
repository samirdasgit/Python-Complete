import pygame
import math

pygame.init()

WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DNA Double Helix Animation")

clock = pygame.time.Clock()

BLACK = (10, 10, 20)
WHITE = (255, 255, 255)

RED = (255, 70, 70)
BLUE = (70, 170, 255)
GREEN = (80, 220, 120)
YELLOW = (255, 220, 0)

font = pygame.font.SysFont("Arial", 18)

angle = 0

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    title = font.render("DNA Double Helix Animation", True, WHITE)
    screen.blit(title, (20, 20))

    centerX = WIDTH // 2

    for i in range(50):

        y = i * 15 + 30

        a = angle + i * 0.35

        x1 = centerX + math.sin(a) * 120
        x2 = centerX - math.sin(a) * 120

        scale = (math.cos(a) + 1.2)

        radius = int(4 + scale * 3)

        # Backbone
        pygame.draw.circle(screen, BLUE, (int(x1), y), radius)
        pygame.draw.circle(screen, RED, (int(x2), y), radius)

        # Base Pair
        pair = i % 4

        if pair == 0:
            color = GREEN
            text = "A-T"
        elif pair == 1:
            color = YELLOW
            text = "G-C"
        elif pair == 2:
            color = (255, 100, 255)
            text = "T-A"
        else:
            color = (0, 255, 255)
            text = "C-G"

        pygame.draw.line(screen, color,
                         (int(x1), y),
                         (int(x2), y), 2)

        if scale > 1.0:
            lbl = font.render(text, True, color)
            screen.blit(lbl, (centerX - 18, y - 8))

    angle += 0.05

    pygame.display.flip()

pygame.quit()