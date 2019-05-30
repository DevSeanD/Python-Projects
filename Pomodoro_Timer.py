"""
Hello this application is designed to function as a Pomodoro timer. It consist of four 25 minute study sessions with 5 minute breaks in between. After 4 study sessions have completed there will be a 20 minute break
Created by: DevSeanD
"""

import tkinter as tk 
import time 
from tkinter import ttk
from tkinter import messagebox  
import threading

window = tk.Tk()
window.title("Pomodoro Timer")
window.geometry("500x500")

def First_Study_Sesh():
    label_blank = tk.Label(text=" ")
    label_blank.pack(side="top")
    label_break = tk.Label(text="Study Session 1 done! 5 min break starts now!")
    label_break.pack(side="top")

def Second_Study_Sesh():
    label_second_sesh = tk.Label(text= " Break 1 is done! Study Session 2 begins now!")
    label_second_sesh.pack(side="top")

def Third_Study_Sesh():
    label_third_sesh = tk.Label(text="Study Session 2 is done! 5 min break starts now!")
    label_third_sesh.pack(side="top")

def Fourth_Study_Sesh():
    label_fourth_sesh = tk.Label(text="Break 2 is done! Study Session 3 begins now!")
    label_fourth_sesh.pack(side="top")

def Fifth_Study_Sesh():
    label_fifth_sesh = tk.Label(text="Study Session 3 is done! 5 min break start now!")
    label_fifth_sesh.pack(side="top")

def Sixth_Study_Sesh():
    label_sixth_sesh = tk.Label(text="Break 3 is done! Study Session 4 begins now!")
    label_sixth_sesh.pack(side="top")

def Seventh_Study_Sesh():
    label_seventh_sesh = tk.Label(text="Pomodoro Session Complete!")
    label_seventh_sesh.pack(side="top")


def Timer_Start():
    timer_start = threading.Timer(1500.0,First_Study_Sesh) # after 10 seconds function First_Study_Sesh will run
    timer_start.start()

    timer_start_1 = threading.Timer(1800.0, Second_Study_Sesh) # after 15 seconds function Break_Five will run
    timer_start_1.start()

    timer_start_2 = threading.Timer(3300.0, Third_Study_Sesh) # after 25 seconds function Third_study_sesh will run
    timer_start_2.start()

    timer_start_3 = threading.Timer(3600.0, Fourth_Study_Sesh) # after 15 seconds function Fourth_study_sesh will run 
    timer_start_3.start()

    timer_start_4 = threading.Timer(5100.0, Fifth_Study_Sesh)
    timer_start_4.start()

    timer_start_5 = threading.Timer(5400.0, Sixth_Study_Sesh)
    timer_start_5.start()

    timer_start_6 = threading.Timer(6900.0, Seventh_Study_Sesh)
    timer_start_6.start()

# Lables
label_welcome = tk.Label(text="Welcome to Pomodoro Timer!",bd=1)
label_welcome.pack(side="top")

#Buttons
start_button = tk.Button(text="Start Timer", command=Timer_Start)
start_button.pack(side="top")

window.mainloop()
