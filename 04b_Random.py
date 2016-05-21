#Script Info

import rhinoscriptsyntax as rs
import random

uniformRandom = random.uniform(-1,1)
gausRamdom = random.gauss(0,10)

count=0
while count<500:
    x = random.gauss(0,10)
    y = random.gauss(0,10)
    z = random.gauss(0,10)
    rs.AddPoint(x,y,z)
    count+=1
