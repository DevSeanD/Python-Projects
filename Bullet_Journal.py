"""
File Name: Bullet_Journal.py
Author: Sean Dever
Date: 1/24/2021

Dependencies: Tkinter
    Ubuntu/Debian Based systems - "sudo apt-get install python-tk"
"""
import tkinter as tk
import random
import sys
import os
from datetime import date
from tkinter import *

def save():    
    #Obtaining entry values
    var0 = entry_0.get()
    var1 = entry_1.get()
    var2 = entry_2.get()
    var3 = entry_3.get()
    var4 = entry_4.get()
    var5 = entry_5.get()
    var6 = entry_6.get()
    var7 = entry_7.get()
    var8 = entry_8.get()
    var9 = entry_9.get()
    var10 = entry_10.get()
    var11 = entry_11.get()
    var12 = entry_12.get()
    var13 = entry_13.get()
    var14 = entry_14.get()
    var15 = entry_15.get()
    var16 = entry_16.get()
    var17 = entry_17.get()

    #Checking checkbox state
    if check_0_val.get() == 1:
        var0 = ""
    if check_1_val.get() == 1:
        var1 = ""
    if check_2_val.get() == 1:
        var2 = ""
    if check_3_val.get() == 1:
        var3 = ""
    if check_4_val.get() == 1:
        var4 = ""
    if check_5_val.get() == 1:
        var5 = ""
    if check_6_val.get() == 1:
        var6 = ""
    if check_7_val.get() == 1:
        var7 = ""
    if check_8_val.get() == 1:
        var8 = ""
    if check_9_val.get() == 1:
        var9 = ""
    if check_10_val.get() == 1:
        var10 = "" 
    if check_11_val.get() == 1:
        var11 = ""
    if check_12_val.get() == 1:
        var12 = ""
    if check_13_val.get() == 1:
        var13 = ""
    if check_14_val.get() == 1:
        var14 = ""
    if check_15_val.get() == 1:
        var15 = ""
    if check_16_val.get() == 1:
        var16 = ""
    if check_17_val.get() == 1:
        var17 = ""
        # continue adding more lines here
        
    if os.path.exists(command_file_name):
          with open(command_file_name, 'w') as file:
            file.write(var0 + "\n")
            file.write(var1 + "\n")
            file.write(var2 + "\n")
            file.write(var3 + "\n")
            file.write(var4 + "\n")
            file.write(var5 + "\n")
            file.write(var6 + "\n")
            file.write(var7 + "\n")
            file.write(var8 + "\n")
            file.write(var9 + "\n")
            file.write(var10 + "\n")
            file.write(var11 + "\n")
            file.write(var12 + "\n")
            file.write(var13 + "\n")
            file.write(var14 + "\n")
            file.write(var15 + "\n")
            file.write(var16 + "\n")
            file.write(var17 + "\n")
    
    def refresh():
        var0_string.set(var0)
        entry_0 = tk.Entry(width="60",textvariable=var0_string)
        entry_0.grid(row=3,column=1)
        
        var1_string.set(var1)
        entry_1 = tk.Entry(width="60",textvariable=var1_string)
        entry_1.grid(row=4,column=1)

        var2_string.set(var2)
        entry_2 = tk.Entry(width="60",textvariable=var2_string)
        entry_2.grid(row=5,column=1)

        var3_string.set(var3)
        entry_3 = tk.Entry(width="60",textvariable=var3_string)
        entry_3.grid(row=6,column=1)
        
        var4_string.set(var4)
        entry_4 = tk.Entry(width="60",textvariable=var4_string)
        entry_4.grid(row=7,column=1)

        var5_string.set(var5)
        entry_5 = tk.Entry(width="60",textvariable=var5_string)
        entry_5.grid(row=9,column=1)

        var6_string.set(var6)
        entry_6 = tk.Entry(width="60",textvariable=var6_string)
        entry_6.grid(row=10,column=1)

        var7_string.set(var7)
        entry_7 = tk.Entry(width="60",textvariable=var7_string)
        entry_7.grid(row=11,column=1)

        var8_string.set(var8)
        entry_8 = tk.Entry(width="60",textvariable=var8_string)
        entry_8.grid(row=12,column=1)

        var9_string.set(var9)
        entry_9 = tk.Entry(width="60",textvariable=var9_string)
        entry_9.grid(row=13,column=1)
    
        var10_string.set(var10)
        entry_10 = tk.Entry(width="60",textvariable=var10_string)
        entry_10.grid(row=14,column=1)

        var11_string.set(var11)
        entry_11 = tk.Entry(width="60",textvariable=var11_string)
        entry_11.grid(row=15,column=1)
        
        var12_string.set(var12)
        entry_12 = tk.Entry(width="60",textvariable=var12_string)
        entry_12.grid(row=16,column=1)

        var13_string.set(var13)
        entry_13 = tk.Entry(width="60",textvariable=var13_string)
        entry_13.grid(row=18,column=1)

        var14_string.set(var14)
        entry_14 = tk.Entry(width="60",textvariable=var14_string)
        entry_14.grid(row=19,column=1)

        var15_string.set(var15)
        entry_15 = tk.Entry(width="60",textvariable=var15_string)
        entry_15.grid(row=20,column=1)

        var16_string.set(var16)
        entry_16 = tk.Entry(width="60",textvariable=var16_string)
        entry_16.grid(row=21,column=1)

        var17_string.set(var17)
        entry_17 = tk.Entry(width="60",textvariable=var17_string)
        entry_17.grid(row=22,column=1)

 
        #Resetting checkbox states
        check_0_val.set(0)
        check_0 = tk.Checkbutton(var=check_0_val)
        check_0.grid(row=3,column=0)
        
        check_1_val.set(0)
        check_1 = tk.Checkbutton(var=check_1_val)
        check_1.grid(row=4,column=0)
        
        check_2_val.set(0)
        check_2 = tk.Checkbutton(var=check_2_val)
        check_2.grid(row=5,column=0)

        check_3_val.set(0)
        check_3 = tk.Checkbutton(var=check_3_val)
        check_3.grid(row=6,column=0)

        check_4_val.set(0)
        check_4 = tk.Checkbutton(var=check_4_val)
        check_4.grid(row=7,column=0)

        check_5_val.set(0)
        check_5 = tk.Checkbutton(var=check_5_val)
        check_5.grid(row=9,column=0)

        check_6_val.set(0)
        check_6 = tk.Checkbutton(var=check_6_val)
        check_6.grid(row=10,column=0)

        check_7_val.set(0)
        check_7 = tk.Checkbutton(var=check_7_val)
        check_7.grid(row=11,column=0)

        check_8_val.set(0)
        check_8 = tk.Checkbutton(var=check_8_val)
        check_8.grid(row=12,column=0)

        check_9_val.set(0)
        check_9 = tk.Checkbutton(var=check_9_val)
        check_9.grid(row=13,column=0)
        
        check_10_val.set(0)
        check_10 = tk.Checkbutton(var=check_10_val)
        check_10.grid(row=14,column=0)

        check_11_val.set(0)
        check_11 = tk.Checkbutton(var=check_11_val)
        check_11.grid(row=15,column=0)

        check_12_val.set(0)
        check_12 = tk.Checkbutton(var=check_12_val)
        check_12.grid(row=16,column=0)

        check_13_val.set(0)
        check_13 = tk.Checkbutton(var=check_13_val)
        check_13.grid(row=18,column=0)

        check_14_val.set(0)
        check_14 = tk.Checkbutton(var=check_14_val)
        check_14.grid(row=19,column=0)

        check_15_val.set(0)
        check_15 = tk.Checkbutton(var=check_15_val)
        check_15.grid(row=20,column=0) 

        check_16_val.set(0)
        check_16 = tk.Checkbutton(var=check_16_val)
        check_16.grid(row=21,column=0)

        check_17_val.set(0)
        check_17 = tk.Checkbutton(var=check_17_val)
        check_17.grid(row=22,column=0)

    refresh()

        
