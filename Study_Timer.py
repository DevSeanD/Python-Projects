"""
Hello this application is designed as a study timer app to aid the user when studying by keeping them motivated
This application uses tkinter as its GUI interface

Created by: DevSeanD

"""

import tkinter as tk
import time
import random


window = tk.Tk()

window.title("Study Timer")

window.geometry("600x400")

# Functions


def study_timer():              # does time conversions

    num_hour = float(entry_field1.get())
    num_hour = num_hour * 3600  # converts hours to seconds

    num_min = float(entry_field2.get())
    num_min = num_min * 60      # converts minuets to seconds

    total_sec = num_min + num_hour

    return total_sec        # prints out a motivation quote dependant upon random generated number


for y in range(1):          # generates one random number
    quote = (random.randint(1, 4))
    
    if quote == 1:
        label_quote1 = tk.Label(text="  Never, never, never give up                                          ")
        label_quote1.grid(column=0, row=5)

    if quote == 2:
        label_quote2 = tk.Label(text="  Quality is not an act, it is a habit                                 ")
        label_quote2.grid(column=0, row=5)

    if quote == 3:
        label_quote2 = tk.Label(text="  It always seems impossible until its done                            ")
        label_quote2.grid(column=0, row=5)

    if quote == 4:
        label_quote2 = tk.Label(text="  Life is 10% what happens to you and 90% how you react to it")
        label_quote2.grid(column=0, row=5)

    if quote == 5:
        label_quote2 = tk.Label(text="  You cannot cross the sea by merely staring at the water")
        label_quote2.grid(column=0, row=5)


def display_timer():            # displays the ending message

    time.sleep(study_timer())
    display_min = float(study_timer() / 60)

    label_fin = tk.Label(text="You have finished your study session of")
    label_fin.grid(column=0, row=6)

    display_fin = tk.Text(master=window, height=1, width=5)
    display_fin.grid(column=0, row=7)
    display_fin.insert(tk.END, display_min)

    label_time = tk.Label(text="minuets")
    label_time.grid(column=0, row=8)


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


