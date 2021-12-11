import maya.cmds as cmds


class UITools()

    def__init__(self):
        
        main_window = 'UIToolSet'
        
        
        self.main_window = cmds.window( title="Rename Tool, Create Ctrl, Change Color", widthHeight=(200, 55) )
        
        cmds.columnLayout( columnAttach=('both', 5), rowSpacing=10, columnWidth=250 )
        cmds.button()
        
        cmds.showWindow(self.main_window)
        
        
        
        
     def delete(self):
         
         if cmds.window(self.main_window, exists=True):
             cmds.delete(self.main_window)