import math

def getTriangleArea(sideA , sideB, sideC):

    if ( sideA < 0 ) or ( sideB < 0 )  or ( sideC < 0 ) or (sideA + sideB <= sideC ) or ( sideA + sideC <= sideB ) or ( sideB + sideC <= sideA ):
        print "Invalid triangle."
    else:
        x = ( sideA + sideB + sideC ) / 2.0
        area = math.sqrt( x * ( x - sideA ) *  ( x - sideB ) * ( x - sideC ) )
        print "The area of a triangle with sides", sideA, sideB, sideC, "is", area 
