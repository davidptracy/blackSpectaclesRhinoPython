#import statements
import rhinoscriptsyntax as rs
import math

#transform on a sine wave!
time=0.0
shape = rs.GetObject("Select an object please:")
while time<2*math.pi:
    rs.MoveObject(shape, (0, math.sin(time), 0))
    time += 0.01
#make some other movement