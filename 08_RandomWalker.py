import rhinoscriptsyntax as rs
import random

location = rs.GetPoint("Select a point")

for i in range(500):    
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)    
    rs.AddPoint([location[0]+x, location[1]+y, 0])    
    location = [location[0]+x, location[1]+y, 0]
#Take it to the 3rd Dimension!