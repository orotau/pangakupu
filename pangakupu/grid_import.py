import numpy as np
import bitstring as bs

SPLITTER1 = "-"
SPLITTER2 = "x"


def import_grid(file_stem):
    # given the file stem (no extension)
    # return a numpy array of 0 and 1 to represent the grid

    # first split off the 'hex stem' from the 'size addon'
    hex_stem = file_stem.split(SPLITTER1)[0]
    size_addon = file_stem.split(SPLITTER1)[1]
    size = int(size_addon.split(SPLITTER2)[0])

    hex_name = bs.BitArray(hex=hex_stem)
    grid_id = hex_name.bin

    # Do we need to remove any part of the grid_id?
    if len(grid_id) == size ** 2:
        # no part needs to be removed
        remove_binary_suffix = False
    else:
        remove_binary_suffix = True

    if remove_binary_suffix:
        length_of_binary_suffix = len(grid_id) - size ** 2
        grid_id = grid_id[:-length_of_binary_suffix]

    return grid_id
