import rhinoscriptsyntax as rs
import math
import time

#myVectorEnd = rs.VectorCreate((1,1,0),(0,0,0))
#myVectorStart = rs.VectorCreate((2,0,0),(0,0,0))

#print(rs.VectorAdd(myVectorStart,-myVectorEnd))

#math.sin()

#select an object
#move it 10 units to the right
shape = rs.GetObject("Select your object:")
#rs.MoveObject(shape, [10,0,0])
#rs.RotateObject(shape, rs.GetPoint(), 30)

centerOfRotate = rs.GetPoint("Specify Center of Rotation, Please")

#speed = rs.GetInteger("Specify Speed, please")


count = 0
while count < 1000:
    speed = 5*math.sin(time.time())
    rs.RotateObject(shape, centerOfRotate, speed)
    count += 1