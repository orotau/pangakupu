import numpy as np


def update_grid(grids, row, column, rotation):

    # the purpose of this function is to take the current grid (last entry in grids)
    # and update the cell indicated by row, column
    # then update the other cells to match indicated by rotation (0, 90, 180)
    # then return the new grid
    if rotation not in [0, 90, 180]:
        return False
        
    current_grid = grids[-1]
    current_cell_value = current_grid[row, column] 
    new_cell_value = not current_cell_value
    
    new_grid = current_grid
    new_grid[row, column] = new_cell_value
    
    if rotation == 0:
        pass
    else :
        # we will need at least the 180 rotation
        # create a masked grid, with only the (row, column) as valid
        mask = np.ones(current_grid.shape)
        mask[row, column] = 0 # we want to keep this one new value
        masked_array = np.ma.masked_array(new_grid, mask)
        masked_array_180 = np.rot90(masked_array, 2)
        rc_180 = np.where((masked_array_180==True) | (masked_array_180== False))
        r_180 = rc_180[0]
        c_180 = rc_180[1]
        new_grid[r_180, c_180] = new_cell_value
        if rotation == 90:
            masked_array_90 = np.rot90(masked_array, 1)
            rc_90 = np.where((masked_array_90==True) | (masked_array_90== False))
            r_90 = rc_90[0]
            c_90 = rc_90[1]
            new_grid[r_90, c_90] = new_cell_value
            
            masked_array_270 = np.rot90(masked_array, 3)
            rc_270 = np.where((masked_array_270==True) | (masked_array_270== False))
            r_270 = rc_270[0]
            c_270 = rc_270[1]
            new_grid[r_270, c_270] = new_cell_value
    return new_grid
     
