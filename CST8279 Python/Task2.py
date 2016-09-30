#Author: Brett Sheehan 040759671
#Lab4: Task2
#Written in: python 3.5

import math

def pointCalculation(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    sum = math.sqrt( ((x2-x1)**2) + ((y2 - y1)**2) )
    return sum

def getValues():
    values = [float(x) for x in input(">>> ").split()]
    while len(values) != 2:
        print("Wrong number of values: ")
        values = [float(x) for x in input().split()]
    return values

print("Enter in Two Values for each point:")
point1 = getValues()
point2 = getValues()
finalDif = pointCalculation(point1, point2)

print("The Difference between both points is: ", round(finalDif))
