"""
This application is a what if gpa calculator.The user enters their current gpa and then they fill in grade predictions
in order to see the effect on gpa.if current gpa is not entered then the calculator will simply calculate the gpa for
the given term.
Created by: DevSeanD
"""

import tkinter as tk
from tkinter import *


def grade_scale(n):  # Works similar to a switch statement to swap strings for float values
    if n == "A+":
        return 4.0
    if n == 'a+':
        return 4.0
    if n == "A":
        return 4.0
    if n == 'a':
        return 4.0
    if n == 'A-':
        return 3.67
    if n == 'a-':
        return 3.67
    if n == 'B+':
        return 3.33
    if n == 'b+':
        return 3.33
    if n == 'B':
        return 3.0
    if n == 'b':
        return 3.0
    if n == 'B-':
        return 2.67
    if n == 'b-':
        return 2.67
    if n == 'C+':
        return 2.33
    if n == 'c+':
        return 2.33
    if n == 'C':
        return 2.0
    if n == 'c':
        return 2.0
    if n == 'C-':
        return 1.67
    if n == 'D+':
        return 1.33
    if n == 'd+':
        return 1.33
    if n == 'D':
        return 1.0
    if n == 'd':
        return 1.0
    if n == 'D-':
        return .67
    if n == 'd-':
        return .67
    if n == 'F':
        return 0.0
    if n == 'f':
        return 0.0
    else:
        return 0.0


def credit_check(a):
    if len(a) == 0:
        return 0.0
    if len(a) == 1:
        b = float(a)
        if b >= 7:
            cred_error_label = Label(text="!You cannot enter a credit value higher than 6!")
            cred_error_label.place(x=25, y=295)
        else:
            return float(a)


def calculate():  # test if the entry box is empty, if it is then it will be assigned 0
    cred = 0.0
    cred = credit_check(credit_val_entry.get())

    cred1 = 0.0
    cred1 = credit_check(credit_val_entry1.get())

    cred2 = 0.0
    cred2 = credit_check(credit_val_entry2.get())

    cred3 = 0.0
    cred3 = credit_check(credit_val_entry3.get())

    cred4 = 0.0
    cred4 = credit_check(credit_val_entry4.get())

    cred5 = 0.0
    cred5 = credit_check(credit_val_entry5.get())

    total_cred = cred + cred1 + cred2 + cred3 + cred4 + cred5  # summing up all the credits

    grade = grade_scale(class_grade_entry.get())  # calling grade scale function to assign grade points
    grade1 = grade_scale(class_grade_entry1.get())
    grade2 = grade_scale(class_grade_entry2.get())
    grade3 = grade_scale(class_grade_entry3.get())
    grade4 = grade_scale(class_grade_entry4.get())
    grade5 = grade_scale(class_grade_entry5.get())

    grade_point = grade * cred  # calculating grade points by the corresponding credit
    grade_point1 = grade1 * cred1
    grade_point2 = grade2 * cred2
    grade_point3 = grade3 * cred3
    grade_point4 = grade4 * cred4
    grade_point5 = grade5 * cred5

    total_grade_points = grade_point + grade_point1 + grade_point2 + grade_point3 + grade_point4 + grade_point5  # summing up grade points

    new_gpa = 0.0

    new_gpa = total_grade_points / total_cred

    current_gpa = 0.0
    if len(curr_gpa_entry.get()) == 0:  # if the user does not enter a current gpa it will only calculate the new gpa
        current_gpa = new_gpa
    if len(curr_gpa_entry.get()) >= 1:
        current_gpa = float(curr_gpa_entry.get())
        if current_gpa > 4.00:  # gpa values may not be over 4.0
            curr_error_label = Label(text="!You cannot enter a current gpa higher than 4.0!")
            curr_error_label.place(x=25, y=325)

    final_gpa = (new_gpa + current_gpa) / 2

    final_gpa_string = str(final_gpa)

    final_gpa_label = Label(text="Your gpa is: " + final_gpa_string)
    final_gpa_label.pack(side="bottom")


window = tk.Tk()

window.title("Gpa Calculator")

window.geometry("350x420")

# Label
curr_gpa_label = Label(text="Current Gpa: ")
curr_gpa_label.place(x=25, y=10)

class_name_label = Label(text="Class Name")
class_name_label.place(x=25, y=50)

credit_val_label = Label(text="Credits")
credit_val_label.place(x=150, y=50)

class_grade_label = Label(text="Letter Grade")
class_grade_label.place(x=250, y=50)

# Entry
curr_gpa_entry = tk.Entry()
curr_gpa_entry.place(x=120, y=10, width=50)

x = 0
shift = 0
while x < 6:  # This loop creates 6 entry boxes for the user's class names
    class_name_entry = tk.Entry()
    class_name_entry.place(x=30, y=shift + 70, width=70)
    x += 1
    shift += 30

# Credit Entry

credit_val_entry = tk.Entry()
credit_val_entry.place(x=160, y=70, width=35)

credit_val_entry1 = tk.Entry()
credit_val_entry1.place(x=160, y=100, width=35)

credit_val_entry2 = tk.Entry()
credit_val_entry2.place(x=160, y=130, width=35)

credit_val_entry3 = tk.Entry()
credit_val_entry3.place(x=160, y=160, width=35)

credit_val_entry4 = tk.Entry()
credit_val_entry4.place(x=160, y=190, width=35)

credit_val_entry5 = tk.Entry()
credit_val_entry5.place(x=160, y=220, width=35)

# Grade Entry

class_grade_entry = tk.Entry()
class_grade_entry.place(x=260, y=70, width=35)

class_grade_entry1 = tk.Entry()
class_grade_entry1.place(x=260, y=100, width=35)

class_grade_entry2 = tk.Entry()
class_grade_entry2.place(x=260, y=130, width=35)

class_grade_entry3 = tk.Entry()
class_grade_entry3.place(x=260, y=160, width=35)

class_grade_entry4 = tk.Entry()
class_grade_entry4.place(x=260, y=190, width=35)

class_grade_entry5 = tk.Entry()
class_grade_entry5.place(x=260, y=220, width=35)

# Button

calc_button = tk.Button(text="Calculate", font=("arial", 10), command=calculate)
calc_button.place(x=125, y=260)

window.mainloop()
