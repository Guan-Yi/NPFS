from __future__ import print_function
import os
import numpy as np
from PIL import Image, ImageEnhance
import itertools

#read image
image = Image.open('test.jpg')
print (image.format, image.size, image.mode)

#parameter combination
green_p = np.arange(0.1, 1.0, 0.05)
blue_p = np.arange(0.1, 1.0, 0.05)
p_pair = list(itertools.product(green_p, blue_p))

#makedir

#test
for i in range(len(p_pair)):
    temp = np.array(image)
    temp[:,:,0] = temp[:,:,0]*0.8 #Red
    temp[:,:,1] = (temp[:,:,1] + (255 - np.amax(temp[:,:,1])))* p_pair[i][0] #Green
    temp[:,:,2] = (temp[:,:,2] + (255 - np.amax(temp[:,:,2])))* p_pair[i][1] #Blue
    temp = Image.fromarray(temp)
    temp = ImageEnhance.Color(temp).enhance(0.8)
    temp = ImageEnhance.Brightness(temp).enhance(1.5)
    temp = ImageEnhance.Contrast(temp).enhance(0.8)
    temp.save(str(i)+'.bmp')