import maya.cmds as cmds

cmds.select (all = True)

def Control(sels, sels2, sels3):
    
    sels = cmds.ls(sl = True)

    if sels:
        for sel in sels: 
        
            cmds.circle (name = 'ctrl')
        
            cmds.group  (name = 'ctrlGroup')
        
            
            cmds.matchTransform ('ctrlGroup', sels)
            cmds.matchTransform ('ctrlGroup', sels2)
            cmds.matchTransform ('ctrlGroup', sels3)
        
        
        
Control('pSphere1', 'pSphere2', 'pSphere3')         
            
        
        
       
       
def ControlColor(newColor):
    
  cmds.setAttr('ctrlShape' + '.overrideEnabled', 1)
  cmds.setAttr('ctrlShape' + '.overrideColor', newColor)

   
    
    
ControlColor(10)       