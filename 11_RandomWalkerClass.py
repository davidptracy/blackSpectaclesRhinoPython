#Script Information

#import statements
import rhinoscriptsyntax as rs
import random

class Walker:
    def __init__(self):
        self.x = 0 
        self.y = 0
        self.z = 0
        self.shape = 0
        
    def getLocation(self):
        return self.shape
        
    def step(self):
        stepX = random.uniform(-1,1)
        self.x += stepX
        stepY = random.uniform(-1,1)
        self.y += stepY
        stepZ = random.uniform(-1,1)
        self.z += stepZ
        self.shape = rs.AddPoint(self.x,self.y, self.z)
        return self.shape

w = Walker()
w1 = Walker()
w2 = Walker()

points = []
points1 = []
points2 = []

radii = []
radii1 = []
radii2 = []

parameters = []
parameters1 = []
parameters2 = []

for i in range(100):
    w.step()
    points.append(w.getLocation())
    w1.step()
    points1.append(w1.getLocation())
    w2.step()
    points2.append(w2.getLocation())

parameterCounter = 0.0
parameterCounter1 = 0.0
parameterCounter2 = 0.0
for point in points:
    tempRadius = random.uniform(.05,.25)
    tempRadius1 = random.uniform(.05,.25)
    tempRadius2 = random.uniform(.05,.25)
    radii.append(tempRadius)
    radii1.append(tempRadius)
    radii2.append(tempRadius)
    parameters.append(parameterCounter)
    parameters1.append(parameterCounter)
    parameters2.append(parameterCounter)
    parameterCounter += 1/len(points)
    parameterCounter1 += 1/len(points)
    parameterCounter2 += 1/len(points)

curve = rs.AddCurve(points)
curve1 = rs.AddCurve(points1)
curve2 = rs.AddCurve(points2)


rs.AddPipe(curve, parameters, radii, 1, 2, False)
rs.AddPipe(curve1, parameters1, radii1, 1, 2, False)
rs.AddPipe(curve2, parameters2, radii2, 1, 2, False)

