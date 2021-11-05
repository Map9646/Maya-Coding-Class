import maya.cmds as cmds

def renaming (objName, number, objNode):

   objS = cmds.ls(sl=True)
   
   for i, sel in enumerate(objS):
    
       cmds.rename(objName + str(i).zfill(2) + objNode)


renaming("arm", 3 , "geo")










