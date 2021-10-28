import random
def Randomizer(num, xmin, ymin, zmin, xmax, ymax, zmax):
    sels = cmds.ls(sl=True)
    
    for sel in sels:
       for i in range(num):
           dup = cmds.duplicate(sel, rr=True)
           dup[0]
           x = random.uniform(xmin, xmax) 
           y = random.uniform(ymin, ymax)
           z = random.uniform(zmin, zmax)
           
           cmds.xform(dup, worldSpace = True, translation = [x, y, z])#moves to a ramdom location. Simliar to move, but a bit different in how it's executed
           
           
           
           
    
    
    
Randomizer(num=5,xmin=-20, xmax=10, ymin=-5, ymax= 6, zmin=-30, zmax=50)