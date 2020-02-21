import tkinter as tkinter
import random
import time

global root
global work_space
global all_boxes
root = tkinter.Tk()
work_space = tkinter.Canvas(root, width = 500, height = 425)
all_boxes = []


def init_screen():
    """Creates the general screen of app"""

    root.title("Chem Structure Drawer")
    #Making Main Screen

    root.geometry("500x500+650+250")
    root.minsize(width = 500, height = 500)
    root.maxsize(width = 500, height = 500)
    #Setting main screen size

def init_canvas():
    """Creates the maleable part of app, to draw on"""

    work_space["background"] = "#A9EDFF"
    work_space.pack()
    #Add a canvas to main screen, to be able to do stuff


def add_buttons():
    """Adds the buttons at the bottom of the screen (Add box, Save, Erase)"""
    
    add_box_button = tkinter.Button(root, text = "Add Box", width = 25, height = 2, command = make_box)
    add_box_button.place( x = 140, y = 448)
    #Add a box button, y = 465 makes direct contact the best

    save_button = tkinter.Button(root, text = "SAVE" , width = 10, height = 2, image = None)
    save_button.place(x = 390, y = 448)
    #Make Save button, later make the save button look like a floppy disk save :D

    erase_button = tkinter.Button(root, text = "Clear All" , width = 10, height = 2, command = clear_all)
    erase_button.place(x = 25, y = 448)


class box():
    def __init__(self, master = None, x = 0 , y= 0):
        self.master = master
        self.x = x
        self.y = y


        thing = tkinter.Entry(root, width = 2)
        self.box = work_space.create_window(x, y, window = thing) 
        work_space.pack() 
  


def make_box():
    """Randomly makes a box"""

    x_pos = random.randint(50 , 450)
    y_pos = random.randint(50 , 400)
    new_box = box(root, x_pos, y_pos)

    all_boxes.append(box)

def clear_all():
    """Clears canvas completely"""

    work_space.delete("all")


def callback(event):
    """Gets a (left button) mouse-click event"""

    x_pos = event.x
    y_pos = event.y

    new_box = box(root, x_pos, y_pos)

def key_pressed(event):
    """Gets a keyboard button event"""

    pressed = repr(event.char)
    print(pressed) 

    if pressed == "' '":
        move_boxes()


def bindings():
    """Binds events to canvas and app in general"""

    work_space.bind("<Button-1>", callback)
    root.bind("<Key>", key_pressed)
    work_space.pack()
    print("packed")


def move_boxes():
    """Nothing for now"""

    print("working")
    pass



if __name__ == "__main__":
    init_screen()
    init_canvas()
    add_buttons()

    bindings()


    root.mainloop()
