from vpython import *
from time import *

# x is length
# y is height
# z is width

mRadius = .75
wallThickness = .1
roomWidth = 50
roomDepth = 50
roomHeight = 50

floor = box(pos=vector(0, -roomHeight/2, 0), color=color.white,
            size=vector(roomWidth, wallThickness, roomDepth))

ceiling = box(pos=vector(0, roomHeight/2, 0), color=color.white,
              size=vector(roomWidth, wallThickness, roomDepth))

leftWall = box(pos=vector(-roomWidth/2, 0, 0), color=color.cyan,
               size=vector(wallThickness, roomHeight, roomDepth))

rightWall = box(pos=vector(roomWidth/2, 0, 0), color=color.yellow,
                size=vector(wallThickness, roomHeight, roomDepth))

backWall = box(pos=vector(0, 0, -roomDepth/2), color=color.green,
               size=vector(roomWidth, roomHeight, wallThickness))

ball = sphere(radius=mRadius, color=color.red)

dx = .1
dy = .8
dz = .6
xPos = 0
yPos = 0
zPos = 0

while True:
    rate(30)
    xPos = xPos + dx
    yPos = yPos + dy
    zPos = zPos + dz

    if xPos > (roomWidth-mRadius)/2 or xPos < -(roomWidth-mRadius)/2:
        dx = dx*(-1)

    if yPos > (roomHeight-mRadius)/2 or yPos < -(roomHeight-mRadius)/2:
        dy = dy*(-1)

    if zPos > (roomDepth-mRadius)/2 or zPos < -(roomDepth-mRadius)/2:
        dz = dz*(-1)

    ball.pos = vector(xPos, yPos, zPos)
    pass
