import numpy as np
import scipy
import pylab
import pymorph
import mahotas
from scipy import ndimage

dna = mahotas.imread('/Users/melonbreath/Dropbox/Programming/NEDCC Project/dna.jpg')
pylab.imshow(dna)
pylab.gray()
pylab.show()

print dna.shape
print dna.dtype
print dna.max()
print dna.min()