import maya.cmds as cmds



def Control():
    
    sels = cmds.ls(sl = True)
    print(sels)
    if sels:
        for sel in sels: 
        
            ctrl=cmds.circle (name = 'ctrl')
        
            grp=cmds.group  (ctrl,name = 'ctrlGroup')
            
            print(sel)
            
            cmds.matchTransform (grp, sel)
            

            

            
        
        
       
       


   
    
    
