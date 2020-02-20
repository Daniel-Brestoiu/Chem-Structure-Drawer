import tkinter as tkinter
import random

root = tkinter.Tk()                
root.title("Chem Structure Drawer")
#Making Main Screen

width = root.winfo_width()
height = root.winfo_height()
#Width and Height of the Screen, not used tho

root.geometry("500x500+650+250")
root.minsize(width = 500, height = 500)
root.maxsize(width = 500, height = 500)
#Setting main screen size


work_space = tkinter.Canvas(root, width = 500, height = 425)
work_space["background"] = "#A9EDFF"
work_space.pack()
#Add a canvas to main screen, to be able to do stuff



#Made main frame and stuff above, now I write my functions

all_boxes = []

def make_box():
    x_pos = random.randint(50 , 450)
    y_pos = random.randint(50 , 400)
    box = tkinter.Entry(root, width = 2)
    work_space.create_window(x_pos, y_pos, window = box)

def clear_all():
    work_space.delete("all")




#might really have to change boxes to a class
#Tragic

"""
Box class would include:
x pos
y pos
4 potential lines
Text field for entry

I could have user move pos using cursor position

Maybe add the objects to a list or a dict or smth, so I can reference to them, without giving a name? 
"""



add_box_button = tkinter.Button(root, text = "Add Box", width = 25, height = 2, command = make_box)
add_box_button.place( x = 140, y = 448)
#Add a box button, y = 465 makes direct contact the best

save_button = tkinter.Button(root, text = "SAVE" , width = 10, height = 2, image = None)
save_button.place(x = 390, y = 448)
#Make Save button, later make the save button look like a floppy disk save :D

erase_button = tkinter.Button(root, text = "Clear All" , width = 10, height = 2, command = clear_all)
erase_button.place(x = 25, y = 448)


#Main buttons and stuff would be added here.

root.mainloop()