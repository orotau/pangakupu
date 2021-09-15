import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((3*297,3*210))
pygame.display.set_caption('Panga Kupu')
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)
