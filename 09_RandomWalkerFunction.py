#Random Walker 1.0
#David Tracy for Black Spex
#May 2016

import rhinoscriptsyntax as rs
import random

def step():
    coordinates = []
    x = random.uniform(-1,1)
    coordinates.append(x)
    y = random.uniform(-1,1)
    coordinates.append(y)
    z = random.uniform(-1,1)
    coordinates.append(z)
    return coordinates

location = [0,0,0]

points = []

for i in range(500):
    randomPoints = step()
    point = rs.AddPoint(location[0]+randomPoints[0], location[1]+randomPoints[1], location[2]+randomPoints[2])
    location = (location[0]+randomPoints[0], location[1]+randomPoints[1], location[2]+randomPoints[2])
    points.append(point)

rs.AddCurve(points)
rs.AddPolyline(points)