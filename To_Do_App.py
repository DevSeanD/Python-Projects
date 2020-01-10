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
    item_number = item_number_entry.get() # user supplied number of items
    item_number = int(item_number)
    counter = 1
    y_shift = 0  # used in order to shift the entry boxes down

    while True:     # this loop will only continue when the counter is less than item_number
        if item_number > 18:   # if item_number is greater then the loop will be broken
            input_error_label = Label(text="Please enter any number up to 18")
            input_error_label.place(x=30, y=110)
            break

        if counter != 0:
            to_do_item = ttk.Entry(width=60)
            to_do_item.place(x=85, y=110 + y_shift)
            check_box = IntVar()
            Checkbutton(text="Done", variable=check_box).place(x=20, y=110 + y_shift)   # places check boxes in front of the entry fields
            counter += 1
            y_shift += 35

        if counter > 16:   # adjust the resolution if the number of list items is greater than 15
            window.geometry("600x1000")

        if counter > item_number:   # when the counter is more than the number of items break the while statement
            break


window = tk.Tk()

window.title("To Do List")

window.geometry("600x600")

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
