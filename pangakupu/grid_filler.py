import tkinter as tk
from tkinter import font


root = tk.Tk()
xw_font = tk.font.Font(family="Ubuntu Mono", size=-50)
c = tk.Canvas(root, width=100, height=100)  # canvas in root
c.create_rectangle(0, 0, 50, 50, fill="green")
c.create_text(25, 25, font=xw_font, text="ā")
c.pack()
root.mainloop()
