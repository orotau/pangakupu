import prettytable
x = prettytable.PrettyTable()

GRID_SIZE = 9 #will be passed in
WHITE_TEXT = '[]' 
BLACK_TEXT = '  '
grid_number = "00" # to start with
grid_headings = [f'{x:02}' for x in range(1, GRID_SIZE + 1)] #across and down


x.field_names = [grid_number] + grid_headings
for row in grid_headings:
    x.add_row([row] + [WHITE_TEXT]*GRID_SIZE)
 
x.hrules = prettytable.ALL
#x.junction_char = "-"
#x.left_padding_width = prettytable.NONE
#x.right_padding_width = prettytable.NONE
#x.padding_width = 0
print(x)
