"""
Hello, this application is designed to calculate semester and cumulative gpa. 
Created by: DevSeanD
"""


print("Hello, this program is designed to calculate semester gpa and cumulative gpa")
print("")


def gpa_calculation(x, y):
    """
    !This module is designed to calculate gpa with the given parameters x and y!
    :param x: grade points and total gpa points
    :param y: total credits and total semesters
    :return:
    """
    return x / y


user_sel = 0   # user selection

while (user_sel != 1) and (user_sel != 2):
    print("How would you like to calculate gpa")
    print("")
    print("For Semester Gpa enter 1")
    print("For Cumulative Gpa enter 2")
    user_sel = int(input())


if user_sel == 1:
    num_classes = 0.0   # how many classes are you taking
    cred_worth = 0.0    # how much is each class worth in credits
    class_grade = 0.0   # what your grade in the class was
    total_cred = 0.0    # total number of credits
    grade_points = 0.0  # total grade points
    counter = 1

    print("===================")
    print("Semester Calculator")
    print("===================")

    while (num_classes <= 0) and (num_classes <= 11):                 # num_classes must be between 1-10
        num_classes = float(input("How want classes are you taking this semester"))
        print(" ")

        while counter <= num_classes:
                print("how many credits is class", counter, "worth")
                cred_worth = float(input())
                if (cred_worth >= 1) and (cred_worth <= 6):           # credit worth must be between 1-6
                    counter += 1
                    total_cred += cred_worth
                    print("To enter a letter type the letter to the right of the letter")
                    print("+---------------------------+")
                    print("| A+ (1)   A (2)    A- (3)  |")
                    print("|                           |")
                    print("| B+ (4)   B (5)    B- (6)  |")
                    print("|                           |")
                    print("| C+ (7)   C (8)    C- (9)  |")
                    print("|                           |")
                    print("| D+ (10)  D (11)   D- (12) |")
                    print("|                           |")
                    print("|          F (13)           |")
                    print("+---------------------------+")
                    class_grade = float(input())
                    if (class_grade >= 1) and (class_grade <= 13):    # the value must be from the menu
                        if class_grade == 1:  # Assigning menu value to gpa
                            class_grade = 4.3
                        if class_grade == 2:
                            class_grade = 4.0
                        if class_grade == 3:
                            class_grade = 3.7
                        if class_grade == 4:
                            class_grade = 3.3
                        if class_grade == 5:
                            class_grade = 3.0
                        if class_grade == 6:
                            class_grade = 2.7
                        if class_grade == 7:
                            class_grade = 2.3
                        if class_grade == 8:
                            class_grade = 2.0
                        if class_grade == 9:
                            class_grade = 1.7
                        if class_grade == 10:
                            class_grade = 1.3
                        if class_grade == 11:
                            class_grade = 1.0
                        if class_grade == 12:
                            class_grade = .07
                        if class_grade == 13:
                            class_grade = 0.0
                        grade_points += class_grade * cred_worth
                        if counter > num_classes:
                            print("========================================")
                            print("Your Semester Gpa is:", gpa_calculation(grade_points, total_cred))  # call function
                            print("========================================")

if user_sel == 2:
    total_sem = 0.0         # total semesters
    sem_gpa = 0.0           # semester gpa
    total_sem_gpa = 0.0     # total of all semesters gpa
    counter = 1             # counter for display

    print("=====================")
    print("Cumulative Calculator")
    print("=====================")

    while(total_sem <=0) and (total_sem <= 15):         # must enter between 1-15 total semesters
        total_sem = float(input("How many semesters have you taken?"))
        print(" ")
    while total_sem >= counter:
        print("What was your gpa for semester", counter)
        sem_gpa = float(input())
        if (sem_gpa <= 4.0) and (sem_gpa >= 0.0):       # grade must be between 0.0 and 4.0
            counter += 1
            total_sem_gpa += sem_gpa                    # adds semester gpa to the gpa total
        if counter > total_sem:                         # if the counter is more than total semesters then calculate
            print("==========================================")
            print("Your Cumulative Gpa is :", gpa_calculation(total_sem_gpa, total_sem))  # call function
print("==========================================")
