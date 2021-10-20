import pygame
import numpy as np
from pathlib import Path
import config
import bitstring as bs
import drawer as dr
import number_grid as ng

cf = config.ConfigFile()
grids_path = cf.configfile[cf.computername]["grids_file_path"]


def get_grid_name(grid):
    # the grid name is the binary representation of the grid
    # converted to a hex (to shorten it)
    # then NxN at the end where N is the cell count across and down
    # assumed square at this point - Oct 21 - 2021
    # then the extension

    grid_id = "".join([str(int(x)) for x in grid.flat])

    #
    if divmod(grid.shape[0]**2, 4)[1] == 0:
        # cell count is an exact multiple of 4
        length_of_hex_suffix = 0
    else:
        # 3 goes to 1, 2 to 2 and 1 to 3
        length_of_hex_suffix = 4 - divmod(grid.shape[0]**2, 4)[1]
        
    hex_suffix = length_of_hex_suffix * "0"  

    grid_id_for_name = grid_id + hex_suffix    
    grid_id_for_name = bs.BitArray(bin=grid_id_for_name)
    
    hex_stem = grid_id_for_name.hex
    
    size_addon = "-" + str(grid.shape[0]) + "x" + str(grid.shape[0])
    
    grid_name = hex_stem + size_addon + ".jpeg"
    return grid_name


def export_grid(grid, rekts, screen, cell_size):
    # the purpose of this function is to
    # get the name of the grid
    # export it as an image
    grid_name = get_grid_name(grid)

    # grid
    dr.draw_grid(grid, screen, rekts)

    # add numbering
    grid_numbers = ng.get_numbers(grid)
    dr.draw_grid_numbers(grid_numbers, screen, rekts, cell_size)

    # grid lines (excluding the 4 borders)
    dr.draw_grid_lines(screen, rekts, cell_size)
    pygame.image.save(screen, Path(grids_path, grid_name))

    return
