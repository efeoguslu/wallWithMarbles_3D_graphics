from vpython import *
from time import *

# x is length
# y is height
# z is width

mRadius = float(input("enter radius of marble: "))
wallThickness = float(input("enter wall thickness: "))
roomWidth = float(input("enter room width: "))
roomDepth = float(input("enter room depth: "))
roomHeight = float(input("input room height: "))

dx = float(input(
    "enter change of speed in x axis (better if you choose between 0 and 1): "))
dy = float(input(
    "enter change of speed in y axis (better if you choose between 0 and 1): "))
dz = float(input(
    "enter change of speed in z axis (better if you choose between 0 and 1): "))

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

xPos = 0
yPos = 0
zPos = 0

while True:
    rate(50)

    xPos = xPos + dx
    xrme = xPos + mRadius
    xlme = xPos - mRadius
    rwe = roomWidth/2 - wallThickness/2
    lwe = -roomWidth/2 + wallThickness/2

    yPos = yPos + dy
    yrme = yPos + mRadius
    ylme = yPos - mRadius
    cwe = roomHeight/2 - wallThickness/2
    fwe = -roomHeight/2 + wallThickness/2

    zPos = zPos + dz
    zrme = zPos + mRadius
    zlme = zPos - mRadius
    frwe = roomDepth/2 - wallThickness/2
    bwe = -roomDepth/2 + wallThickness/2

    if xrme >= rwe or xlme <= lwe:
        dx = dx*(-1)

    if yrme >= cwe or ylme <= fwe:
        dy = dy*(-1)

    if zrme >= frwe or zlme <= bwe:
        dz = dz*(-1)

    ball.pos = vector(xPos, yPos, zPos)
    pass
