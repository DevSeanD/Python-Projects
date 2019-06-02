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
window.geometry("650x650")

counter = 0
# setting the checkbox values to true, so when they are executed they will be checked 
check_val_1 = tk.BooleanVar()
check_val_1.set(True)

check_val_2 = tk.BooleanVar()
check_val_2.set(True)

check_val_3 = tk.BooleanVar()
check_val_3.set(True)

# Made each section its own function for simplicity
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
    label_seventh_sesh = tk.Label(text="Pomodoro Session Complete!(25 min break)")
    label_seventh_sesh.pack(side="top")

def Check_box_1_set():
    check_box_complete = tk.Checkbutton(variable=check_val_1).place(x=120,y=135)

def Check_box_2_set():
    check_box_complete_2 = tk.Checkbutton(variable=check_val_2).place(x=120,y=315)

def Check_box_3_set():
    check_box_complete_3 = tk.Checkbutton(variable=check_val_3).place(x=120,y=490)

# Main function of program containing the secquencing 
def Timer_Start(): 
    label_sesh_1= tk.Label(text="Session 1")
    label_sesh_1.place(x=50,y=135)

    label_seshs_2 = tk.Label(text="Session 2")
    label_seshs_2.place(x=50,y=315)

    label_seshs_3 = tk.Label(text="Session 3")
    label_seshs_3.place(x=50,y=490)

    timer_start = threading.Timer(1500.0,First_Study_Sesh) # each interval = time(min) * 60 + previous time. In order to not overlap threading timers 
    timer_start.start()
 
    timer_start_1 = threading.Timer(1800.0, Second_Study_Sesh) 
    timer_start_1.start()
 
    timer_start_2 = threading.Timer(3300.0, Third_Study_Sesh) 
    timer_start_2.start()
 
    timer_start_3 = threading.Timer(3600.0, Fourth_Study_Sesh) 
    timer_start_3.start()
 
    timer_start_4 = threading.Timer(5100.0, Fifth_Study_Sesh)
    timer_start_4.start()
 
    timer_start_5 = threading.Timer(5400.0, Sixth_Study_Sesh)
    timer_start_5.start()
 
    timer_start_6 = threading.Timer(6900.0, Seventh_Study_Sesh)
    timer_start_6.start()

    label_blank_1 = tk.Label(text=" ")
    label_blank_1.pack(side="top")
    
    global counter # converting counter into a global variable then incrementing by 1
    counter += 1
    
    # Depending on what session is completed the checkbox will correspond
    if counter == 1:
        check_button_1 = threading.Timer(6900.0, Check_box_1_set)
        check_button_1.start()
    if counter == 2:
        check_button_2 =threading.Timer(6900.0, Check_box_2_set)
        check_button_2.start()
    if counter == 3:
        check_button_3 = threading.Timer(6900.0,Check_box_3_set)
        check_button_3.start()
# Lables
label_welcome = tk.Label(text="Welcome to Pomodoro Timer!",bd=1)
label_welcome.pack(side="top")

#Buttons
start_button = tk.Button(text="Start Timer", command=Timer_Start)
start_button.pack(side="top")


window.mainloop()
