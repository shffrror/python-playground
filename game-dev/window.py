import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))

done = False

while not done:
    for event in pygame.event.get():
        rectangle = pygame.Rect(10, 30, 13, 13)
        RED = (255, 30, 70)
        pygame.draw.rect(screen, RED, rectangle)
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()

