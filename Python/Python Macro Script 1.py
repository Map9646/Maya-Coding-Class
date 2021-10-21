import maya.cmds as cmds

cmds.polySphere(axis=[0, 1, 0], constructionHistory=1, createUVs=2, radius=1, subdivisionsX=20, subdiviionsY=20)

cmds.polySphere(axis=[0, 1, 0], constructionHistory=1, createUVs=2, radius=1, subdivisionsX=20, subdiviionsY=20)
cmds.move(0, 0.66217, 0[polySphere2])
cmds.scale(0.7, 0.7, 0.7[polySphere2])
cmds.move(0, 0.4, 0[polySphere1])

cmds.polySphere(axis=[0, 1, 0], constructionHistory=1, createUVs=2, radius=1, subdivisionsX=20, subdiviionsY=20)
cmds.move(0, 0.45, 0[polySphere2])
cmds.scale(0.6, 0.6, 0.6[polySphere2])

cmds.polySphere(axis=[0, 1, 0], constructionHistory=1, createUVs=2, radius=1, subdivisionsX=20, subdiviionsY=20)
cmds.move(2, 0, 0[polySphere3])
cmds.move(0, 0.4, 0[polySphere3])
cmds.move(0, -0.2, 0[polySphere3])
cmds.duplicate([polySphere3])
cmds.move(0, -0.4, 0[polySphere3])
cmds.move(0.1, 0, 0[polySphere3])

cmds.polySphere(axis=[0, 1, 0], constructionHistory=1, createUVs=2, radius=1, subdivisionsX=20, subdiviionsY=20)
cmds.move(0, 2, 0[polySphere4])
cmds.move(0.4, 0, 0[polySphere4])
cmds.move(0, 0, -0.2[polySphere4])
cmds.scale(0.3, 0.3, 0.3[polySphere4])
cmds.duplicate([polySphere4])
cmds.move(0, 0, 0.3[polySphere])
cmds.move(0, 0, -0.1[polySphere])
cmds.move(-0.02, 0, 0[polySphere4])

cmds.polySphere(axis=[0, 1, 0], constructionHistory=1, createUVs= 2, radius=1, subdivisionsX=20, subdiviionsY=20)
cmds.rotate(0, 0, -90[polySphere5])
cmds.move(-2, 0, 0[polySphere5])
cmds.scale(0.2, 0.2, 0.2[polySphere5])
cmds.move(0, 0.5, 0[polysphere5])
cmds.move(0, -0.03, 0[polySphere5])
cmds.move(0, 0, -0.03[polySphere5])
cmds.move(0.03, 0, 0[polySphere5])
cmds.duplicate([polySphere5])
cmds.move(0, -0.1, 0[polySphere5])
cmds.move(0, 0, 0.1[polySphere5])
cmds.duplicate([polySphere5])
cmds.move(0, 0, 0.3[polySphere5])
cmds.select()



