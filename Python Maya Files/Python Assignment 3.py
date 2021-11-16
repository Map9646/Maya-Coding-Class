import Maya.cmds as cmds

sels = cmds.ls(sl = True)

def Control()

    for sel in sels:
        shapes = cmds.ListRelatives(sel, children = True, shapes = True)
        

       