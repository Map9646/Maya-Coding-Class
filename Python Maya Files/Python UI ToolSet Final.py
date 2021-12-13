#Tomorrow - Parent all color buttons to grid, then test window again, add scripts to buttons and check functionality of UI. 
import maya.cmds as cmds


class UITools():

    def __init__(self):
        self.main_window = 'UITools'

    def create(self):
        self.delete()

        self.main_window = cmds.window(self.main_window, title="Rename Tool, Create Ctrl, Change Color",
                                       widthHeight=(200, 55))

        column = cmds.columnLayout(columnAttach=('both', 5), rowSpacing=10, columnWidth=250)
        cmds.button(parent=column, label="Rename")
        cmds.button(parent=column, label="Create Control")

        grid = cmds.gridLayout(numberOfColumns=4, cellWidthHeight=(7, 4)) 
        cmds.button(parent=self.main_window, label="Light Grey")
        cmds.button(parent=self.main_window, label="Black")
        cmds.button(parent=self.main_window, label="Dark Grey")
        cmds.button(parent=self.main_window, label="Grey")
        cmds.button(parent=self.main_window, label="Red")
        cmds.button(parent=self.main_window, label="Dark Blue")
        cmds.button(parent=self.main_window, label="Indigo")
        cmds.button(parent=self.main_window, label="Forest Green")
        cmds.button(parent=self.main_window, label="Darker Blue")
        cmds.button(parent=self.main_window, label="Pink-Purple")
        cmds.button(parent=self.main_window, label="Light Brown")
        cmds.button(parent=self.main_window, label="Dark Brown")
        cmds.button(parent=self.main_window, label="Brown")
        cmds.button(parent=self.main_window, label="Prange")
        cmds.button(parent=self.main_window, label="Light Green")
        cmds.button(parent=self.main_window, label="Blue")
        cmds.button(parent=self.main_window, label="White")
        cmds.button(parent=self.main_window, label="Yellow")
        cmds.button(parent=self.main_window, label="Light Blue")
        cmds.button(parent=self.main_window, label="Light Green")
        cmds.button(parent=self.main_window, label="Light Pink")
        cmds.button(parent=self.main_window, label="Tan")
        cmds.button(parent=self.main_window, label="Pastel Yellow")
        cmds.button(parent=self.main_window, label="Pale Green")
        cmds.button(parent=self.main_window, label="Tan-Brown")
        cmds.button(parent=self.main_window, label="Puke Green")
        cmds.button(parent=self.main_window, label="Yellow-Green")
        cmds.button(parent=self.main_window, label="Green")
        cmds.button(parent=self.main_window, label="Baby Blue")
        cmds.button(parent=self.main_window, label="Light Indigo")
        cmds.button(parent=self.main_window, label="Purple")
        cmds.button(parent=self.main_window, label="Red-Purple")

        cmds.showWindow(self.main_window)

    def delete(self):
        if cmds.window(self.main_window, exists=True):
            cmds.delete(self.main_window)
