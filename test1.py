import numpy as np
xa = 10
ya = 10
za = 0
xb = 5
yb = 5
zb = 0
la = 6
lb =8
# our new co-ordinates
new_xal = (xa-(la/2))
new_xa2 = (xa+(la/2))
new_xbl = xb-(lb/2)
new_xb2 = xb+(lb/2)
# list function

list1 = np.arange(new_xal,new_xa2+1,0.5)
new_list1 = []
new_list1.append(list1)
print((new_list1))

list2 = np.arange(new_xbl,new_xb2+1,0.5)
new_list2 = []
new_list2.append(list2)
print((new_list2))

a= np.intersect1d(new_list1,new_list2)
print(a)
b = len(a)/2
print(b)
vol = b*b*b
print(vol)
if len(a) ==0:
    print("No Intersect")
else:
    print("Intersect")