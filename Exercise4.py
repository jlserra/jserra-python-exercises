from AreaIdentifier.Circle import *
from AreaIdentifier.Triangle import *
from AreaIdentifier.Rectangle import *

try: 
   circleRadius = (raw_input("Enter Radius of Circle: "))
   getCircleArea(float(circleRadius))
except ValueError:
    print "Invalid value of radius entered"

try:
    sideA, sideB, sideC = (raw_input("Enter the 3 sides of Triangle (separated by space) ")).split()
    getTriangleArea(float(sideA),float(sideB),float(sideC))
except ValueError:
    print "Invalid value of triangle sides entered"
    
try:
    length, width = (raw_input("Enter Length and Width of Rectangle: ")).split()
    getRectangleArea(float(length),float(width))
except ValueError:
     print "Invalid value of length or width entered"
