

ax =[1,2,3,4]
ay = [1,2,3,4]
h =6

if len(ax) == len(ay): # condition for square intersection
    vol = len(ax)*len(ax)*len(ax)
    print(vol)
else: # condition for rectangle intersection
    vol = len(ax)*len(ay)*h # h=height, we take min of both cube
    print(vol)