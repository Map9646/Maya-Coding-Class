import maya.cmds as cmds

m_window = 'changeColorUI'

if cmds.window(m_window, exists = True):
    cmds.deleteUI(m_window)

#puts window in a variable, so nothing gets lost in code

m_window = cmds.window(m_window, title="Change Color", widthHeight=(200, 55) )
cmds.showWindow( m_window )
#Watch videos for last class and this class, so I can make my window 
#fix color script so it changes the color for more than one object. 

#class examples and how to make them

class ToolUI():
    def __init__(self):
        pass
        
        


def create(self):
    #insert windows code here for creating my window. 