import pygame
import numpy as np
import pprint

"""
The creation of a board is compared with creating a map
that maps out the journey from start (blank board) to finish
So the update_map.py contains the code that allows us to update the map
The key aspects being
a) The history of the grid - grids
b) The necessary data for undo and redo - undos
c) The new grid (if relevant)
"""

def redo_map(grids, undos):
    # if there is nothing in undos, then do nothing - beep
    # otherwise remove the most recent entry in undos and add it to the end of grids
    try:
        grid_to_restore = undos.pop()
    except:
        # nothing in undos
        pygame.mixer.init()
        sound = pygame.mixer.Sound('nothing left to do.wav')
        sound.play()
    else:
        grids.append(grid_to_restore)
        return grids, undos


def undo_map(grids, undos):
    # if there is only 1 entry in grids, then do nothing - beep
    # otherwise remove the most recent entry in grids and add it to the end of undos
    if len(grids) == 1:
        pygame.mixer.init()
        sound = pygame.mixer.Sound('nothing left to do.wav')
        sound.play()
    else:
        grid_to_undo = grids.pop()
        undos.append(grid_to_undo)
        return grids, undos


def new_grid(grid, grids, undos):
    grids.append(grid)
    # check to see if we are at the end of the trunk or not
    if undos:
        # we are not at the end of the trunk, so branching off
        undos.clear()
    return grids, undos
        
    
