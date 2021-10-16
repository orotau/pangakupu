import numpy as np


def get_rotated_cell(grid_shape, row, column, rotation):

    # the purpose of this function is to take as input the 'row' and 'column'
    # of the cell that is to be updated in the current grid
    # and return the row and column of the rotated cell as a tuple
    grid_to_rotate = np.ones(grid_shape)
    grid_to_rotate[row, column] = 0  # we want to keep this one new value
    rotated_array = np.rot90(grid_to_rotate, rotation / 90)
    rotated_cell = np.where(rotated_array == 0)
    row_rotated_cell = rotated_cell[0]
    column_rotated_cell = rotated_cell[1]
    return row_rotated_cell, column_rotated_cell


def create_new_grid(current_grid, row, column, rotation):

    # the purpose of this function is to take the current grid (last entry in grids)
    # and update the cell indicated by row, column
    # then update the other cells to match indicated by rotation (0, 90, 180)
    # then return the new grid

    if rotation not in [0, 90, 180]:
        return False

    cells_to_update = []

    # the cell we have pressed space bar on always gets updated (toggles)
    rc_0 = row, column
    cells_to_update.append(rc_0)

    if rotation == 0:
        pass
    else:
        # get the 180 degree rotation
        rc_180 = get_rotated_cell(current_grid.shape, row, column, 180)
        cells_to_update.append(rc_180)
        if rotation == 180:
            pass
        elif rotation == 90:
            rc_90 = get_rotated_cell(current_grid.shape, row, column, 90)
            cells_to_update.append(rc_90)
            rc_270 = get_rotated_cell(current_grid.shape, row, column, 270)
            cells_to_update.append(rc_270)
        else:
            return False

    # create the new grid
    current_cell_value = current_grid[row, column]
    new_cell_value = not current_cell_value
    new_grid = current_grid.copy()

    for rc in cells_to_update:
        new_grid[rc[0], rc[1]] = new_cell_value
    return new_grid
