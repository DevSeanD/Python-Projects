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

class label():
    def __init__(self,str_val,row_val,col_val):
        sectionTitle = StringVar(value=str_val)
        sectionTitleLabel = tk.Label(textvariable=sectionTitle)
        sectionTitleLabel.grid(row=row_val,column=col_val)


def save():
    pass


routineLabel = label("Routine",0,1)
schoolLabel = label("School",14,1)
selfLabel = label("Self",23,1)

check_box_1 = check_box(1,0)
check_box_2 = check_box(2,0,1)
check_box_3 = check_box(3,0)
check_box_4 = check_box(4,0)
check_box_5 = check_box(5,0)
check_box_6 = check_box(7,0)
check_box_7 = check_box(8,0)
check_box_8 = check_box(9,0)
check_box_9 = check_box(10,0)
check_box_10 = check_box(11,0)
check_box_11 = check_box(12,0)
check_box_12 = check_box(13,0)
check_box_13 = check_box(15,0)
check_box_14 = check_box(16,0)
check_box_15 = check_box(17,0)
check_box_16 = check_box(18,0)
check_box_17 = check_box(19,0)
check_box_18 = check_box(20,0)
check_box_19 = check_box(21,0)
check_box_20 = check_box(22,0)

entry_1 = entry_box(1,1)
entry_2 = entry_box(2,1,"Test")

window.mainloop()
