import pygame
import pygame.freetype
import numpy as np


def draw_grid(grid, screen, rekts):
    for index, x in np.ndenumerate(grid):
        kolor = "WHITE" if x == True else "BLACK"
        pygame.draw.rect(screen, kolor, rekts[index])


def draw_grid_lines(screen, rekts, cell_size):
    # horizontal lines
    for row in rekts[1:]:
        grid_points = []

        for x in row:
            grid_points.append((x.left, x.top))

        # get into the left of the last column
        grid_points.append((x.left + cell_size, x.top))
        pygame.draw.lines(screen, "BLACK", False, grid_points)

    # vertical lines
    for column in np.transpose(rekts)[1:]:
        grid_points = []

        for x in column:
            grid_points.append((x.left, x.top))

        # get into top of the last row
        grid_points.append((x.left, x.top + cell_size))
        pygame.draw.lines(screen, "BLACK", False, grid_points)


def draw_grid_border(screen, grid_rect):
    grid_points = []
    grid_points.append(grid_rect.topleft)
    grid_points.append(grid_rect.topright)
    grid_points.append(grid_rect.bottomright)
    grid_points.append(grid_rect.bottomleft)
    pygame.draw.lines(screen, "BLACK", True, grid_points)
    return


def draw_grid_numbers(grid_numbers, screen, rekts, cell_size):
    pygame.freetype.init()
    my_ft_font: None = pygame.freetype.SysFont("opensymbol", cell_size / 2.5)
    offset = int(cell_size / 3 / 5)
    for (x, y), number in np.ndenumerate(grid_numbers):
        if number != "":
            my_ft_font.render_to(
                screen,
                (rekts[x, y].left + offset, rekts[x, y].top + offset),
                number,
                "BLACK",
            )


def draw_here(screen, kolor, here, border):
    pygame.draw.rect(screen, kolor, here, border)
