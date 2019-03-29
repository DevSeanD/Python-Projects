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
from tkinter import messagebox

window = tk.Tk()

window.title("Study Timer")

window.geometry("265x300")


# Functions

def study_timer():  # does time conversions

    num_hour = float(entry_field1.get())
    num_hour = num_hour * 3600  # converts hours to seconds

    num_min = float(entry_field2.get())
    num_min = num_min * 60  # converts minuets to seconds

    total_sec = num_min + num_hour

    return total_sec  # prints out a motivation quote dependant upon random generated number


for y in range(1):  # generates one random number
    quote = (random.randint(1, 9))  # generates a random number between 1 and 5

    if quote == 1:
        label_quote1 = tk.Label(text="\"Never, never, never give up\"", bd=1, anchor=CENTER)
        label_quote1 .grid(column=0, row=0)

    if quote == 2:
        label_quote2 = tk.Label(text="  \"Quality is not an act, it is a habit\"", bd=1, anchor=CENTER)
        label_quote2.grid(column=0, row=0)

    if quote == 3:
        label_quote2 = tk.Label(text="  \"It always seems impossible until its done\"", bd=1, anchor=CENTER)
        label_quote2.grid(column=0, row=0)
        window.geometry("300x300")  # higher rez because of longer text

    if quote == 4:
        label_quote2 = tk.Label(text="  \"Life is 10% what happens to you and 90% how you react to it\"", bd=1, anchor=CENTER)
        label_quote2.grid(column=0, row=0)
        window.geometry("450x300")      # higher rez because of longer text

    if quote == 5:
        label_quote2 = tk.Label(text="  \"You cannot cross the sea by merely staring at the water\"", bd=1, anchor=CENTER)
        label_quote2.grid(column=0, row=0)
        window.geometry("420x300") # higher rez because of longer text

    if quote == 6:
        label_quote2 = tk.Label(text="  \"Even if you fall on your face, you are moving forward\"", bd=1, anchor=CENTER)
        label_quote2.grid(column=0, row=0)
        window.geometry("450x300")      # higher rez because of longer text

    if quote == 7:
        label_quote2 = tk.Label(text="  \"To be a good loser is to learn how to win\"", bd=1, anchor=CENTER)
        label_quote2.grid(column=0, row=0)
        window.geometry("300x300")  # higher rez because of longer text

    if quote == 8:
        label_quote2 = tk.Label(text="  \"Always do your best. What you plant now, you will harvest later\"", bd=1, anchor=CENTER)
        label_quote2.grid(column=0, row=0)
        window.geometry("450x300")      # higher rez because of longer text

    if quote == 9:
        label_quote2 = tk.Label(text="  \"Every day brings new choices\"", bd=1, anchor=CENTER)
        label_quote2.grid(column=0, row=0)


def display_timer():  # displays the ending message

    time.sleep(study_timer())
    display_min = float(study_timer() / 60)

    begin_alert = "You have finished your study session of "
    end_alert = " minuets!"
    display_min = str(display_min)
    whole_alert = begin_alert + display_min + end_alert

    messagebox.showinfo("Finished Session", whole_alert)


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
