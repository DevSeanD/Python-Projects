"""
File: OO_Bullet_Journal.py 
Description: This is a revision of my Bullet_Journal.py program. These revisions and efficiency are sourced from @kriskros34 who has been extremely kind and helpful. 

Issues with my old code mostly consisted of a high level of repetition which can be solved by accepting an object oriented model.
"""
import os 
import tkinter as tk
from tkinter import *
from datetime import datetime

window = tk.Tk()
window.title("Bullet Journal")
window.geometry("625x400")

class entry_box():
    def __init__(self,row_val,col_val,str_val=None):
        if str_val is None:
            str_val = StringVar(value="")
        else:
            str_val = StringVar(value=str_val)
        self.entry = tk.Entry(width="80",textvariable=str_val)
        self.entry.grid(row=row_val,column=col_val)
        
class check_box():
    def __init__(self,row_val,col_val,check_state=None):
        if check_state is None:
           self.check_state = IntVar()
        if check_state == 1:
            self.check_state = IntVar(value=1)
        self.check = tk.Checkbutton(var=self.check_state)
        self.check.grid(row=row_val,column=col_val)
    def selectCheckBox(self):
        self.check.select()
    def checkState(self):
        return self.check_state.get()

class label():
    def __init__(self,str_val,row_val,col_val):
        sectionTitle = StringVar(value=str_val)
        sectionTitleLabel = tk.Label(textvariable=sectionTitle)
        sectionTitleLabel.grid(row=row_val,column=col_val)


def save():
    entryText = []
    for entry in range(len(entryBoxArray)): # puts all entry text into entryText array 
        entryText.append(entryBoxArray[entry].entry.get())
    
    strCheck = "" # inital state of checkbox state string
    # processing checkbox states 
    for checkbox in range(len(checkBoxArray)):
        if checkBoxArray[checkbox].checkState() == 1:
            strCheck += "1"
        else:
            strCheck += "0"

    # writing entry text to journal file
    if os.path.exists(commandFileName):
        with open(commandFileName, 'w') as file:
            for entry in entryText:
                file.write(entry + "\n")
            # writing strCheck to jounral file
            file.write(strCheck + "\n") 



# Entry Points

# Command line argument inputs
if(len(sys.argv) == 1):
    date = datetime.now()
    date = str(date).split()
    commandFileName = date[0] + ".txt"

if(len(sys.argv) == 2):
    #file to be read and written to
    commandFileName = sys.argv[1]

if(len(sys.argv) == 3):
    if(sys.argv[1] == "cp"):
        date = datetime.now()
        date = str(date).split()
        commandFileName = date[0] + ".txt"
        sourceFile = sys.argv[2]
        with open(sourceFile,"r") as srFile:
            with open(commandFileName,"w") as destFile:
                 for line in srFile:
                    destFile.write(line)
            destFile.close()
        srFile.close()
    else:
        print("Invalid command")
        quit()

# Button
saveButton = tk.Button(text = " Save ",font = ("arial",15),command = save)
saveButton.grid(row = "0",column = "1")

# Labels
routineLabel = label("Routine",1,1)
schoolLabel = label("School",7,1)
selfLabel = label("Self",18,1)

checkBoxArray = [] # Array that holds check box objects
spaceCount = 2 
for check in range(22):
    if(spaceCount == 7 or spaceCount == 18):
        pass
    else:
        checkBoxArray.append(check_box(spaceCount,0))
    spaceCount += 1

checkBoxArray[2].selectCheckBox()

entryBoxArray = [] # Array that holds entry box objects
spaceCount = 2
for entry in range(22):
    if(spaceCount == 7 or spaceCount == 18):
        pass
    else:
        entryBoxArray.append(entry_box(spaceCount,1))
    spaceCount += 1 
    
commandFileName = "test.txt"

window.mainloop()
