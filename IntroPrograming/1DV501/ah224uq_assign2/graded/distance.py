from math import sqrt
def distance(x1,y1,x2,y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

#starting main
x1 = float(input("Enter x1:"))
y1 = float(input("Enter y1:"))
x2 = float(input("Enter x2:"))
y2 = float(input("Enter y2:"))

result_distance = round(distance(x1,y1,x2,y2), 3)
print("The distance between ",x1,y1," and ",x2,y2," is ", result_distance)
 