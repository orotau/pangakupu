import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,800))
rect0 = pygame.Rect(60, 60, 60, 60)
rect = rect0.copy()
clock = pygame.time.Clock()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    keys = pygame.key.get_pressed()

    if sum(keys)==1: # this prevents diagonal movement when 2 keys are pressed
        if keys[pygame.K_UP]:
            rect.move_ip((0 , -1))
        if keys[pygame.K_DOWN]:
            rect.move_ip((0 , 1))
        if keys[pygame.K_LEFT]:
            rect.move_ip((-1 , 0))
        if keys[pygame.K_RIGHT]:
            rect.move_ip((1 , 0))       
        rect.clamp_ip(screen.get_rect()) #prevent movement off grid

    screen.fill('GRAY')
    pygame.draw.rect(screen, 'RED', rect, 4)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()