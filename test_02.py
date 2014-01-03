import numpy as np
import scipy
import pylab
import pymorph
import mahotas
from scipy import ndimage

image = mahotas.imread('/Users/melonbreath/Dropbox/Programming/NEDCC Project/files/Example_Leafcasting_Photo_Plum_Print.jpg')
pylab.imshow(image)
pylab.gray()
pylab.show()

print image.shape
print image.dtype
print image.max()
print image.min()

for y in image.shape[0]:
    print image[0,y]