#Entry Point
window = tk.Tk()

window.title("Bullet Journal")

window.geometry("525x300")

#file to be read and written to
command_file_name = sys.argv[1]

#Button calls the save function
item_number_button = tk.Button(text="Save", font=("arial", 10), command=save)
item_number_button.grid(row=0,column=1)

#Reading the input from the text file
if os.path.exists(command_file_name):
    with open(command_file_name,"r") as test_file:
        var0 = test_file.readline()
        var1 = test_file.readline()
        var2 = test_file.readline()
        var3 = test_file.readline()
        var4 = test_file.readline()
        var5 = test_file.readline()
        var6 = test_file.readline()
        var7 = test_file.readline()
        var8 = test_file.readline()
        var9 = test_file.readline()
        var10 = test_file.readline()
        var11 = test_file.readline()
        var12 = test_file.readline()
        var13 = test_file.readline()
        var14 = test_file.readline()
        var15 = test_file.readline()
        var16 = test_file.readline()
        var17 = test_file.readline()
else:
    with open(command_file_name,"w+") as test_file:
        var0 = ""
        var1 = ""
        var2 = ""
        var3 = ""
        var4 = ""
        var5 = ""
        var6 = ""
        var7 = ""
        var8 = ""
        var9 = ""
        var10 = ""
        var11 = ""
        var12 = ""
        var13 = ""
        var14 = "" 
        var15 = ""
        var16 = ""
        var17 = ""
        

