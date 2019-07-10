            to_do_item.place(x=85, y=110 + y_shift)
            counter += 1
            y_shift += 35

        if counter > 16:   # adjust the resolution if the number of list items is greater than 15
            window.geometry("600x1000")

        if counter > item_number:   # when the counter is more than the number of items break the while statement
            break


window = tk.Tk()

window.title("To Do List")

window.geometry("600x600")

# Label
welcome_label = Label(text="Hello, welcome to a simple To-Do list app")
welcome_label.place(x=150, y=10)

item_number_label = Label(text="How many items would you like?")
item_number_label.place(x=30, y=30)

#   Entry
item_number_entry = tk.Entry()
item_number_entry.place(x=30, y=50)

#   Button
item_number_button = tk.Button(text="Enter", font=("arial", 10), command=to_do)
item_number_button.place(x=30, y=75)
y_shift = 0
counter = 0


window.mainloop()

                                                                                                                              53,1          Bot
