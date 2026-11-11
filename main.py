import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Graphics Window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 40))
    pygame.draw.circle(screen, (80, 180, 255), (400, 500), 100)
    pygame.display.flip()

pygame.quit()