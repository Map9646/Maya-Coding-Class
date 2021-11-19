import maya.cmds as cmds

cmds.select (all = True)

def Control(objName)
    
    sels = cmds.ls(sl = True)

    if sels:
        for sel in sels: #Take this into PyCharmm on my Desktop and see what isn't working and why. 
        
       
        
            cmds.circle (n = 'ctrl')
        
            cmds.group ('ctrl', n = 'ctrlGroup')
        
            cmds.parent ('ctrl', 'ctrlGroup')
        
            cmds.matchTransform ('ctrlGroup', sels)
        
        
        
        
            if objName:
                
                cmds.rename(objName + 'Ctrl')
            
            
        
        
       
       
def ControlColor(newColor):
    
  cmds.setAttr('ctrl' + 'overrideEnabled', newColor)
  cmds.setAttr('ctrl' + 'overrideColor', newColor)

   
    
    
ControlColor(5)       