#Getting rid of extra space after content
var0 = var0[:-1]
var1 = var1[:-1]
var2 = var2[:-1]
var3 = var3[:-1]
var4 = var4[:-1]
var5 = var5[:-1]
var6 = var6[:-1]
var7 = var7[:-1]
var8 = var8[:-1]
var9 = var9[:-1]
var10 = var10[:-1]
var11 = var11[:-1]
var12 = var12[:-1]
var13 = var13[:-1]
var14 = var14[:-1]
var15 = var15[:-1]
var16 = var16[:-1]
var17 = var17[:-1]

#Creating string var versions of each line for later use
var0_string = StringVar(value=var0)
var1_string = StringVar(value=var1)
var2_string = StringVar(value=var2)
var3_string = StringVar(value=var3)
var4_string = StringVar(value=var4)
var5_string = StringVar(value=var5)
var6_string = StringVar(value=var6)
var7_string = StringVar(value=var7)
var8_string = StringVar(value=var8)
var9_string = StringVar(value=var9)
var10_string = StringVar(value=var10)
var11_string = StringVar(value=var11)
var12_string = StringVar(value=var12)
var13_string = StringVar(value=var13)
var14_string = StringVar(value=var14)
var15_string = StringVar(value=var15)
var16_string = StringVar(value=var16)
var17_string = StringVar(value=var17)

blankLine = StringVar(value=" ")
blankLineLabel = tk.Label(textvariable=blankLine)
blankLineLabel.grid(row=1,column=1)

sectionTitle = StringVar(value="Routine")
sectionTitleLabel = tk.Label(textvariable=sectionTitle)
sectionTitleLabel.grid(row=2,column=1)

#Creating entries and setting defualt text as varX_string
entry_0 = tk.Entry(width="60",textvariable=var0_string)
entry_0.grid(row=3,column=1)

entry_1 = tk.Entry(width="60",textvariable=var1_string)
entry_1.grid(row=4,column=1)

entry_2 = tk.Entry(width="60",textvariable=var2_string)
entry_2.grid(row=5,column=1)

entry_3 = tk.Entry(width="60",textvariable=var3_string)
entry_3.grid(row=6,column=1)

entry_4 = tk.Entry(width="60",textvariable=var4_string)
entry_4.grid(row=7,column=1)

sectionTitle1 = StringVar(value="School")
sectionTitleLabel1 = tk.Label(textvariable=sectionTitle1)
sectionTitleLabel1.grid(row=8,column=1)

entry_5 = tk.Entry(width="60",textvariable=var5_string)
entry_5.grid(row=9,column=1)

entry_6 = tk.Entry(width="60",textvariable=var6_string)
entry_6.grid(row=10,column=1)

