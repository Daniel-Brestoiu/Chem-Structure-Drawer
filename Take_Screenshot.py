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

    #master = Selection_Box.master       Oof, doesn't actually have position of root.

    x_adjustment = 650 + 2
    y_adjustment = 250 + 24

    

    #Mouse functions
    pyautogui.moveTo((x1+x_adjustment),(y1+y_adjustment))
    pyautogui.PAUSE = 2
    pyautogui.moveTo((x2+x_adjustment),(y2+y_adjustment))
    pyautogui.PAUSE = 2
    print('functional')
