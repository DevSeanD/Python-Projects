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
schoolLabel = label("School",6,1)
selfLabel = label("Self",15,1)

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
check_box_13 = check_box(14,0)
check_box_14 = check_box(16,0)
check_box_15 = check_box(17,0)
check_box_16 = check_box(18,0)
check_box_17 = check_box(19,0)
check_box_18 = check_box(20,0)
 
entry_1 = entry_box(1,1)
entry_2 = entry_box(2,1,"Test")
entry_3 = entry_box(3,1)
entry_4 = entry_box(4,1)
entry_5 = entry_box(5,1)
entry_6 = entry_box(7,1)
entry_7 = entry_box(8,1)
entry_8 = entry_box(9,1)
entry_9 = entry_box(10,1)
entry_10 = entry_box(11,1)
entry_11 = entry_box(12,1)
entry_12 = entry_box(13,1)
entry_13 = entry_box(14,1)
entry_14 = entry_box(16,1)
entry_15 = entry_box(17,1)
entry_16 = entry_box(18,1)
entry_17 = entry_box(19,1)
entry_18 = entry_box(20,1)

window.mainloop()
