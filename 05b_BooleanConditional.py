#Script Info

import rhinoscriptsyntax as rs

a = False
b = 3

#Conditional statements
if a is True:
    print("The Truth!")
else:
    print("It was all a lie!")

#evaluating b
if b>10:
    print("It was greater than 10!")
elif b is 5:
    print("It was 5!")
else:
    print("It was something else entirely")
