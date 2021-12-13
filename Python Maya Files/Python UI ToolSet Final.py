#Today -  add scripts to buttons, make sure to put all scripts into Maya scripts folder, start testing out UI
import maya.cmds as cmds


class UITools():

    def __init__(self):
        self.main_window = 'UITools'

    def create(self):
        self.delete()

        self.main_window = cmds.window(self.main_window, title="Rename Tool, Create Ctrl, Change Color",
                                       widthHeight=(200, 55))

        column = cmds.columnLayout(columnAttach=('both', 5), rowSpacing=10, columnWidth=250, command=lambda x: Python Renamer Tool Assignment)
        cmds.button(parent=column, label="Rename")
        cmds.button(parent=column, label="Create Control")

        grid = cmds.gridLayout(numberOfColumns=4, cellWidthHeight=(50, 50), command=lambda x: )
        cmds.button(parent=grid, label="Light Grey")
        cmds.button(parent=grid, label="Black")
        cmds.button(parent=grid, label="Dark Grey")
        cmds.button(parent=grid, label="Grey")
        cmds.button(parent=grid, label="Red")
        cmds.button(parent=grid, label="Dark Blue")
        cmds.button(parent=grid, label="Indigo")
        cmds.button(parent=grid, label="Forest Green")
        cmds.button(parent=grid, label="Darker Blue")
        cmds.button(parent=grid, label="Pink-Purple")
        cmds.button(parent=grid, label="Light Brown")
        cmds.button(parent=grid, label="Dark Brown")
        cmds.button(parent=grid, label="Brown")
        cmds.button(parent=grid, label="Prange")
        cmds.button(parent=grid, label="Light Green")
        cmds.button(parent=grid, label="Blue")
        cmds.button(parent=grid, label="White")
        cmds.button(parent=grid, label="Yellow")
        cmds.button(parent=grid, label="Light Blue")
        cmds.button(parent=grid, label="Light Green")
        cmds.button(parent=grid, label="Light Pink")
        cmds.button(parent=grid, label="Tan")
        cmds.button(parent=grid, label="Pastel Yellow")
        cmds.button(parent=grid, label="Pale Green")
        cmds.button(parent=grid, label="Tan-Brown")
        cmds.button(parent=grid, label="Puke Green")
        cmds.button(parent=grid, label="Yellow-Green")
        cmds.button(parent=grid, label="Green")
        cmds.button(parent=grid, label="Baby Blue")
        cmds.button(parent=grid, label="Light Indigo")
        cmds.button(parent=grid, label="Purple")
        cmds.button(parent=grid, label="Red-Purple")

        cmds.showWindow(self.main_window)

    def delete(self):
        if cmds.window(self.main_window, exists=True):
            cmds.delete(self.main_window)