entry_7 = tk.Entry(width="60",textvariable=var7_string)
entry_7.grid(row=11,column=1)

entry_8 = tk.Entry(width="60",textvariable=var8_string)
entry_8.grid(row=12,column=1)

entry_9 = tk.Entry(width="60",textvariable=var9_string)
entry_9.grid(row=13,column=1)

entry_10 = tk.Entry(width="60",textvariable = var10_string)
entry_10.grid(row=14,column=1)

entry_11 = tk.Entry(width="60",textvariable = var11_string)
entry_11.grid(row=15,column=1)

entry_12 = tk.Entry(width="60",textvariable = var12_string)
entry_12.grid(row=16,column=1)

sectionTitle2 = StringVar(value="Self")
sectionTitleLabel2 = tk.Label(textvariable=sectionTitle2)
sectionTitleLabel2.grid(row=17,column=1)

entry_13 = tk.Entry(width="60",textvariable = var13_string)
entry_13.grid(row=18,column=1)

entry_14 = tk.Entry(width="60",textvariable = var14_string)
entry_14.grid(row=19,column=1)

entry_15 = tk.Entry(width="60",textvariable = var15_string)
entry_15.grid(row=20,column=1)

entry_16 = tk.Entry(width="60",textvariable = var16_string)
entry_16.grid(row=21,column=1)

entry_17 = tk.Entry(width="60",textvariable = var17_string)
entry_17.grid(row=22,column=1)

file_name_var = StringVar(value=sys.argv[1])
file_name_label = tk.Label(textvariable=file_name_var)
file_name_label.grid(row=25,column=1)

#Creating checkboxes
check_0_val = IntVar()
check_0 = tk.Checkbutton(var=check_0_val)
check_0.grid(row=3,column=0)

check_1_val = IntVar()
check_1 = tk.Checkbutton(var=check_1_val)
check_1.grid(row=4,column=0)

check_2_val = IntVar()
check_2 = tk.Checkbutton(var=check_2_val)
check_2.grid(row=5,column=0)

check_3_val = IntVar()
check_3 = tk.Checkbutton(var=check_3_val)
check_3.grid(row=6,column=0)

check_4_val = IntVar()
check_4 = tk.Checkbutton(var=check_4_val)
check_4.grid(row=7,column=0)

check_5_val = IntVar()
check_5 = tk.Checkbutton(var=check_5_val)
check_5.grid(row=9,column=0)

check_6_val = IntVar()
check_6 = tk.Checkbutton(var=check_6_val)
check_6.grid(row=10,column=0)

check_7_val = IntVar()
check_7 = tk.Checkbutton(var=check_7_val)
check_7.grid(row=11,column=0)

check_8_val = IntVar()
check_8 = tk.Checkbutton(var=check_8_val)
check_8.grid(row=12,column=0)

check_9_val = IntVar()
check_9 = tk.Checkbutton(var=check_9_val)
check_9.grid(row=13,column=0)

check_10_val = IntVar()
check_10 = tk.Checkbutton(var=check_10_val)
check_10.grid(row=14,column=0)

check_11_val = IntVar()
check_11 = tk.Checkbutton(var=check_11_val)
check_11.grid(row=15,column=0)

check_12_val = IntVar()
check_12 = tk.Checkbutton(var=check_12_val)
check_12.grid(row=16,column=0)

check_13_val = IntVar()
check_13 = tk.Checkbutton(var=check_13_val)
check_13.grid(row=18,column=0)

check_14_val = IntVar()
check_14 = tk.Checkbutton(var=check_14_val)
check_14.grid(row=19,column=0)

check_15_val = IntVar()
check_15 = tk.Checkbutton(var=check_15_val)
check_15.grid(row=20,column=0)

check_16_val = IntVar()
check_16 = tk.Checkbutton(var=check_16_val)
check_16.grid(row=21,column=0)

check_17_val = IntVar()
check_17 = tk.Checkbutton(var=check_17_val)
check_17.grid(row=22,column=0)


window.mainloop()
