import maya.cmds as cmds

cmds.select (all = True)

def Control(objName)
    
    sels = cmds.ls(sl = True)

    if sels:
        for sel in sels: 
        
       
        
            cmds.circle (n = 'ctrl')
        
            cmds.group ('ctrl', n = 'ctrlGroup')
        
            cmds.parent ('ctrl', 'ctrlGroup')
        
            cmds.matchTransform ('ctrlGroup', sels)
        
        
        
        
            #if objName:
                
                #cmds.rename(objName + 'ctrl')
            
            
        
        
       
       
def ControlColor(newColor):
    
  cmds.setAttr('ctrlShape' + '.overrideEnabled', 1)
  cmds.setAttr('ctrlShape' + '.overrideColor', newColor)

   
    
    
ControlColor(10)       