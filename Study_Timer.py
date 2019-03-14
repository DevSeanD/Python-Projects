"""
Hello this application is designed as a study timer app to aid the user when studying by keeping them motivated
This application uses tkinter as its GUI interface
Created by: DevSeanD
"""

import tkinter as tk
import time
import random
from tkinter import ttk
from tkinter import *

window = tk.Tk()

window.title("Study Timer")

window.geometry("300x300")


# Functions

def study_timer():  # does time conversions

    num_hour = float(entry_field1.get())
    num_hour = num_hour * 3600  # converts hours to seconds

    num_min = float(entry_field2.get())
    num_min = num_min * 60  # converts minuets to seconds

    total_sec = num_min + num_hour

    return total_sec  # prints out a motivation quote dependant upon random generated number


for y in range(1):  # generates one random number
    quote = (random.randint(1, 5))  # generates a random number between 1 and 5

    if quote == 1:
        label_quote1 = tk.Label(text="\"Never, never, never give up\"", bd=1, anchor=CENTER)
        label_quote1 .grid(column=0, row=0)

    if quote == 2:
        label_quote2 = tk.Label(text="  \"Quality is not an act, it is a habit\"", bd=1, anchor=CENTER)
        label_quote2.grid(column=0, row=0)

    if quote == 3:
        label_quote2 = tk.Label(text="  \"It always seems impossible until its done\"", bd=1, anchor=CENTER)
        label_quote2.grid(column=0, row=0)

    if quote == 4:
        label_quote2 = tk.Label(text="  \"Life is 10% what happens to you and 90% how you react to it\"", bd=1, anchor=CENTER)
        label_quote2.grid(column=0, row=0)
        window.geometry("450x300")      # higher rez because of longer text

    if quote == 5:
        label_quote2 = tk.Label(text="  \"You cannot cross the sea by merely staring at the water\"", bd=1, anchor=CENTER)
        label_quote2.grid(column=0, row=0)
        window.geometry("420x300")      # higher rez because of longer text


def display_timer():  # displays the ending message

    time.sleep(study_timer())
    display_min = float(study_timer() / 60)

    label_fin = tk.Label(text="You have finished your study session of")
    label_fin.grid(column=0, row=8)

    display_fin = tk.Text(master=window, height=1, width=5)
    display_fin.grid(column=0, row=9)
    display_fin.insert(tk.END, display_min)

    label_time = tk.Label(text="minuets")
    label_time.grid(column=0, row=10)


# LABEL
label_hour = tk.Label(text="How many hours?")
label_hour.grid(column=0, row=1)

label_min = tk.Label(text="How many minuets?")
label_min.grid(column=0, row=3)

# BUTTON
button1 = ttk.Button(text="Start Timer", command=display_timer)
button1.grid(column=0, row=5)

label_blank = tk.Label(text="  ")
label_blank.grid(column=0, row=6)

# Entry Field
entry_field1 = ttk.Entry()
entry_field1.grid(column=0, row=2)

entry_field2 = ttk.Entry()
entry_field2.grid(column=0, row=4)

window.mainloop()
