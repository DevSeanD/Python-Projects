"""
Hello, this application is a simplistic to do list made using tkinter
Create by: DevSeanD

"""

import tkinter as tk
import time
import random
from tkinter import ttk
from tkinter import *


def to_do():
    item_number = item_number_entry.get()
    item_number = int(item_number)
    counter = 1
    y_shift = 0

    while True:
        if counter != 0:
            to_do_item = ttk.Entry(width=65)
            to_do_item.place(x=30, y=110 + y_shift)
            counter += 1
            y_shift += 50

        if counter > item_number:
            break


window = tk.Tk()

window.title("To Do List")

window.geometry("600x1000")

# Label
welcome_label = Label(text="Hello, welcome to a simple To-Do list app")
welcome_label.place(x=150, y=10)

item_number_label = Label(text="How many items would you like?")
item_number_label.place(x=30, y=30)

#   Entry
item_number_entry = tk.Entry()
item_number_entry.place(x=30, y=50)

#   Button
item_number_button = tk.Button(text="Enter", font=("arial", 10), command=to_do)
item_number_button.place(x=30, y=75)
y_shift = 0
counter = 0


window.mainloop()
