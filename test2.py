import numpy as np
xa = 10
ya = 15
za = 0
xb = 6
yb = 12
zb = 0
la = 6
lb =8

# new cordinates x-axis
new_xal = (xa-(la/2))
new_xa2 = (xa+(la/2))
new_xbl = xb-(lb/2)
new_xb2 = xb+(lb/2)

# new cordinates y-axis
new_yal = (ya-(la/2))
new_ya2 = (ya+(la/2))
new_ybl = yb-(lb/2)
new_yb2 = yb+(lb/2)

# list function for x-axis

list_x1 = np.arange(new_xal,new_xa2+0.5,0.5)
new_list_x1 = []
new_list_x1.append(list_x1)
print((new_list_x1))

list_x2 = np.arange(new_xbl,new_xb2+0.5,0.5)
new_list_x2 = []
new_list_x2.append(list_x2)
print((new_list_x2))

# list function for y-axis
# list function

list_y1 = np.arange(new_yal,new_ya2+1,0.5)
new_list_y1 = []
new_list_y1.append(list_y1)
print((new_list_y1))

list_y2 = np.arange(new_ybl,new_yb2+1,0.5)
new_list_y2 = []
new_list_y2.append(list_y2)
print((new_list_y2))

ax= np.intersect1d(new_list_x1,new_list_x2)
ay= np.intersect1d(new_list_y1,new_list_y2)
print(ax)
print(ay)
# code for intersection
if len(ax) ==0:
    print("No Intersect")
else:
    print("Intersect")
l = len(ax)/2
b = len(ay)/2
h = min(la,lb)
vol = l*b*h
print(vol)

