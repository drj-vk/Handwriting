import cv2
import scipy.ndimage as ndi
import scipy
import numpy
import Image
import math
from Groep2.preprocessing import thinning, prepImage



#def Edge_Maps(img):
# load an color image in grayscale
img = cv2.imread('h.jpg', cv2.IMREAD_GRAYSCALE)

#the preprocessor object
prepper = prepImage.PreProcessor()
img = prepper.bgSub(img)
binary = prepper.binarize(img)
thin = thinning.thinning(binary)


sobelout = Image.new('L', (thin.shape[1],thin.shape[0]))                                       #empty image
gradx = numpy.array(sobelout, dtype = float)
grady = numpy.array(sobelout, dtype = float)
gradup = numpy.array(sobelout, dtype = float)
graddown = numpy.array(sobelout, dtype = float)


sobel_x = [[-1,2,-1],
           [-1,2,-1],
           [-1,2,-1]]
sobel_y = [[-1,-1,-1],
           [2,2,2],
           [-1,-1,-1]]

sobel_up = [[-1,-1,2],
           [-1,2,-1],
           [2,-1,-1]]

sobel_down = [[2,-1,-1],
           [-1,2,-1],
           [-1,-1,2]]


width = thin.shape[1]
height = thin.shape[0]

for x in range(1, height-1):
    for y in range(1, width-1):
        px = (sobel_x[0][0] * thin[x-1][y-1]) + (sobel_x[0][1] * thin[x][y-1]) + \
             (sobel_x[0][2] * thin[x+1][y-1]) + (sobel_x[1][0] * thin[x-1][y]) + \
             (sobel_x[1][1] * thin[x][y]) + (sobel_x[1][2] * thin[x+1][y]) + \
             (sobel_x[2][0] * thin[x-1][y+1]) + (sobel_x[2][1] * thin[x][y+1]) + \
             (sobel_x[2][2] * thin[x+1][y+1])
        py = (sobel_y[0][0] * thin[x-1][y-1]) + (sobel_y[0][1] * thin[x][y-1]) + \
             (sobel_y[0][2] * thin[x+1][y-1]) + (sobel_y[1][0] * thin[x-1][y]) + \
             (sobel_y[1][1] * thin[x][y]) + (sobel_y[1][2] * thin[x+1][y]) + \
             (sobel_y[2][0] * thin[x-1][y+1]) + (sobel_y[2][1] * thin[x][y+1]) + \
             (sobel_y[2][2] * thin[x+1][y+1])

        pup = (sobel_up[0][0] * thin[x-1][y-1]) + (sobel_up[0][1] * thin[x][y-1]) + \
             (sobel_up[0][2] * thin[x+1][y-1]) + (sobel_up[1][0] * thin[x-1][y]) + \
             (sobel_up[1][1] * thin[x][y]) + (sobel_up[1][2] * thin[x+1][y]) + \
             (sobel_up[2][0] * thin[x-1][y+1]) + (sobel_up[2][1] * thin[x][y+1]) + \
             (sobel_up[2][2] * thin[x+1][y+1])
        pdown = (sobel_down[0][0] * thin[x-1][y-1]) + (sobel_down[0][1] * thin[x][y-1]) + \
             (sobel_down[0][2] * thin[x+1][y-1]) + (sobel_down[1][0] * thin[x-1][y]) + \
             (sobel_down[1][1] * thin[x][y]) + (sobel_down[1][2] * thin[x+1][y]) + \
             (sobel_down[2][0] * thin[x-1][y+1]) + (sobel_down[2][1] * thin[x][y+1]) + \
             (sobel_down[2][2] * thin[x+1][y+1])

        gradx[x][y] = max(px-2,0)
        grady[x][y] = max(py-2,0)
        gradup[x][y] = max(pup-2,0)
        graddown[x][y] = max(pdown-2,0)


#show the image
cv2.imshow('image',gradx)
cv2.waitKey(0)
cv2.destroyAllWindows()