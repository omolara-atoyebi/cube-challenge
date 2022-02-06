from matplotlib.pyplot import axes
import numpy as np

class Cube:
    def __init__(self,xa,ya,za,la,xb,yb,zb,lb,):
        self.xa = xa
        self.ya = ya
        self.za = za
        self.la = la
        self.xb = xb
        self.yb = yb
        self.zb = zb
        self.lb = lb
    
    def x_cordinates(self):
        new_xal = (self.xa-(self.la/2))
        new_xa2 = (self.xa+(self.la/2))
        new_xbl = self.xb-(self.lb/2)
        new_xb2 = self.xb+(self.lb/2)
        return(new_xal,new_xa2,new_xbl,new_xb2)
    
    def y_cordinates(self):
        new_yal = (self.ya-(self.la/2))
        new_ya2 = (self.ya+(self.la/2))
        new_ybl = self.yb-(self.lb/2)
        new_yb2 = self.yb+(self.lb/2)
        return(new_yal,new_ya2,new_ybl,new_yb2)

    def list_x_axis(self):
        new_list_x1 = []
        list_x1 = np.arange(self.new_xal,self.new_xa2+0.5,0.5)
        new_list_x1.append(list_x1)
        

        list_x2 = np.arange(self.new_xbl,self.new_xb2+0.5,0.5)
        new_list_x2 = []
        new_list_x2.append(list_x2)

        return new_list_x1, new_list_x2 
    

    def list_y_axis(self):
        list_y1 = np.arange(self.new_yal,self.new_ya2+1,0.5)
        new_list_y1 = []
        new_list_y1.append(list_y1)
        

        list_y2 = np.arange(self.new_ybl,self.new_yb2+1,0.5)
        new_list_y2 = []
        new_list_y2.append(list_y2)

        ax= np.intersect1d(self.new_list_x1, self.new_list_x2)
        ay= np.intersect1d(self.new_list_y1,self.new_list_y2)

        if len(ax) ==0:
            print("No Intersect")
        else:
            print("Intersect")
        
        

    #def intersect(self):
        #ax= np.intersect1d(self.new_list_x1, self.new_list_x2)
        #ay= np.intersect1d(self.new_list_y1,self.new_list_y2)
        

        # code for intersection
        #if len(self.ax) ==0:
            #print("No Intersect")
        #else:
            #print("Intersect")

        #return(ax, ay)

    def __str__(self):
        return f"Cube('{self.xa}', {self.ya},{self.za},{self.la},{self.xb},{self.yb},{self.zb},{self.lb})"


test1 = Cube(10,15,0,6,6,12,0,8)
test1.list_y_axis()

   