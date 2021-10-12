import numpy as np
from collections import namedtuple

'''
The purpose of this module is to handle the numbering of the grid
'''

Surround = namedtuple('Surround', ['n', 'e', 's', 'w'])
across = (Surround(n = True, e = True, s = True, w = False),
          Surround(n = True, e = True, s = False, w = False),
          Surround(n = False, e = True, s = False, w = False))
                 
down = (Surround(n = False, e = True, s = True, w = True),
        Surround(n = False, e = False, s = True, w = True),
        Surround(n = False, e = False, s = True, w = False))
                
across_and_down = (Surround(n = False, e = True, s = True, w = False),
                   Surround(n = False, e = False, s = False, w = False))    

other = (Surround(n = True, e = True, s = True, w = True),
         Surround(n = True, e = True, s = False, w = True),
         Surround(n = True, e = False, s = True, w = True),
         Surround(n = True, e = False, s = True, w = False),
         Surround(n = False, e = True, s = False, w = True),
         Surround(n = True, e = False, s = False, w = True),
         Surround(n = True, e = False, s = False, w = False),
         Surround(n = False, e = False, s = False, w = True))

# assert uniqueness (belt and braces)
assert (len(set(across + down + across_and_down + other)) == 
            len(across + down + across_and_down + other))


def get_surround_state(grid, row, column):
    '''
    given the grid and the row and column of the cell that 
    we are looking at, check n, s, e and w
    and return the appropriate Surround namedtuple
    '''
    if grid[row, column] == False: # black
        return False
    
    if row != 0:
        north = grid[row - 1, column]
    else:
        # we are on the first row so no north
        north = False
        
    if column != grid.shape[1] - 1:
        east = grid[row, column + 1]
    else:
        # we are on the last column so no east
        east = False
        
    if row != grid.shape[0] - 1:
        south = grid[row + 1, column]
    else:
        # we are on the last row so no south
        south = False
        
    if column != 0:
        west = grid[row, column - 1]
    else:
        # we are on the first column so no west
        west = False        
        
    return Surround(n = north, e = east, s = south, w = west)    



def get_numbers(grid):

    surround_states = np.empty(grid.shape, dtype=object)
    number_type = np.empty(grid.shape, dtype='<U7') #7 = longest string
    numbering = np.empty(grid.shape, dtype='<U3') # up to 999
    print(numbering)
    
    # get the 'surround state' of each cell
    for (r, c), x in np.ndenumerate(grid):
        surround_state = get_surround_state(grid, r, c)
        if surround_state:
            surround_states[r, c] = surround_state
        else:
            surround_states[r, c] = False

    # get the 'number type' of each cell    
    for (r, c), x in np.ndenumerate(surround_states):
        if x in across:
            number_type[r, c] = "across"
        elif x in down:
            number_type[r, c] = "down"  
        elif x in across_and_down:
            number_type[r, c] = "a_and_d"
        else:
            number_type[r, c] = ""
    print(number_type)
    
    number_of_numbers = 0
    for (r, c), x in np.ndenumerate(number_type):
        if x != "":
            number_of_numbers = number_of_numbers + 1
            numbering[r, c] = number_of_numbers
    return(numbering)

