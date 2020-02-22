import tkinter as tkinter
import random
from typing import List

global root
global work_space
global all_boxes
global all_lines
global double_clicks

root = tkinter.Tk()
work_space = tkinter.Canvas(root, width = 500, height = 425)

all_boxes: List["Box"] = []
all_lines: List["Line"] = []
double_clicks: List[int] = []
 


#Tkinter canvas doesn't work well with save. Hecking extra work to do. 

#Options are: generate a postscript document (to feed into some other tool: ImageMagick, Ghostscript, etc):
#draw the same image in parallel on PIL (Doesn't work because I need entries from user.)



"""
Future Objectives

How to Leave text field

Save to JPG

Drag Selection --> Save

Maybe make a kill individual entry function? Click escape in the entry to delete it? 

Btw, Entry widget seems to make a whole new window, so it might wonk around w/ save functionalities and is wierd in general.
"""

class Box():
    def __init__(self, master = None, x = 0 , y= 0, list_position = None):
        self.master = master
        self.x = x
        self.y = y
        self.list_position = list_position


        thing = tkinter.Entry(root, width = 2)
        self.box = work_space.create_window(x, y, window = thing) 
        work_space.pack()

    def movement(self, new_x, new_y):
        work_space.move(self.box, new_x, new_y) 

class Line():
    def __init__(self, master = None, 
                x1 = None, y1 = None, 
                x2 = None, y2 = None,
                list_position = None):
        
        self.master = master
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.list_position = list_position

        self.this_line = work_space.create_line(x1, y1, x2, y2)
        work_space.pack()

  

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

    add_box_button = tkinter.Button(root, text = "Does Nothing rn", width = 25, height = 2)
    add_box_button.place( x = 140, y = 448)
    #Add a box button, y = 465 makes direct contact the best

    save_button = tkinter.Button(root, text = "SAVE" , width = 10, height = 2, image = None, command = save_work_space)
    save_button.place(x = 390, y = 448)
    #Make Save button, later make the save button look like a floppy disk save :D

    erase_button = tkinter.Button(root, text = "Clear All" , width = 10, height = 2, command = clear_all)
    erase_button.place(x = 25, y = 448)


def make_box(x: int, y: int):
    """Creates a box, then adds to list of boxes."""

    new_box = Box(root, x, y, len(all_boxes))
    all_boxes.append(new_box)


def clear_all():
    """Clears canvas completely"""

    work_space.delete("all")
    all_boxes = []


def click_callback(event):
    """Gets a (left button) mouse-click event"""

    x_pos = event.x
    y_pos = event.y

    make_box(x_pos, y_pos)


def two_finger_click_callback(event):
    """
    Gets a right click (two finger) mouse click event.
    Store the position of this double click to a list, in form x, y.
    Clears the list when it holds 4 values (two clicks).
    Also currently prints the contents of the list. 
    """

    global double_clicks

    x = event.x
    y = event.y

    if len(double_clicks) == 0:
        #First double click

        double_clicks.append(x)
        double_clicks.append(y)

    elif len(double_clicks) == 2:
        #Second double click
        double_clicks.append(x)
        double_clicks.append(y)

        line_straightener()

        make_line(double_clicks[0], double_clicks[1], double_clicks[2], double_clicks[3])

        double_clicks = []


def key_pressed(event):
    """Gets a keyboard button event"""

    pressed = repr(event.char)

    if pressed == "' '":
        move_all_boxes()


def bindings():
    """Binds events to canvas and app in general"""

    work_space.bind("<Button-1>", click_callback)
    work_space.bind("<Button-2>", two_finger_click_callback)
    root.bind("<Key>", key_pressed)
    work_space.pack()


def move_all_boxes():
    """Moves all boxes down 1 and right 1. Also printed the item."""

    
    for z in all_boxes:
        new_x = int(z.x) + 1 
        new_y = int(z.y) + 1
        z.movement(new_x, new_y)
        
        print("This is item: " , z)


def make_line(x1,y1,x2,y2):
    new_line = Line(root, x1, y1, x2, y2)
    all_lines.append(new_line)
 

def line_straightener():
    """
    Looks at the x and y values of a potential line.
    If they are close enough that it seems meant to be a straight line, straighten it. 
    """

    delta_x = double_clicks[0] - double_clicks[2]
    delta_y = double_clicks[1] - double_clicks[3]

    if abs(delta_x) < 15:
        double_clicks[2] = double_clicks[0]
    
    elif abs(delta_y) < 15:
        double_clicks[3] = double_clicks[1] 


def save_work_space():
    pass



if __name__ == "__main__":
    init_screen()
    init_canvas()
    add_buttons()

    bindings()


    root.mainloop()
