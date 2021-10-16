import prettytable
import numpy

x = prettytable.PrettyTable()

GRID_SIZE = 15  # will be passed in
WHITE_TEXT = "::"
BLACK_TEXT = "  "
grid_number = "XX"  # to start with
grid_headings = [f"{x:02}" for x in range(1, GRID_SIZE + 1)]  # across and down

# create empty grid
# grid = numpy.full((GRID_SIZE,GRID_SIZE), False, dtype=bool)

# create randomly populated grid
rng = numpy.random.default_rng()
grid = rng.choice(a=[False, True], size=(GRID_SIZE, GRID_SIZE))

grid_to_print = numpy.where(grid, WHITE_TEXT, BLACK_TEXT)
grid_to_print_as_list = grid_to_print.tolist()

x.field_names = [grid_number] + grid_headings

for (row_number, row_content) in zip(grid_headings, grid_to_print_as_list):
    x.add_row([row_number] + row_content)

x.hrules = prettytable.ALL
x.junction_char = "-"

print(x)
