import cv2
import manus
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('camera1.jpg')
# h_mat = load_h('camera1.txt') #homography matrix
# h_mat = np.linalg.inv(h_mat) #invert the matrix
# %matplotlib 

# print(h_mat)

#draw the grid on the image by connecting the first and last row and column of the grid
def draw_grid(img, points):
    for (x,y) in points:
        if x == 0:
            cv2.line(img, (int(x),int(y)), (int(x+200),int(y)), (0,0,255), 1)
        if y == 0:
            cv2.line(img, (int(x),int(y)), (int(x),int(y+200)), (0,0,255), 1)
    return img    

class Grid:
    points = []
    h = ()
    w = ()
    x = ()
    y = ()
    def __init__(self, x,y,h,w):
        self.h = h
        self.w = w
        self.x = x
        self.y = y
        self.grid_points()
        
    def grid_points(self): # x,y - number of points in grid, h,w - height and width of the grid
        self.points = np.zeros((self.x,self.y,2))
        for i in range(self.x):
            for j in range(self.y):
                self.points[i][j] = (i*self.h/self.x, j*self.w/self.y)
                
    
    def draw_grid(self, img, color=(0,0,255)):
        for x in range(self.x):
            for y in range(self.y):
                if x == 0:
                    cv2.line(img, (int(self.points[x][y][0]),int(self.points[x][y][0])), (int(self.points[-1][y][0]),int(self.points[-1][y][0])), color, 1)
                if y == 0:
                    cv2.line(img, (int(self.points[x][y][0]),int(self.points[x][y][0])), (int(self.points[x][-1][0]),int(self.points[x][-1][0])), color, 1)
                # draw points
        return img
                

#change image to rgb
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

grid = Grid(10,10,200,200)

#display image and the grid on top of it
plt.figure()

#draw the homography grid on the image
# img = draw_grid(img, grid_points(10, 10,200,200))
img = grid.draw_grid(img)
# plt.axis('off')
plt.imshow(img)
plt.show()