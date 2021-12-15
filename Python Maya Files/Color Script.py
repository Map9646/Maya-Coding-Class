import maya.cmds as cmds

def Color(newColor):

  sels = cmds.ls(sl=True)
  for sel in sels:
    shapes = cmds.listRelatives(sel, children=True, shapes=True)
    for shape in shapes:
      cmds.setAttr('.overrideEnabled', 1)
      cmds.setAttr('.overrideColor', newColor)

  return