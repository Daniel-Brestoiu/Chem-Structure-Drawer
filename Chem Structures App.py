import tkinter as tkinter
import random
from typing import List
import time
from Take_Screenshot import take_screenshot


global root
global work_space
global all_boxes
global all_lines
global clicks_list
global double_clicks
global selection_mode
global selection_boxes_list

all_boxes: List["Box"] = []
all_lines: List["Line"] = []
clicks_list: List[int] =[]
double_clicks: List[int] = []
selection_boxes_list: List["Selection_Box"] = []
selection_mode = False

root = tkinter.Tk()
work_space = tkinter.Canvas(root, width = 500, height = 425)


"""
FUTURE OBJECTIVES


Relocate squares to better fit on lines :)
    - Meet at endpoints             (done)
    - Fit well on line
    - Intersections of lines
    Might use Bresenham's Line Algorithm?

Make lines with close endpoints connect at their end points

Box is auto-selected for text entry upon creation

Change screenshot function to be relative to position.

Delete an entry or additional line functionality.

Leave Text-Field, after typing.

Help/Instructions box.

Fullscreen mode, with same functionalities. 

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
                list_position = None,
                points = None):
        
        self.master = master
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.list_position = list_position
        self.points = points_of_interest(self)

        self.this_line = work_space.create_line(x1, y1, x2, y2)
        work_space.pack()

class Selection_Box():
    def __init__(self, master = None,
                x1 = None, y1 = None,
                x2= None, y2 = None,
                ID = None):
        
        self.master = master
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.ID = ID


        this_selection = work_space.create_rectangle(x1,y1, x2,y2, dash = (3,3))
        self.ID = this_selection

        work_space.pack()
        clear_selections()
        selection_boxes_list.append(self)

    def self_destruct(self, ID):
        work_space.delete(ID)


def points_of_interest(Line):
    points_list = []

    dx = abs(Line.x2 - Line.x1)
    dy = abs(Line.y2 - Line.y1)

    x, y = Line.x1, Line.y1
    sx = -1 if Line.x1 > Line.x2 else 1
    sy = -1 if Line.y1 > Line.y2 else 1 

    if dx > dy:
        err = dx / 2.0
        while x != Line.x2:

            points_list.append((x,y))
            err -= dy

            if err < 0:
                y += sy
                err += dx
            x += sx 

    else:
        err = dy/ 2.0
        
        while y != Line.y2:
            points_list.append((x,y))
            err -= dx

            if err < 0:
                x += sx
                err += dy
            y += sy
        
    points_list.append((x,y))
    return (points_list)

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
    """Adds the buttons at the bottom of the screen (Selection box, Save, clear)"""

    selection_box_button = tkinter.Button(root, text = "Selection Mode", width = 25, height = 2, command = clicked_selection_box)
    selection_box_button.place(x = 140, y = 448)
    #Add a box button, y = 465 makes direct contact the best

    save_button = tkinter.Button(root, text = "SAVE" , width = 10, height = 2, image = None, command = save_work_space)
    save_button.place(x = 390, y = 448)
    #Make Save button, later make the save button look like a floppy disk save :D

    clear_button = tkinter.Button(root, text = "Clear All" , width = 10, height = 2, command = clear_all)
    clear_button.place(x = 25, y = 448)


def make_box(x: int, y: int):
    """Creates a box, then adds to list of boxes."""
    new_x, new_y = skewer_box(x,y)

    new_box = Box(root, new_x, new_y, len(all_boxes))
    all_boxes.append(new_box)


def clear_all():
    """Clears canvas completely"""
    global all_boxes
    global all_lines
    global selection_boxes_list

    work_space.delete("all")

    selection_boxes_list = []
    all_lines = []
    all_boxes = []


def make_box_click_callback(event):
    """Gets a mouse-click event, uses it to make a box, or selection rectangle."""
    global clicks_list

    if not selection_mode:
        #Not selection mode, place a box.
        x_pos = event.x
        y_pos = event.y

        make_box(x_pos, y_pos)



def release_left(event):
    """
    If in selection mode, obtains position of release and compiles click 
    list for co-ordinates to draw a rectangle 'selection box'.
    """
    global clicks_list
    global selection_mode

    if selection_mode:
        x = event.x
        y = event.y

        clicks_list.append(x)
        clicks_list.append(y)


        if len(clicks_list) == 4:

            x1 = clicks_list[0]
            y1 = clicks_list[1]
            x2 = clicks_list[2]
            y2 = clicks_list[3]

            selection = Selection_Box(root,x1,y1,x2,y2)


            clicks_list = []

def make_line_click_callback(event):
    """
    Gets a mouse click event.
    Store the position of this double click to a list, in form x, y.
    """

    global double_clicks
    global selection_mode

    x = event.x
    y = event.y

    if not selection_mode:
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

    elif selection_mode:
        #Make a selection square functionality

        x_pos = event.x
        y_pos = event.y

        clicks_list.append(x_pos)
        clicks_list.append(y_pos)

def key_pressed(event):
    """Gets a keyboard button event"""
    pressed = repr(event.char)



def bindings():
    """Binds events to canvas and app in general"""

    work_space.bind("<Button-1>", make_line_click_callback)
    work_space.bind("<Button-2>", make_box_click_callback)
    work_space.bind("<ButtonRelease-1>", release_left)
    root.bind("<Key>", key_pressed)
    work_space.pack()

    #Historic
    #work_space.bind("<Button-1>", click_callback)
    #work_space.bind("<Button-2>", two_finger_click_callback)
    #work_space.bind("<ButtonRelease-1>", release_left)


def move_all_boxes():
    """Moves all boxes down 1 and right 1. Also printed the item."""
    
    for z in all_boxes:
        new_x = int(z.x) + 1 
        new_y = int(z.y) + 1
        z.movement(new_x, new_y)


def make_line(x1,y1,x2,y2):
    """Draws a straight line given four co-ordinates"""
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
    
def skewer_box(x,y):
    """
    Takes in intergers x,y and compares to the endpoints of currently existing lines.
    If the difference between the given x,y and an endpoint is less than 15 pixels for both x and y, then
    returns the position of the endpoint. Otherwise returns initial input. 
    """
    global all_lines

    for z in all_lines:
        position1 = (z.x1, z.y1)
        position2 = (z.x2, z.y2)

        delta_x1 = abs(position1[0] - x)
        delta_y1 = abs(position1[1] - y)

        delta_x2 = abs(position2[0] - x)
        delta_y2 = abs(position2[1] - y)

        if delta_x1 < 15 and delta_y1 < 15:
            return(position1)
        
        elif delta_x2 < 15 and delta_y2 < 15:
            return(position2)

        for a in z.points:
            print(a)

            delta_x = abs(a[0] - x)
            delta_y = abs(a[1] - y)

            if delta_x < 5 and delta_y < 5:
                print("found valid place")
                return(a)
    return(x,y)
        


def clicked_selection_box():
    """Functionality for drag selection, and change button colours."""
    global selection_mode
    global clicks_list

    if not selection_mode:
        #Select mode is not currently on, therefore turn it on and allow selection.

        work_space["background"] = "#90EE90"
        selection_mode = True
        
 
    elif selection_mode:
        #Select mode is on, and user wants to turn it off. Therefore, turn it off. 

        work_space["background"] = "#A9EDFF"
        selection_mode = False

        clear_selections()
        clicks_list = []


def clear_selections():
    """Deletes all currently existing selection boxes, as listed in selection_boxes_list"""
    global selection_boxes_list

    for z in selection_boxes_list:
        z.self_destruct(z.ID)
        selection_boxes_list.remove(z)


def save_work_space():
    """
    Calls another file I have.
    Uses Mac commands to take a screenshot
    and save to clipboard.
    Additionally changes background to red to indicate completion
    before changing back to blue.
    """

    try:
        take_screenshot(selection_boxes_list[0])
        #selection_boxes_list[0] should now be an object located in memory

        work_space["background"] = "#DDA0DD"
        work_space.update()

    except:
        work_space["background"] = "#FF4D4D"
        work_space.update()

    time.sleep(1)

    if selection_mode:
        work_space["background"] = "#90EE90"

    else:
        work_space["background"] = "#A9EDFF"



if __name__ == "__main__":
    init_screen()
    init_canvas()
    add_buttons()

    bindings()

    root.mainloop()
