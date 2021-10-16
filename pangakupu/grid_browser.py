import os.path
from collections import deque
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
frame = ttk.Frame(root)  # frame in root
frame.grid()
image_label = ttk.Label(frame)  # the label to contain the image

root.bind("<Right>", lambda event: next())
root.bind("<Left>", lambda event: previous())

# create a next and previous button
next_button = ttk.Button(frame, command=lambda event: next())
previous_button = ttk.Button(frame, command=lambda event: previous())

fyles = [f for f in os.listdir() if os.path.isfile(f)]
image_files = [x for x in fyles if x.endswith(".jpeg") or x.endswith(".png")]
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


display_image()

root.mainloop()
