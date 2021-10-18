import os.path
import config
from pathlib import Path
from collections import deque
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

cf = config.ConfigFile()
grids_path = cf.configfile[cf.computername]["grids_file_path"]

root = tk.Tk()
frame = ttk.Frame(root)  # frame in root
frame.grid()
image_label = ttk.Label(frame)  # the label to contain the image

root.bind("<Right>", lambda event: next())
root.bind("<Left>", lambda event: previous())
root.bind("<Return>", lambda event: select())

# create a next and previous button
next_button = ttk.Button(frame, command=lambda event: next())
previous_button = ttk.Button(frame, command=lambda event: previous())

# get the grid image files
files_and_directories = [os.path.join(grids_path, f) for f in os.listdir(grids_path)]
all_files = [f for f in files_and_directories if os.path.isfile(f)]
image_files = [x for x in all_files if x.endswith(".jpeg") or x.endswith(".png")]

if image_files:
    image_files = deque(image_files)
else:
    # no image files
    raise SystemExit("No image files found")

# display image
def display_image():
    image = Image.open(image_files[0])
    image_to_display = ImageTk.PhotoImage(image)
    image_label.configure(image=image_to_display)
    image_label.image = image_to_display
    image_label.grid(row=0, column=0)


def next():
    image_files.rotate(1)
    display_image()


def previous():
    image_files.rotate(-1)
    display_image()

    
def select():
    # https://stackoverflow.com/a/48593823/4679876
    print(Path(image_files[0]).stem)
    


display_image()

root.mainloop()
