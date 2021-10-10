import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))

done = False
rectangle_x =  10
rectangle_y = 30

while not done:
    for event in pygame.event.get():
        rectangle = pygame.Rect(rectangle_x, rectangle_y, 13, 13)
        RED = (255, 30, 70)
        pygame.draw.rect(screen, RED, rectangle)
        pressed = pygame.key.get_pressed()

        if(pressed[pygame.K_LEFT]):
            if(rectangle_x - 5 > 0):
                rectangle_x = rectangle_x - 5
        elif(pressed[pygame.K_RIGHT]):
            if(rectangle_x + 5 < 400):
                rectangle_x = rectangle_x + 5
        elif(pressed[pygame.K_UP]):
            if(rectangle_y - 5 > 0):
                rectangle_y = rectangle_y - 5
        elif(pressed[pygame.K_DOWN]):
            if(rectangle_y + 5 < 400):
                rectangle_y = rectangle_y + 5

        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()

