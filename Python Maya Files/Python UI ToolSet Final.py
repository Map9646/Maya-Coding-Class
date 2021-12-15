import maya.cmds as cmds
import Python_Renamer_Tool_Assignment as renamer
import Color_Script as Color
import Python_Assignment_3 as ctrl




class UITools():

    def __init__(self):
        self.main_window = 'UITools'
        self.obj_n=""
        self.num=""
        self.geo=""

    def create(self):
        self.delete()

        self.main_window = cmds.window(self.main_window, title="Rename Tool, Create Ctrl, Change Color",
                                       widthHeight=(200, 55))

        column=cmds.columnLayout(columnAttach=('both', 5), rowSpacing=10, columnWidth=250)
        self.obj_n=cmds.textFieldGrp(parent=column,label='Rename', placeholderText='arm_')
        self.num=cmds.textFieldGrp(parent=column,label='Rename', placeholderText='3')
        self.geo=cmds.textFieldGrp(parent=column,label='Rename', placeholderText='_geo')
        cmds.button(parent=column, label="Rename", command=lambda *x: self.rename_button())
        cmds.button(parent=column, label="Create Control",command=lambda *x: self.ctrl_button())

        grid=cmds.gridLayout(numberOfColumns=4, cellWidthHeight=(50, 50))
        cmds.button(parent=grid, label="Light Grey", command=lambda *x: self.color_button(col=0))
        cmds.button(parent=grid, label="Black", command=lambda *x: self.color_button(col=1))
        cmds.button(parent=grid, label="Dark Grey", command=lambda *x: self.color_button(col=2))
        cmds.button(parent=grid, label="Grey", command=lambda *x: self.color_button(col=3))
        cmds.button(parent=grid, label="Red", command=lambda *x: self.color_button(col=4))
        cmds.button(parent=grid, label="Dark Blue", command=lambda *x: self.color_button(col=5))
        cmds.button(parent=grid, label="Indigo", command=lambda *x: self.color_button(col=6))
        cmds.button(parent=grid, label="Forest Green", command=lambda *x: self.color_button(col=7))
        cmds.button(parent=grid, label="Darker Blue", command=lambda *x: self.color_button(col=8))
        cmds.button(parent=grid, label="Pink-Purple", command=lambda *x: self.color_button(col=9))
        cmds.button(parent=grid, label="Light Brown", command=lambda *x: self.color_button(col=10))
        cmds.button(parent=grid, label="Dark Brown", command=lambda *x: self.color_button(col=11))
        cmds.button(parent=grid, label="Brown", command=lambda *x: self.color_button(col=12))
        cmds.button(parent=grid, label="Orange", command=lambda *x: self.color_button(col=13))
        cmds.button(parent=grid, label="Light Green", command=lambda *x: self.color_button(col=14))
        cmds.button(parent=grid, label="Blue", command=lambda *x: self.color_button(col=15))
        cmds.button(parent=grid, label="White", command=lambda *x: self.color_button(col=16))
        cmds.button(parent=grid, label="Yellow", command=lambda *x: self.color_button(col=17))
        cmds.button(parent=grid, label="Light Blue", command=lambda *x: self.color_button(col=18))
        cmds.button(parent=grid, label="Light Green", command=lambda *x: self.color_button(col=19))
        cmds.button(parent=grid, label="Light Pink", command=lambda *x: self.color_button(col=20))
        cmds.button(parent=grid, label="Tan", command=lambda *x: self.color_button(col=21))
        cmds.button(parent=grid, label="Pastel Yellow", command=lambda *x: self.color_button(col=22))
        cmds.button(parent=grid, label="Pale Green", command=lambda *x: self.color_button(col=23))
        cmds.button(parent=grid, label="Tan-Brown", command=lambda *x: self.color_button(col=24))
        cmds.button(parent=grid, label="Puke Green", command=lambda *x: self.color_button(col=25))
        cmds.button(parent=grid, label="Yellow-Green", command=lambda *x: self.color_button(col=26))
        cmds.button(parent=grid, label="Green", command=lambda *x: self.color_button(col=27))
        cmds.button(parent=grid, label="Baby Blue", command=lambda *x: self.color_button(col=28))
        cmds.button(parent=grid, label="Light Indigo", command=lambda *x: self.color_button(col=29))
        cmds.button(parent=grid, label="Purple", command=lambda *x: self.color_button(col=30))
        cmds.button(parent=grid, label="Red-Purple", command=lambda *x: self.color_button(col=31))

        cmds.showWindow(self.main_window)

    def delete(self):
        if cmds.window(self.main_window, exists=True):
           cmds.delete(self.main_window)

    def rename_button(self):
        import importlib
        importlib.reload(renamer)
      
        objName=cmds.textFieldGrp(self.obj_n,q=True,text=True)
        number=cmds.textFieldGrp(self.num,q=True,text=True)
        objNode=cmds.textFieldGrp(self.geo,q=True,text=True)
        renamer.renaming(objName, number, objNode)
        
        
    def color_button(self,col):
        import importlib
        importlib.reload(Color)
        Color.Color(col)
        
    def ctrl_button(self):
        import importlib
        importlib.reload(ctrl)
        ctrl.Control()
        
        
myUI = UITools()
myUI.create()
        
        
        
