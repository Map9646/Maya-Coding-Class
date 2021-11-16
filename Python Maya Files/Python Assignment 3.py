import Maya.cmds as cmds

sels = cmds.ls(sl = True)

    for sel in sels:
        shapes = cmds.ListRelatives(sel, children = True, shapes = True)
        

       
       
def ControlColor(newColor):

   cmds.color("nurbsCircle1", rgb = (1, 0, 0))
    
    
ControlColor(2)       