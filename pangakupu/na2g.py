import pygame
import numpy as np
from sys import exit
import create_new_grid as cng
import update_map as um

# Turn a numpy array into a grid

# Constants
CELL_SIZE = 50 # in pixels
grid_size = 15 #count will be passed in

# pygame stuff
pygame.init()
screen = pygame.display.set_mode((CELL_SIZE * grid_size, CELL_SIZE * grid_size))
screen.fill('GRAY') # not sure if this is in the right position
pygame.display.set_caption('Panga Kupu')
clock = pygame.time.Clock()

# the 'here' square'
here = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)

# create randomly populated boolean grid to start with
grids = []
rng = np.random.default_rng()
start_grid = rng.choice(a=[True, False], size=(grid_size, grid_size), p=[0, 1])  
grids.append(start_grid)

undos = [] # grids that have been undone using 'ctrl-x'


# create and fill the rekts array
# there are 2 ways to think about the rectangles
# from the numpy perspective and from the pygame perspective

# from the numpy perspective each rectangle is an item in a numpy array
# referenced by a tuple of consecutive integers (row, column) - 0 indexed

# from the pygame perspective each rectangle's position is 
# referenced by a tuple of pixels (distance from left, distance from top)

# we can move from one to the other as follows ...
# numpy (row, column) to pygame (distance from left, distance from top)
# distance from left = column * CELL_SIZE
# distance from top = row * CELL_SIZE

# e.g. if CELL_SIZE = 50
# numpy (2, 3) = 3 * 50 = 150 from left, 2 * 50 = 100 from top = pygame(150, 100)

# AND the other way round
# pygame (distance from left, distance from top) to numpy (row, column)
# row  =  int(distance from top / CELL_SIZE) (convert to integer for neatness)
# column  =  int(distance from left / CELL_SIZE) (convert to integer for neatness)

# e.g. if CELL_SIZE = 50
# pygame (150, 100) = 100 / 50 = 2 row, 150 / 50 = 3 column = numpy(2, 3)


rekts = np.empty((grid_size, grid_size), dtype=object)
for index, x in np.ndenumerate(grids[-1]):
    rekts[index] = pygame.Rect((index[1] * CELL_SIZE, index[0] * CELL_SIZE) ,
                                                   (CELL_SIZE, CELL_SIZE))
 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()   

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                here_row = int(here.top / CELL_SIZE)
                here_column = int(here.left / CELL_SIZE)
                new_grid = cng.create_new_grid(grids[-1], here_row, here_column, 90)
                # add the new grid and adjust 'undos' if necessary
                um.new_grid(new_grid, grids, undos)
                
                
            if event.mod & pygame.KMOD_CTRL:
                if event.key == pygame.K_x:
                    um.undo_map(grids, undos)
                if event.key == pygame.K_y:
                    um.redo_map(grids, undos)
            
            
    keys = pygame.key.get_pressed()
    if sum(keys)==1: # this prevents diagonal movement when 2 keys are pressed
        if keys[pygame.K_UP]:
            here.move_ip((0 , -CELL_SIZE))
        if keys[pygame.K_DOWN]:
            here.move_ip((0 , CELL_SIZE))
        if keys[pygame.K_LEFT]:
            here.move_ip((-CELL_SIZE , 0))
        if keys[pygame.K_RIGHT]:
            here.move_ip((CELL_SIZE , 0))       
        here.clamp_ip(screen.get_rect()) #prevent movement off grid 
    



    # 
    # ###############
    # print out the rects #
    # ###############
    #
    for index, x in np.ndenumerate(grids[-1]):
        if x :
            kolor = 'WHITE'
        else :
            kolor = 'BLACK'
        pygame.draw.rect(screen, kolor, rekts[index])

    # print the grid lines (excluding the 4 borders)
    # horizontal lines
    for row in rekts[1:]:
        grid_points = []
        
        for x in row:
            grid_points.append((x.left,  x.top))
        
        # get into the left of the last column
        grid_points.append((x.left + CELL_SIZE, x.top))
        
        pygame.draw.lines(screen, 'BLACK', False, grid_points)

    # vertical lines    
    for column in np.transpose(rekts)[1:]:
        grid_points = []
        
        for x in column:
            grid_points.append((x.left, x.top))
            
        # get into top of the last row    
        grid_points.append((x.left, x.top  + CELL_SIZE))    
        
        pygame.draw.lines(screen, 'BLACK', False, grid_points)
        
    pygame.draw.rect(screen, 'GREEN', here, 4)     
    pygame.display.update()
    clock.tick(10) # by trial and error moving the 'here' rectangle around (may change)
