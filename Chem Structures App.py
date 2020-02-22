import tkinter as tkinter
import random
import time
from typing import List

global root
global work_space
global all_boxes
root = tkinter.Tk()
work_space = tkinter.Canvas(root, width = 500, height = 425)

all_boxes: List["Box"] = []

#List full of objects of class type box


"""
Future Objectives

Add Lines 
Manipulate/Move Lines
Manipulate/Move Boxes

How to Leave text field

Save to JPG

Drag Selection --> Save

"""

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

    add_box_button = tkinter.Button(root, text = "Add Line", width = 25, height = 2, command = draw_line)
    add_box_button.place( x = 140, y = 448)
    #Add a box button, y = 465 makes direct contact the best

    save_button = tkinter.Button(root, text = "SAVE" , width = 10, height = 2, image = None)
    save_button.place(x = 390, y = 448)
    #Make Save button, later make the save button look like a floppy disk save :D

    erase_button = tkinter.Button(root, text = "Clear All" , width = 10, height = 2, command = clear_all)
    erase_button.place(x = 25, y = 448)


class Box():
    def __init__(self, master = None, x = 0 , y= 0, position = None):
        self.master = master
        self.x = x
        self.y = y
        self.position = position


        thing = tkinter.Entry(root, width = 2)
        self.box = work_space.create_window(x, y, window = thing) 
        work_space.pack()

    def movement(self, new_x, new_y):
        work_space.move(self.box, new_x, new_y) 
  

def make_box(x: int, y: int):
    """Creates a box, then adds to list of boxes."""

    new_box = Box(root, x, y, len(all_boxes))
    all_boxes.append(new_box)

def clear_all():
    """Clears canvas completely"""

    work_space.delete("all")
    all_boxes = []


def callback(event):
    """Gets a (left button) mouse-click event"""

    x_pos = event.x
    y_pos = event.y

    make_box(x_pos, y_pos)

def key_pressed(event):
    """Gets a keyboard button event"""

    pressed = repr(event.char)

    if pressed == "' '":
        move_all_boxes()


def bindings():
    """Binds events to canvas and app in general"""

    work_space.bind("<Button-1>", callback)
    root.bind("<Key>", key_pressed)
    work_space.pack()


def move_all_boxes():
    """Moves all boxes down 1 and right 1. Also printed the item."""

    
    for z in all_boxes:
        new_x = int(z.x) + 1 
        new_y = int(z.y) + 1
        z.movement(new_x, new_y)
        
        print("This is item: " , z)


def draw_line():
    x1 = random.randint(50, 450)
    x2 = random.randint(50, 450)
    y1= random.randint(50, 450)
    y2 = random.randint(50, 450)
    
    work_space.create_line(x1,y1, x2,y2)
    work_space.place()



if __name__ == "__main__":
    init_screen()
    init_canvas()
    add_buttons()

    bindings()


    root.mainloop()
