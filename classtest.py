import numpy as np

class Cube:
    def __init__(self,xa,ya,za,len_a,xb,yb,zb,len_b):
        # (xa,ya,za) are the center cordinates of cube-a , len_a is the edge length of cube a,
        # (xb,yb,zb) are the center cordinates of cube-b, len_b is the edge length of cube b.
        self.xa = xa
        self.ya = ya
        self.za = za
        self.len_a = len_a
        self.xb = xb
        self.yb = yb
        self.zb = zb
        self.len_b = len_b
        # we are making za,zb are zeros(0) because to prevent rotation of the cubes.
        assert za ==0, f"cube Z-axis {za} is not equal to 0 - please enter 0"
        assert zb ==0, f"cube Z-axis {zb} is not equal to 0 - please enter 0"
    
    def intersect(self):
        # We are determining starting point and ending point of cube on x-axis.
        # By using the center point of cube and length of cube.
        new_xal = (self.xa-(self.len_a/2))
        new_xa2 = (self.xa+(self.len_a/2))
        new_xbl = self.xb-(self.len_b/2)
        new_xb2 = self.xb+(self.len_b/2)
   
        # We are determining starting point and ending point of cube on x-axis.
        # By using the center point of cube and length of cube.

        new_yal = (self.ya-(self.len_a/2))
        new_ya2 = (self.ya+(self.len_a/2))
        new_ybl = self.yb-(self.len_b/2)
        new_yb2 = self.yb+(self.len_b/2)
        

        # Range of co-ordinates for X&Y-axis are appended into list.

        # Cube-a x-axis
        new_list_x1 = []
        list_x1 = np.arange(new_xal,new_xa2+0.5,0.5)
        new_list_x1.append(list_x1)
        
        # cube-b X-axis
        list_x2 = np.arange(new_xbl,new_xb2+0.5,0.5)
        new_list_x2 = []
        new_list_x2.append(list_x2)

        # cube-a y-axis 
        list_y1 = np.arange(new_yal,new_ya2+0.5,0.5)
        new_list_y1 = []
        new_list_y1.append(list_y1)
        
        # cube-b y-axis.
        list_y2 = np.arange(new_ybl,new_yb2+0.5,0.5)
        new_list_y2 = []
        new_list_y2.append(list_y2)

        # Finding Instercts of cube-a & b using numpy.
        ax= np.intersect1d(new_list_x1, new_list_x2)
        ay= np.intersect1d(new_list_y1, new_list_y2)
        
        # The Intersected cube may be square/rectangle.
        # For this reason, we are caluculating l,b,h to find volume of rectangle intersection.
        # length of the intersected edge is taken from the axis.
        # last value in the list(-)first value in the list gives length of intersected edge.

        l = ax[len(ax)-1]-ax[0]
        b = ay[len(ay)-1]-ay[0]
        h = min(self.len_a,self.len_b)

        while len(ax)>=1:
            if l == b:  # for the square intersected cube.
                vol = l*l*l
                print("True,",vol)
                break
            else: # for the rectangle intersected cube.
                vol = l*b*h
                print("True,",vol)   
                break    
        else:  # No intersection.
            print("False, 0" )
      
        
    def __str__(self):
        return f"Cube('{self.xa}', {self.ya},{self.za},{self.la},{self.xb},{self.yb},{self.zb},{self.lb})"


test1 = Cube(8,4,0,5,5,3,0,6)
test1.intersect()
