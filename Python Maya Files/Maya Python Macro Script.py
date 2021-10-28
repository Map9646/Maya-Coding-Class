cmds.polySphere(axis=[0, 1, 0], constructionHistory=1, createUVs=2, radius=1, subdivisionsX=20, subdivisionsY=20)

cmds.polySphere(axis=[0, 1, 0], constructionHistory=1, createUVs=2, radius=1, subdivisionsX=20, subdivisionsY=20)
cmds.move(0, 0.66217, 0, relative=True)
cmds.scale(0.7, 0.7, 0.7)
cmds.move(0, 1, 0, relative=True)

cmds.polySphere(axis=[0, 1, 0], constructionHistory=1, createUVs=2, radius=1, subdivisionsX=20, subdivisionsY=20)
cmds.move(0, 1.8, 0, relative=True)
cmds.scale(0.6, 0.6, 0.6)

cmds.polySphere(axis=[0, 1, 0], constructionHistory=1, createUVs=2, radius=1, subdivisionsX=20, subdivisionsY=20)

cmds.scale(0.1, 0.1, 0.1)
cmds.move(0.55, 0, 0, relative=True)
cmds.move(0, 1.9, 0, relative=True)
cmds.move(0, 0, -0.2, relative=True)
cmds.duplicate(smartTransform=True)

cmds.move(0, 0, 0.4, relative=True)

cmds.duplicate(smartTransform=True)
cmds.move(0, 0, -0.6, relative=True)
cmds.move(0, -0.2, 0, relative=True)
