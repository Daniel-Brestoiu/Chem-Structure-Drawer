import pyautogui

"""
General Process:

Method A: To Screenshot

    Simultaneous click Command-Control-Shift-4 to open general screen shot
        - This causes mouse to become a top-left coordinate thing

    Click Left
    Move Mouse to bottom right corner of where I want (Still holding down left mouse)
    Release left mouse click
        - This takes the screenshot of the selected area.

"""

def test():
    """Simple test function of the functionalities of Take_Screenshot.py"""
    x1 = 100
    y1 = 300
    x2 = 300
    y2 = 400
    x_adjustment = 50 + 2
    y_adjustment = 50 + 244


    pyautogui.keyDown("command")
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("shift")
    pyautogui.keyDown("4")

    pyautogui.keyUp("command")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("shift")
    pyautogui.keyUp("4")

    pyautogui.mouseDown(button = 'left', x= (x1+x_adjustment), y= (y1+y_adjustment))
    pyautogui.dragTo(x= (x2+x_adjustment), y= (y2+y_adjustment), duration = 0.15, button = 'left')
    pyautogui.mouseUp(button='left')


def take_screenshot(Selection_Box):
    """
    Given a Selection_Box object, with x1,y1, and x2,y2 parameters
    takes a screenshot of the area between x1,y1, and x2,y2 as modified
    by the geometry of the initial frame. Currently 250 pixels down and 650 pixels right
    of the top left corner of the screen. 
 
    """
    x1 = Selection_Box.x1
    y1 = Selection_Box.y1
    
    x2 = Selection_Box.x2
    y2 = Selection_Box.y2

    x_adjustment = 650 
    y_adjustment = 250 + 22
    #Kludge fix to adjustment, see if there is any better long term solution to adjustments
    #Current idea is to store the adjustments in a list or smth and import that to take_screenshot? 
    #Idk how tracking movement would work. Look into it later

    
    pyautogui.keyDown("command")
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("shift")
    pyautogui.keyDown("4")

    pyautogui.keyUp("command")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("shift")
    pyautogui.keyUp("4")


    pyautogui.mouseDown(x= (x1+x_adjustment), y= (y1+y_adjustment), button = 'left')
    pyautogui.dragTo(x= (x2+x_adjustment), y= (y2+y_adjustment), duration = 0.2, button ='left')
    pyautogui.mouseUp(button='left')
    #Might want to use pyautogui.moveRel in order to move relative to a position and not have to deal with adjustment factors?


if __name__ == "__main__":
    test()
