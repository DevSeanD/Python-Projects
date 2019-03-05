"""
Hello this application is designed as a study timer app to aid the user when studying
This application uses tkinter as its GUI interface

Created by: DevSeanD

"""

import tkinter as tk
import random

window = tk.Tk()

window.title("Study Timer")

window.geometry("600x400")

# Functions


def study_timer():
    num_hour = float(entry_field1.get())
    num_hour = num_hour * 3600  # converts hours to seconds

    num_min = float(entry_field2.get())
    num_min = num_min * 60      # converts minuets to seconds

    total_sec = num_min + num_hour

    return total_sec


def display_timer():
    import time
    time.sleep(study_timer())
    display_min = float(study_timer() / 60)

    label_fin = tk.Label(text="You have finished your study session of")
    label_fin.grid(column=1, row=4)

    display_fin = tk.Text(master=window, height=2, width=5)
    display_fin.grid(column=1, row=5)
    display_fin.insert(tk.END, display_min)

    label_time = tk.Label(text="minuets")
    label_time.grid(column=1, row=6)


# LABEL
title = tk.Label(text="Hello welcome to Study Timer", font=("Times New Roman", 15))
title.grid(column=0, row=0)

label_hour = tk.Label(text="How many hours?")
label_hour.grid(column=0, row=1)

label_min = tk.Label(text="How many minuets?")
label_min.grid(column=0, row=2)


# BUTTON
button1 = tk.Button(text="Start", command=display_timer)
button1.grid(column=1, row=3)

# Entry Field
entry_field1 = tk.Entry()
entry_field1.grid(column=1, row=1)

entry_field2 = tk.Entry()
entry_field2.grid(column=1, row=2)


window.mainloop()


