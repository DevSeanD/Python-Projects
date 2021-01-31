"""
File: OO_Bullet_Journal.py 
Description: This is a revision of my Bullet_Journal.py program. These revisions and efficiency are sourced from @kriskros34 who has been extremely kind and helpful. 

Issues with my old code mostly consisted of a high level of repetition which can be solved by accepting an object oriented model.
"""
import os 
import tkinter as tk
from tkinter import *

window = Tk()
window.title("Bullet Journal")
window.geometry("625x400")

class entry_box():
    def __init__(self,row_val,col_val,str_val):
        self.entry = tk.Entry(width="60",textvariable=str_val)
        self.entry.grid(row=row_val,column=col_val)
        
class check_box():
    def __init__(self,row_val,col_val,check_state=None):
        if check_state is None:
            check_state = IntVar()

        self.check = tk.Checkbutton(var=check_state)
        self.check.grid(row=row_val,column=col_val)


def save():
    pass


check_box_1 = check_box(1,0)

str_var_1 = StringVar(value="Test")
entry_1 = entry_box(1,1,str_var_1)


window.mainloop()
