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
    def __init__(self,row_val,col_val,str_val=None):
        if str_val is None:
            str_val = StringVar(value="")
        else:
            str_val = StringVar(value=str_val)
        self.entry = tk.Entry(width="60",textvariable=str_val)
        self.entry.grid(row=row_val,column=col_val)
        
class check_box():
    def __init__(self,row_val,col_val,check_state=None):
        if check_state is None:
           self.check_state = IntVar()
        if check_state == 1:
            self.check_state = IntVar(value=1)
        self.check = tk.Checkbutton(var=self.check_state)
        self.check.grid(row=row_val,column=col_val)

def save():
    pass


check_box_1 = check_box(1,0)
check_box_2 = check_box(2,0,1)

entry_1 = entry_box(1,1)
entry_2 = entry_box(2,1,"Test")

window.mainloop()
