import rhinoscriptsyntax as rs
import random
import time

print(random.uniform(1.0,100.0))
print(random.gauss(20.0, 0.5))

#create a bunch of random points
basePoint = rs.GetPoint("Pick a base point")
steps = 0

while steps < 1000:
#    x=random.uniform(0.0,20.0)
#    y=random.uniform(0.0,20.0)
#    z=random.uniform(0.0,20.0)
    x=random.gauss(1.0, 20.0)
    y=random.gauss(1.0, 20.0)
    z=random.gauss(1.0, 20.0)

    rs.AddPoint( basePoint[0]+x, basePoint[1]+y, 0 )
    steps+=1