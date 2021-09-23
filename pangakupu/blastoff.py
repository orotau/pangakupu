import pygame
from sys import exit

pygame.init()
cell_size = 40 # in pixels
x_by_x = 15 # grid dimension 
screen = pygame.display.set_mode((cell_size * x_by_x, cell_size * x_by_x))
pygame.display.set_caption('Panga Kupu')
clock = pygame.time.Clock()
# test_surface = pygame.Surface((cell_size, cell_size))
# test_surface.fill('Red')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # screen.blit(test_surface, (0 , 0))        
    pygame.display.update()
    clock.tick(60)
