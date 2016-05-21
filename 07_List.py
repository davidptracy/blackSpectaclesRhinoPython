#Some info about our script

import rhinoscriptsyntax as rs

points = []

point1 = rs.GetPoint("Select a point")
points.append(point1)

point2 = rs.GetPoint("Select a point")
points.append(point2)

point3 = rs.GetPoint("Select a point")
points.append(point3)

point4 = rs.GetPoint("Select a point")
points.append(point4)

#automatically iterating
#for point in points:
#    print(point)
    
for i in range(4):
    print(points[i])