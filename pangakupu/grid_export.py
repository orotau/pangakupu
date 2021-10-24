import pygame
import numpy as np
from pathlib import Path
import config
import bitstring as bs

import grid_drawer as gd
import grid_number as gn

cf = config.ConfigFile()
grids_path = cf.configfile[cf.computername]["grids_file_path"]
SPLITTER1 = "-"
SPLITTER2 = "x"


def get_grid_name(grid):
    # the grid name is the binary representation of the grid
    # converted to a hex (to shorten it)
    # then NxN at the end where N is the cell count across and down
    # assumed square at this point - Oct 21 - 2021
    # then the extension

    grid_id = bs.BitArray(bin="".join([str(int(x)) for x in grid.flat]))

    # do we need a binary suffix or not?
    if divmod(grid.shape[0] ** 2, 4)[1] == 0:
        # the cell count is an exact multiple of 4
        need_binary_suffix = False
    else:
        need_binary_suffix = True

    if need_binary_suffix:
        length_of_binary_suffix = 4 - divmod(grid.shape[0] ** 2, 4)[1]
        binary_suffix = length_of_binary_suffix * "0"
        grid_id.append(bs.BitArray(bin=binary_suffix))

    hex_stem = grid_id.hex

    size_addon = SPLITTER1 + str(grid.shape[0]) + SPLITTER2 + str(grid.shape[0])

    grid_name = hex_stem + size_addon + ".jpeg"
    return grid_name


def export_grid(grid, rekts, screen, cell_size):
    # the purpose of this function is to
    # get the name of the grid
    # export it as an image
    grid_name = get_grid_name(grid)

    # grid
    gd.draw_grid(grid, screen, rekts)

    # add numbering
    grid_numbers = gn.get_numbers(grid)
    gd.draw_grid_numbers(grid_numbers, screen, rekts, cell_size)

    # grid lines (excluding the 4 borders)
    gd.draw_grid_lines(screen, rekts, cell_size)
    pygame.image.save(screen, Path(grids_path, grid_name))

    return
