#David Tracy for BlackSpectacles.com
#May 2016

import rhinoscriptsyntax as rs

#set a variable to access the Object you select
shape = rs.GetObject("Select an object please:")
rs.MoveObject(shape, (0,10,0) )

#You can redefine the variable you used earlier
#because operations are run sequentially
shape = rs.GetObject("Select an object please:")
rs.RotateObject(shape, rs.GetPoint("Select Centroid"), 45)

#use vectors to transform
#VectorCreate takes the destination argument first!
start = rs.VectorCreate([0,0,0],[0,0,0])
end = rs.VectorCreate([20,10,0],[0,0,0])
transform = rs.VectorAdd(end,start)
print(transform)
shape = rs.GetObject("Select an object please:")
rs.MoveObject(shape, transform )