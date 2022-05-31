#The circle module has functions that
#perform calculatios related to circles
import math

#the area funciton accepts a cricle's radius as an
#argument and returns the area of the circle
def area(radius):
    return math.pi * radius**2

#the circumference function accepts a circle's
#radius and returs the circle's circumference
def circumference(radius):
    return 2 * math.pi * radius
    