import pygame
import numpy as np
from sys import exit
import create_new_grid as cng
import update_grid_map as ugm
import export_grid as eg
import drawer as dr

# Create a New Grid

# Constants
TARGETED_GRID_SIZE = 600


# pygame stuff
def grid_inception(cell_count, symmetry):
    pygame.init()
    cell_size = int(TARGETED_GRID_SIZE / cell_count)

    # to deal with rounding issues
    actual_grid_size = cell_size * cell_count

    # used to keep the 'here' square in the grid
    grid_rect = pygame.Rect(0, 0, actual_grid_size, actual_grid_size)

    screen = pygame.display.set_mode((actual_grid_size, actual_grid_size))
    screen.fill("GRAY")
    pygame.display.set_caption("Panga Kupu - Grid Creation")
    clock = pygame.time.Clock()

    # the 'here' square'
    here = pygame.Rect(0, 0, cell_size, cell_size)

    # create randomly populated boolean grid to start with
    grids = []
    rng = np.random.default_rng()
    start_grid = rng.choice(a=[True, False], size=(cell_count, cell_count), p=[0, 1])
    grids.append(start_grid)

    undos = []  # grids that have been undone using 'ctrl-x'

    # create and fill the rekts array
    # there are 2 ways to think about the rectangles
    # from the numpy perspective and from the pygame perspective

    # from the numpy perspective each rectangle is an item in a numpy array
    # referenced by a tuple of consecutive integers (row, column) - 0 indexed

    # from the pygame perspective each rectangle's position is
    # referenced by a tuple of pixels (distance from left, distance from top)

    # we can move from one to the other as follows ...
    # numpy (row, column) to pygame (distance from left, distance from top)
    # distance from left = column * cell_size
    # distance from top = row * cell_size

    # e.g. if cell_size = 50
    # numpy (2, 3) = 3 * 50 = 150 from left, 2 * 50 = 100 from top = pygame(150, 100)

    # AND the other way round
    # pygame (distance from left, distance from top) to numpy (row, column)
    # row  =  int(distance from top / cell_size) (convert to integer for neatness)
    # column  =  int(distance from left / cell_size) (convert to integer for neatness)

    # e.g. if cell_size = 50
    # pygame (150, 100) = 100 / 50 = 2 row, 150 / 50 = 3 column = numpy(2, 3)

    rekts = np.empty((cell_count, cell_count), dtype=object)

    for index, x in np.ndenumerate(grids[-1]):
        rekts[index] = pygame.Rect(
            (index[1] * cell_size, index[0] * cell_size), (cell_size, cell_size)
        )


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    here_row = int(here.top / cell_size)
                    here_column = int(here.left / cell_size)
                    new_grid = cng.create_new_grid(
                        grids[-1], here_row, here_column, symmetry
                    )
                    # add the new grid and adjust 'undos' if necessary
                    ugm.new_grid(new_grid, grids, undos)

                if event.mod & pygame.KMOD_CTRL:
                    if event.key == pygame.K_x:
                        ugm.undo_map(grids, undos)

                    if event.key == pygame.K_y:
                        ugm.redo_map(grids, undos)

                    if event.key == pygame.K_e:
                        eg.export_grid(grids[-1], rekts, screen, cell_size)

                    if event.key == pygame.K_f:
                        new_grid = ~grids[-1]  # flip the grid
                        ugm.new_grid(new_grid, grids, undos)

        keys = pygame.key.get_pressed()
        if sum(keys) == 1:  # this prevents diagonal movement when 2 keys are pressed
            if keys[pygame.K_UP]:
                here.move_ip((0, -cell_size))
            if keys[pygame.K_DOWN]:
                here.move_ip((0, cell_size))
            if keys[pygame.K_LEFT]:
                here.move_ip((-cell_size, 0))
            if keys[pygame.K_RIGHT]:
                here.move_ip((cell_size, 0))
            here.clamp_ip(grid_rect)  # prevent movement off grid

        #
        # ######
        #  draw
        # ######
        #
        # grid
        dr.draw_grid(grids[-1], screen, rekts)

        # grid lines (excluding the 4 borders)
        dr.draw_grid_lines(screen, rekts, cell_size)

        # 'here' square
        dr.draw_here(screen, "GREEN", here, 3)

        pygame.display.update()
        clock.tick(
            10
        )  # by trial and error moving the 'here' rectangle around  (may change)


if __name__ == "__main__":

    import sys
    import argparse
    import ast

    # create the top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # create the parser for the grid_inception function
    grid_inception_parser = subparsers.add_parser("grid_inception")
    grid_inception_parser.add_argument(
        "cell_count", help="the number of cells across (and also down)", type=int
    )
    grid_inception_parser.add_argument(
        "symmetry", help="0-No symmetry, 90 or 180", type=int, choices=[0, 90, 180]
    )
    grid_inception_parser.set_defaults(function=grid_inception)

    # parse the arguments
    arguments = parser.parse_args()
    arguments = vars(arguments)  # convert from Namespace to dict

    # attempt to extract and then remove the function entry
    try:
        function_to_call = arguments["function"]
    except KeyError:
        print("You need a function name. Please type -h to get help")
        sys.exit()
    else:
        # remove the function entry as we are only passing arguments
        del arguments["function"]

    if arguments:
        # remove any entries that have a value of 'None'
        # We are *assuming* that these are optional
        # We are doing this because we want the function definition to define
        # the defaults (NOT the function call)
        arguments = {k: v for k, v in arguments.items() if v is not None}

        # alter any string 'True' or 'False' to bools
        arguments = {
            k: ast.literal_eval(v) if v in ["True", "False"] else v
            for k, v in arguments.items()
        }

    result = function_to_call(
        **arguments
    )  # note **arguments works fine for empty dict {}
