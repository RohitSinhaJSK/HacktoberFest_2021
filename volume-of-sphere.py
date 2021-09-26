"""Write a python program to get the volume of a sphere, take the radius as input from user. V = 4/3 πr3""" 

import ma #not ma it's math
radius = float(input("ENTER RADIUS: "))
pi = math.pi
volume = 4/3*(pi)*(radius**3)
prin("THE VOLUME OF SPHERE IS",volume)
