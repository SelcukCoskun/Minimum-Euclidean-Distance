points=[(1,2),(2,3),(3,4),(5,6),(6,7)] #A list representing points in 2D space

def euclideanDistance(point1,point2):#Function that calculates Euclidean distance
    x1,y1=point1
    x2,y2=point2                    #  First import the math module.  import math
    d=((x2-x1)**2+(y2-y1)**2) ** 0.5#  math.sqrt((x2-x1)**2+(y2-y1)**2))
    return d

distances=[]#Calculates the Euclidean distance between any two points.
for i in range(len(points)):
    for j in range(i+1,len(points)):
        distances.append(euclideanDistance(points[i],points[j]))

for k in distances:#Prints distances
    print(k)

print("minimum distance=",min(distances))