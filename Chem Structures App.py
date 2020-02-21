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
    root.title("Chem Structure Drawer")
    #Making Main Screen

    root.geometry("500x500+650+250")
    root.minsize(width = 500, height = 500)
    root.maxsize(width = 500, height = 500)
    #Setting main screen size

def init_canvas():
    work_space["background"] = "#A9EDFF"
    work_space.pack()
    #Add a canvas to main screen, to be able to do stuff


def add_buttons():
    add_box_button = tkinter.Button(root, text = "Add Box", width = 25, height = 2, command = make_box)
    add_box_button.place( x = 140, y = 448)
    #Add a box button, y = 465 makes direct contact the best

    save_button = tkinter.Button(root, text = "SAVE" , width = 10, height = 2, image = None)
    save_button.place(x = 390, y = 448)
    #Make Save button, later make the save button look like a floppy disk save :D

    erase_button = tkinter.Button(root, text = "Clear All" , width = 10, height = 2, command = clear_all)
    erase_button.place(x = 25, y = 448)


"""
class box:
    def __init__(self, master = None):
        self.master = master

        self.x = 1
        self.y = 1
"""


def make_box():
    x_pos = random.randint(50 , 450)
    y_pos = random.randint(50 , 400)
    box = tkinter.Entry(root, width = 2)
    work_space.create_window(x_pos, y_pos, window = box)


    all_boxes.append(box)

def clear_all():
    work_space.delete("all")


def callback(event):

    x_pos = event.x
    y_pos = event.y

    print("Clicked at: " , x_pos, y_pos)

    place_box(x_pos, y_pos)

def key_pressed(event):
    pressed = repr(event.char)
    print(pressed) 

    if pressed == "' '":
        move_boxes()


def bindings():
    work_space.bind("<Button-1>", callback)
    root.bind("<Key>", key_pressed)
    work_space.pack()
    print("packed")

def place_box(x,y):
    box = tkinter.Entry(root, width = 2)
    work_space.create_window(x,y, window = box)

def move_boxes():
    print("working")
    pass



if __name__ == "__main__":
    init_screen()
    init_canvas()
    add_buttons()

    bindings()

    root.mainloop()
