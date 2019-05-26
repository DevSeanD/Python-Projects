"""
This application is a what if cumulative gpa calculator.The user enters their current gpa and then they fill in grade predictions
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
    if n == '4':
        return 4
    if n == '4.0':
        return 4.0
    if n == '3.67':
        return 3.67
    if n == '3.33':
        return 3.33
    if n == '3':
        return 3.0
    if n == '3.0':
        return 3.0
    if n == '2.67':
        return 2.67
    if n == '2.33':
        return 2.33
    if n == '2':
        return 2.0
    if n == '2.0':
        return 2.33
    if n == '2.0':
        return 2.0
    if n == '1.67':
        return 1.67
    if n == '1.33':
        return 1.33
    if n == '1':
        return 1.0
    if n == '1.0':
        return 1.0
    if n == '.67':
        return .67
    if n == '0.0':
        return 0.0
    if n=='100':
        return 4.0
    if n=='99':
        return 4.0
    if n=='98':
        return 4.0
    if n=='97':
        return 4.0
    if n=='96':
        return 4.0
    if n=='95':
        return 4.0
    if n=='94':
        return 4.0
    if n=='93':
        return 4.0
    if n=='92':
        return 4.0
    if n=='91':
        return 3.75
    if n=='90':
        return 3.75
    if n=='89':
        return 3.5
    if n=='88':
        return 3.5
    if n=='87':
        return 3.0
    if n=='86':
        return 3.0
    if n=='85':
        return 3.0
    if n=='84':
        return 3.0
    if n=='83':
        return 3.0
    if n=='82':
        return 3.0
    if n=='81':
        return 2.75
    if n=='80':
        return 2.75
    if n=='79':
        return 2.5
    if n=='78':
        return 2.5
    if n=='77':
        return 2.0
    if n=='76':
        return 2.0
    if n=='75':
        return 2.0
    if n=='74':
        return 2.0
    if n=='73':
        return 2.0
    if n=='72':
        return 2.0
    if n=='71':
        return 1.75
    if n=='70':
        return 1.75
    if n=='69':
        return 1.5
    if n=='68':
        return 1.5
    if n=='67':
        return 1.0
    if n=='66':
        return 1.0
    if n=='65':
        return 1.0
    if n=='64':
        return 1.0
    if n=='63':
        return 1.0
    if n=='62':
        return 1.0
    if n=='61':
        return .75
    if n=='60':
        return .75
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
    cred=cred1=cred2=cred3=cred4=cred5=cred6=cred7=cred8=cred9=cred10=cred11=cred12=cred13=cred14=cred15=cred16=cred17=cred18=cred19=cred20=cred21=cred22=cred23=cred24=cred25=cred26=cred27=cred28=cred29=cred30=cred31=cred32=cred33=cred34=cred35=0.0

    cred = credit_check(credit_val_entry.get())     # assigning cred# to its entry box
    cred1 = credit_check(credit_val_entry1.get())
    cred2 = credit_check(credit_val_entry2.get())
    cred3 = credit_check(credit_val_entry3.get())
    cred4 = credit_check(credit_val_entry4.get())
    cred5 = credit_check(credit_val_entry5.get())
    cred6 = credit_check(credit_val_sec2_entry.get())
    cred7 = credit_check(credit_val_sec2_entry1.get())
    cred8 = credit_check(credit_val_sec2_entry2.get())
    cred9 = credit_check(credit_val_sec2_entry3.get())
    cred10 = credit_check(credit_val_sec2_entry4.get())
    cred11 = credit_check(credit_val_sec2_entry5.get())
    cred12 = credit_check(credit_val_sec3_entry.get())
    cred13 = credit_check(credit_val_sec3_entry1.get())
    cred14 = credit_check(credit_val_sec3_entry2.get())
    cred15 = credit_check(credit_val_sec3_entry3.get())
    cred16 = credit_check(credit_val_sec3_entry4.get())
    cred17 = credit_check(credit_val_sec3_entry5.get())
    cred18 = credit_check(credit_val_sec4_entry.get())
    cred19 = credit_check(credit_val_sec4_entry1.get())
    cred20 = credit_check(credit_val_sec4_entry2.get())
    cred21 = credit_check(credit_val_sec4_entry3.get())
    cred22 = credit_check(credit_val_sec4_entry4.get())
    cred23 = credit_check(credit_val_sec4_entry5.get())
    cred24 = credit_check(credit_val_sec5_entry.get())
    cred25 = credit_check(credit_val_sec5_entry1.get())
    cred26 = credit_check(credit_val_sec5_entry2.get())
    cred27 = credit_check(credit_val_sec5_entry3.get())
    cred28 = credit_check(credit_val_sec5_entry4.get())
    cred29 = credit_check(credit_val_sec5_entry5.get())
    cred30 = credit_check(credit_val_sec6_entry.get())
    cred31 = credit_check(credit_val_sec6_entry1.get())
    cred32 = credit_check(credit_val_sec6_entry2.get())
    cred33 = credit_check(credit_val_sec6_entry3.get())
    cred34 = credit_check(credit_val_sec6_entry4.get())
    cred35 = credit_check(credit_val_sec6_entry5.get())

    # summing up all the credits
    total_cred = cred+cred1+cred2+cred3+cred4+cred5+cred6+cred7+cred8+cred9+cred10+cred11+cred12+cred13+cred14+cred15+cred16+cred17+cred18+cred19+cred20+cred21+cred22+cred23+cred24+cred25+cred26+cred27+cred28+cred29+cred30+cred31+cred32+cred33+cred34+cred35

    grade = grade_scale(class_grade_entry.get())  # calling grade scale function to assign grade points
    grade1 = grade_scale(class_grade_entry1.get())
    grade2 = grade_scale(class_grade_entry2.get())
    grade3 = grade_scale(class_grade_entry3.get())
    grade4 = grade_scale(class_grade_entry4.get())
    grade5 = grade_scale(class_grade_entry5.get())
    grade6 = grade_scale(class_grade_sec2_entry.get())
    grade7 = grade_scale(class_grade_sec2_entry1.get())
    grade8 = grade_scale(class_grade_sec2_entry2.get())
    grade9 = grade_scale(class_grade_sec2_entry3.get())
    grade10 = grade_scale(class_grade_sec2_entry4.get())
    grade11 = grade_scale(class_grade_sec2_entry5.get())
    grade12 = grade_scale(class_grade_sec3_entry.get())
    grade13 = grade_scale(class_grade_sec3_entry1.get())
    grade14 = grade_scale(class_grade_sec3_entry2.get())
    grade15 = grade_scale(class_grade_sec3_entry3.get())
    grade16 = grade_scale(class_grade_sec3_entry4.get())
    grade17 = grade_scale(class_grade_sec3_entry5.get())
    grade18 = grade_scale(class_grade_sec4_entry.get())
    grade19 = grade_scale(class_grade_sec4_entry1.get())
    grade20 = grade_scale(class_grade_sec4_entry2.get())
    grade21 = grade_scale(class_grade_sec4_entry3.get())
    grade22 = grade_scale(class_grade_sec4_entry4.get())
    grade23 = grade_scale(class_grade_sec4_entry5.get())
    grade24 = grade_scale(class_grade_sec5_entry.get())
    grade25 = grade_scale(class_grade_sec5_entry1.get())
    grade26 = grade_scale(class_grade_sec5_entry2.get())
    grade27 = grade_scale(class_grade_sec5_entry3.get())
    grade28 = grade_scale(class_grade_sec5_entry4.get())
    grade29 = grade_scale(class_grade_sec5_entry5.get())
    grade30 = grade_scale(class_grade_sec6_entry.get())
    grade31 = grade_scale(class_grade_sec6_entry1.get())
    grade32 = grade_scale(class_grade_sec6_entry2.get())
    grade33 = grade_scale(class_grade_sec6_entry3.get())
    grade34 = grade_scale(class_grade_sec6_entry4.get())
    grade35 = grade_scale(class_grade_sec6_entry5.get())
    grade_point = grade * cred  # calculating grade points by the corresponding credit
    grade_point1 = grade1 * cred1
    grade_point2 = grade2 * cred2
    grade_point3 = grade3 * cred3
    grade_point4 = grade4 * cred4
    grade_point5 = grade5 * cred5
    grade_point6 = grade6 * cred6
    grade_point7 = grade7 * cred7
    grade_point8 = grade8 * cred8
    grade_point9 = grade9 * cred9
    grade_point10 = grade10 * cred10
    grade_point11 = grade11 * cred11
    grade_point12 = grade12 * cred12
    grade_point13 = grade13 * cred13
    grade_point14 = grade14 * cred14
    grade_point15 = grade15 * cred15
    grade_point16 = grade16 * cred16
    grade_point17 = grade17 * cred17
    grade_point18 = grade18 * cred18
    grade_point19 = grade19 * cred19
    grade_point20 = grade20 * cred20
    grade_point21 = grade21 * cred21
    grade_point22 = grade22 * cred22
    grade_point23 = grade23 * cred23
    grade_point24 = grade24 * cred24
    grade_point25 = grade25 * cred25
    grade_point26 = grade26 * cred26
    grade_point27 = grade27 * cred27
    grade_point28 = grade28 * cred28
    grade_point29 = grade29 * cred29
    grade_point30 = grade30 * cred30
    grade_point31 = grade31 * cred31
    grade_point32 = grade32 * cred32
    grade_point33 = grade33 * cred33
    grade_point34 = grade34 * cred34
    grade_point35 = grade35 * cred35

    total_grade_points = grade_point+grade_point1+grade_point2+grade_point3+grade_point4+grade_point5+grade_point6+grade_point7+grade_point8+grade_point9 + grade_point10 + grade_point11+ grade_point12+grade_point13+grade_point14+grade_point15+grade_point16+grade_point17+grade_point18+grade_point19+grade_point20+grade_point21+grade_point22+grade_point23+grade_point24+grade_point25+grade_point26+grade_point27+grade_point28+grade_point29+grade_point30+grade_point31+grade_point32+grade_point33+grade_point34+grade_point35
    # summing up grade points

    new_gpa = total_grade_points / total_cred

    final_gpa = new_gpa

    final_gpa_string = str(final_gpa)

    final_gpa_label = Label(text="Your gpa is: " + final_gpa_string)
    final_gpa_label.pack(side="bottom")


window = tk.Tk()

window.title("Gpa Calculator")

window.geometry("1080x550")

# Label

# Section 1
semester_number_label = Label(text="Semester 1", font="times 11 bold underline")
semester_number_label.place(x=25, y=0)

class_name_label = Label(text="Class Name")
class_name_label.place(x=25, y=20)

credit_val_label = Label(text="Credits")
credit_val_label.place(x=150, y=20)

class_grade_label = Label(text="Letter Grade")
class_grade_label.place(x=250, y=20)

# Section 2
semester_number_label2 = Label(text="Semester 2", font="times 11 bold underline")
semester_number_label2.place(x=375, y=0)

class_name_label2 = Label(text="Class Name")
class_name_label2.place(x=375, y=20)

credit_val_label = Label(text="Credits")
credit_val_label.place(x=505, y=20)

class_grade_label = Label(text="Letter Grade")
class_grade_label.place(x=605, y=20)

# Section 3
semester_number_label2 = Label(text="Semester 3", font="times 11 bold underline")
semester_number_label2.place(x=725, y=0)

class_name_label2 = Label(text="Class Name")
class_name_label2.place(x=725, y=20)

credit_val_label = Label(text="Credits")
credit_val_label.place(x=860, y=20)

class_grade_label = Label(text="Letter Grade")
class_grade_label.place(x=960, y=20)

# Section 4
semester_number_label = Label(text="Semester 4", font="times 11 bold underline")
semester_number_label.place(x=25, y=225)

class_name_label = Label(text="Class Name")
class_name_label.place(x=25, y=245)

credit_val_label = Label(text="Credits")
credit_val_label.place(x=150, y=245)

class_grade_label = Label(text="Letter Grade")
class_grade_label.place(x=250, y=245)

# Section 5
semester_number_label = Label(text="Semester 5", font="times 11 bold underline")
semester_number_label.place(x=375, y=225)

class_name_label = Label(text="Class Name")
class_name_label.place(x=375, y=245)

credit_val_label = Label(text="Credits")
credit_val_label.place(x=505, y=245)

class_grade_label = Label(text="Letter Grade")
class_grade_label.place(x=605, y=245)

# Section 6
semester_number_label = Label(text="Semester 6", font="times 11 bold underline")
semester_number_label.place(x=725, y=225)

class_name_label = Label(text="Class Name")
class_name_label.place(x=725, y=245)

credit_val_label = Label(text="Credits")
credit_val_label.place(x=860, y=245)

class_grade_label = Label(text="Letter Grade")
class_grade_label.place(x=960, y=245)


# Class Name Entry

# Section 1
x = 0
shift = 0
while x < 6:  # This loop creates 6 entry boxes for the user's class names
    class_name_entry = tk.Entry()
    class_name_entry.place(x=30, y=shift + 35, width=70)
    x += 1
    shift += 30

# Section 2
x = 0
shift = 0
while x < 6:  # This loop creates 6 entry boxes for the user's class names
    class_name_entry = tk.Entry()
    class_name_entry.place(x=380, y=shift + 35, width=70)
    x += 1
    shift += 30
# Section 3
x = 0
shift = 0
while x < 6:  # This loop creates 6 entry boxes for the user's class names
    class_name_entry = tk.Entry()
    class_name_entry.place(x=730, y=shift + 35, width=70)
    x += 1
    shift += 30
# Section 4
x = 0
shift = 225
while x < 6:  # This loop creates 6 entry boxes for the user's class names
    class_name_entry = tk.Entry()
    class_name_entry.place(x=30, y=shift + 35, width=70)
    x += 1
    shift += 30
# Section 5
x = 0
shift = 225
while x < 6:  # This loop creates 6 entry boxes for the user's class names
    class_name_entry = tk.Entry()
    class_name_entry.place(x=380, y=shift + 35, width=70)
    x += 1
    shift += 30
# Section 6
x = 0
shift = 225
while x < 6:  # This loop creates 6 entry boxes for the user's class names
    class_name_entry = tk.Entry()
    class_name_entry.place(x=730, y=shift + 35, width=70)
    x += 1
    shift += 30

# Credit Entry

# Section 1
credit_val_entry = tk.Entry()
credit_val_entry.place(x=160, y=35, width=35)

credit_val_entry1 = tk.Entry()
credit_val_entry1.place(x=160, y=65, width=35)

credit_val_entry2 = tk.Entry()
credit_val_entry2.place(x=160, y=95, width=35)

credit_val_entry3 = tk.Entry()
credit_val_entry3.place(x=160, y=125, width=35)

credit_val_entry4 = tk.Entry()
credit_val_entry4.place(x=160, y=155, width=35)

credit_val_entry5 = tk.Entry()
credit_val_entry5.place(x=160, y=185, width=35)

# Section 2
credit_val_sec2_entry = tk.Entry()
credit_val_sec2_entry.place(x=510, y=35, width=35)

credit_val_sec2_entry1 = tk.Entry()
credit_val_sec2_entry1.place(x=510, y=65, width=35)

credit_val_sec2_entry2 = tk.Entry()
credit_val_sec2_entry2.place(x=510, y=95, width=35)

credit_val_sec2_entry3 = tk.Entry()
credit_val_sec2_entry3.place(x=510, y=125, width=35)

credit_val_sec2_entry4 = tk.Entry()
credit_val_sec2_entry4.place(x=510, y=155, width=35)

credit_val_sec2_entry5 = tk.Entry()
credit_val_sec2_entry5.place(x=510, y=185, width=35)

# Section 3
credit_val_sec3_entry = tk.Entry()
credit_val_sec3_entry.place(x=860, y=35, width=35)

credit_val_sec3_entry1 = tk.Entry()
credit_val_sec3_entry1.place(x=860, y=65, width=35)

credit_val_sec3_entry2 = tk.Entry()
credit_val_sec3_entry2.place(x=860, y=95, width=35)

credit_val_sec3_entry3 = tk.Entry()
credit_val_sec3_entry3.place(x=860, y=125, width=35)

credit_val_sec3_entry4 = tk.Entry()
credit_val_sec3_entry4.place(x=860, y=155, width=35)

credit_val_sec3_entry5 = tk.Entry()
credit_val_sec3_entry5.place(x=860, y=185, width=35)

# Section 4
credit_val_sec4_entry = tk.Entry()
credit_val_sec4_entry.place(x=160, y=260, width=35)

credit_val_sec4_entry1 = tk.Entry()
credit_val_sec4_entry1.place(x=160, y=290, width=35)

credit_val_sec4_entry2 = tk.Entry()
credit_val_sec4_entry2.place(x=160, y=320, width=35)

credit_val_sec4_entry3 = tk.Entry()
credit_val_sec4_entry3.place(x=160, y=350, width=35)

credit_val_sec4_entry4 = tk.Entry()
credit_val_sec4_entry4.place(x=160, y=380, width=35)

credit_val_sec4_entry5 = tk.Entry()
credit_val_sec4_entry5.place(x=160, y=410, width=35)

# Section 5
credit_val_sec5_entry = tk.Entry()
credit_val_sec5_entry.place(x=510, y=260, width=35)

credit_val_sec5_entry1 = tk.Entry()
credit_val_sec5_entry1.place(x=510, y=290, width=35)

credit_val_sec5_entry2 = tk.Entry()
credit_val_sec5_entry2.place(x=510, y=320, width=35)

credit_val_sec5_entry3 = tk.Entry()
credit_val_sec5_entry3.place(x=510, y=350, width=35)

credit_val_sec5_entry4 = tk.Entry()
credit_val_sec5_entry4.place(x=510, y=380, width=35)

credit_val_sec5_entry5 = tk.Entry()
credit_val_sec5_entry5.place(x=510, y=410, width=35)

# Section 6
credit_val_sec6_entry = tk.Entry()
credit_val_sec6_entry.place(x=860, y=260, width=35)

credit_val_sec6_entry1 = tk.Entry()
credit_val_sec6_entry1.place(x=860, y=290, width=35)

credit_val_sec6_entry2 = tk.Entry()
credit_val_sec6_entry2.place(x=860, y=320, width=35)

credit_val_sec6_entry3 = tk.Entry()
credit_val_sec6_entry3.place(x=860, y=350, width=35)

credit_val_sec6_entry4 = tk.Entry()
credit_val_sec6_entry4.place(x=860, y=380, width=35)

credit_val_sec6_entry5 = tk.Entry()
credit_val_sec6_entry5.place(x=860, y=410, width=35)

# Grade Entry

# Section 1
class_grade_entry = tk.Entry()
class_grade_entry.place(x=260, y=35, width=35)

class_grade_entry1 = tk.Entry()
class_grade_entry1.place(x=260, y=65, width=35)

class_grade_entry2 = tk.Entry()
class_grade_entry2.place(x=260, y=95, width=35)

class_grade_entry3 = tk.Entry()
class_grade_entry3.place(x=260, y=125, width=35)

class_grade_entry4 = tk.Entry()
class_grade_entry4.place(x=260, y=155, width=35)

class_grade_entry5 = tk.Entry()
class_grade_entry5.place(x=260, y=185, width=35)

# Section 2
class_grade_sec2_entry = tk.Entry()
class_grade_sec2_entry.place(x=610, y=35, width=35)

class_grade_sec2_entry1 = tk.Entry()
class_grade_sec2_entry1.place(x=610, y=65, width=35)

class_grade_sec2_entry2 = tk.Entry()
class_grade_sec2_entry2.place(x=610, y=95, width=35)

class_grade_sec2_entry3 = tk.Entry()
class_grade_sec2_entry3.place(x=610, y=125, width=35)

class_grade_sec2_entry4 = tk.Entry()
class_grade_sec2_entry4.place(x=610, y=155, width=35)

class_grade_sec2_entry5 = tk.Entry()
class_grade_sec2_entry5.place(x=610, y=185, width=35)

# Section 3
class_grade_sec3_entry = tk.Entry()
class_grade_sec3_entry.place(x=960, y=35, width=35)

class_grade_sec3_entry1 = tk.Entry()
class_grade_sec3_entry1.place(x=960, y=65, width=35)

class_grade_sec3_entry2 = tk.Entry()
class_grade_sec3_entry2.place(x=960, y=95, width=35)

class_grade_sec3_entry3 = tk.Entry()
class_grade_sec3_entry3.place(x=960, y=125, width=35)

class_grade_sec3_entry4 = tk.Entry()
class_grade_sec3_entry4.place(x=960, y=155, width=35)

class_grade_sec3_entry5 = tk.Entry()
class_grade_sec3_entry5.place(x=960, y=185, width=35)

# Section 4
class_grade_sec4_entry = tk.Entry()
class_grade_sec4_entry.place(x=260, y=260, width=35)

class_grade_sec4_entry1 = tk.Entry()
class_grade_sec4_entry1.place(x=260, y=290, width=35)

class_grade_sec4_entry2 = tk.Entry()
class_grade_sec4_entry2.place(x=260, y=320, width=35)

class_grade_sec4_entry3 = tk.Entry()
class_grade_sec4_entry3.place(x=260, y=350, width=35)

class_grade_sec4_entry4 = tk.Entry()
class_grade_sec4_entry4.place(x=260, y=380, width=35)

class_grade_sec4_entry5 = tk.Entry()
class_grade_sec4_entry5.place(x=260, y=410, width=35)

# Section 5
class_grade_sec5_entry = tk.Entry()
class_grade_sec5_entry.place(x=610, y=260, width=35)

class_grade_sec5_entry1 = tk.Entry()
class_grade_sec5_entry1.place(x=610, y=290, width=35)

class_grade_sec5_entry2 = tk.Entry()
class_grade_sec5_entry2.place(x=610, y=320, width=35)

class_grade_sec5_entry3 = tk.Entry()
class_grade_sec5_entry3.place(x=610, y=350, width=35)

class_grade_sec5_entry4 = tk.Entry()
class_grade_sec5_entry4.place(x=610, y=380, width=35)

class_grade_sec5_entry5 = tk.Entry()
class_grade_sec5_entry5.place(x=610, y=410, width=35)

# Section 6
class_grade_sec6_entry = tk.Entry()
class_grade_sec6_entry.place(x=960, y=260, width=35)

class_grade_sec6_entry1 = tk.Entry()
class_grade_sec6_entry1.place(x=960, y=290, width=35)

class_grade_sec6_entry2 = tk.Entry()
class_grade_sec6_entry2.place(x=960, y=320, width=35)

class_grade_sec6_entry3 = tk.Entry()
class_grade_sec6_entry3.place(x=960, y=350, width=35)

class_grade_sec6_entry4 = tk.Entry()
class_grade_sec6_entry4.place(x=960, y=380, width=35)

class_grade_sec6_entry5 = tk.Entry()
class_grade_sec6_entry5.place(x=960, y=410, width=35)


# Button
calc_button = tk.Button(text="Calculate", font=("arial", 10), command=calculate)
calc_button.place(x=475, y=475)

window.mainloop()   
