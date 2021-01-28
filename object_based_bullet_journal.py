import os
from tkinter import *


def save():
    with open(txt_database, "w+") as my_file:
        entries_that_arent_empty = []
        for entry in InpEntry.EntryObjects:
            if entry.text.get() != "":
                my_file.write(entry.text.get() + "\n")
                entries_that_arent_empty.append(entry)
        checkboxes = "".join([str(entry.checked.get()) for entry in InpEntry.EntryObjects if entry in entries_that_arent_empty])
        my_file.write(checkboxes)
        my_file.close()


window = Tk()
window.title("OO take on Bullet Journal")
window.geometry("625x400")
txt_database = "txt.txt"

btn_save = Button(master=window, text="Save", font=("arial", 10), command=save)
btn_save.pack()

list_of_entries = []
if os.path.exists(txt_database):
    with open(txt_database, "r") as my_file:
        """
            Comprehensions are awesome!
        """
        list_of_values = [line for line in my_file.readlines()]
        list_of_entries = [line[:-1] for line in list_of_values][:-1]
        try:
            check_boxes = list_of_values[-1]
            if check_boxes.endswith("\n"):
                check_boxes = str(check_boxes)[:-1]
        except:
            check_boxes = "0"*len(list_of_entries)
        my_file.close()
else:
    with open(txt_database, "w+") as my_file:
        my_file.write("mock_data \n 1")
        my_file.close()


check_boxes = [int(x) for x in check_boxes]
print(check_boxes)


class InpEntry(Frame):
    """
    The list of objects made from this class will be accessible through
    class variable by typing InpEntry.EntryObjects.
    It's useful when we want to use data common to all instances a class, for example Players
    The list is also 'private' to the class. It minimizes possibility of accidentally overriding it later in code
    by private I mean it uses the namespace InpEntry. InpEntry.[thing]
    just like methods with @classmethod and variables with @property decorator
    """
    EntryObjects = []

    def __init__(self, text=None, width=60):
        """
        By using the super() We refer to the Frame class my InpEntry inherits from.
        It adds to our object all the initial (.__init__) properties a Frame would have, as if you used tk.Frame(master=window)
        """
        super().__init__(master=window)
        """
        This stuff bellow will be executed for every instance of our object. This means generating
        a check_box with corresponding IntVar and entry with StringVar, without the need to repeat code.
        By using master=self you can put these inside your soon to be tk object.
        """
        self.text = StringVar(value=text)
        self.entry = Entry(master=self, width=width, textvariable=self.text)
        self.checked = IntVar()
        self.check_box = Checkbutton(master=self, variable=self.checked)
        self.set_check_box_value(check_boxes)
        InpEntry.EntryObjects.append(self)

    def set_check_box_value(self, check_boxes):
        if check_boxes[len(InpEntry.EntryObjects)] == 1:
            self.checked.set(1)
            self.check_box.select()
        else:
            pass
            self.checked.set(0)

    def pack_both(self):
        self.check_box.pack(side=LEFT)
        self.entry.pack(side=RIGHT)
        self.pack()

    """
    Class methods are used on our class instead of particular objects.
    cls.EntryObjects === InpEntry.EntryObjects
    """
    @classmethod
    def pack_all_entries(cls):
        for entry_frame in cls.EntryObjects:
            entry_frame.pack_both()


def append_entry():
    """
    Add another input
    """
    check_boxes.append(0)
    e = InpEntry()
    e.pack_both()
    window.update()


for entry in list_of_entries:
    e = InpEntry(entry)
    """
    Using common methods on lists, instead of referring to every object separately shortens the code
    and makes it easier to read. By a lot. There's a principle in programming called DRY(Don't repeat yourself)
    It means that you should generally strive to minimize the amount of reoccurring code,
    like int: player_1_score, int: player_2_score, int: player_3_score, generally by holding these in 
    collections or objects (lists, dicts etc.) and using loops, list comprehensions
    """
InpEntry.pack_all_entries()

btn_save = Button(master=window, text="Add entry", font=("arial", 10), command=append_entry)
btn_save.pack()


window.mainloop()
