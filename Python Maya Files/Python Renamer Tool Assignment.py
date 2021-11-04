import maya.cmds as cmds

def renaming (objName, number, objNode):

   objS = cmds.ls(sl=True)
   
   numbers = i
   
   for i, sel in enumerate(objS):
    "arm" , "geo".partition(objName)
    
    cmds.rename(objName + str(i).zfill + objNode)


renaming("arm", 2, "geo")

#not sure why it won't let me call my function. Something with my string. It could be my partition. It's just not running


#Moving it into the for loop seemed to resolve issues, but I'm not sure if that means it's working properly yet. 


#for i, sel in enumerate()


#I'll ask for help tonight. It's probs just a simple fix. 

#Would I put numbers in place of i? Not sure, but possibly. I'll test it. 
      

















