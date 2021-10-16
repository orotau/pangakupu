import pygame
import numpy as np
import drawer as dr
import number_grid as ng


def get_grid_name(grid):
    # given the grid get the name of the grid
    # the grid is identified by all its entries, concatenated to make a binary
    # this is then converted to a hex to reduce length
    # if the first entry is 'False' then the name will be flipped
    # that way we don't have to deal with 0's at the start

    FLIP_ADD = "-flip"
    Flip = grid[0, 0] == False  # we will flip if first entry is 0
    name_grid = ~grid if Flip else grid
    name = [str(int(x)) for x in name_grid.flat]
    bin_string = "".join(name)
    hex_name = hex(int(bin_string, base=2))

    if Flip:
        return hex_name + FLIP_ADD + ".jpeg"
    else:
        return hex_name + ".jpeg"


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
    pygame.image.save(screen, grid_name)

    return
