from __future__ import print_function
import os
import numpy as np
from PIL import Image, ImageEnhance

#read image
image = Image.open('test.jpg')
print (image.format, image.size, image.mode)

#filter
test = np.array(image)
def warmfilter (img):
    temp = np.array(img)
    temp[:,:,0] = temp[:,:,0] + (255 - np.amax(temp[:,:,0]))  #Red
    temp[:,:,1] = temp[:,:,1] + (255 - np.amax(temp[:,:,1]))  #Green
    temp[:,:,2] = temp[:,:,2] + (255 - np.amax(temp[:,:,2]))  #Blue
    temp = Image.fromarray(temp)
    temp = ImageEnhance.Color(temp).enhance(1.1) 
    return temp

def coolfilter (img):
    temp = np.array(img)
    temp[:,:,0] = temp[:,:,0]*0.9  #Red
    temp[:,:,1] = temp[:,:,1] + (255 - np.amax(temp[:,:,1]))*0.5 #Green
    temp[:,:,2] = temp[:,:,2] + (255 - np.amax(temp[:,:,2]))*0.5 #Blue
    temp = Image.fromarray(temp)
    temp = ImageEnhance.Color(temp).enhance(0.95)
    return temp

#run
out = warmfilter(test)
out.show()
out = coolfilter(test)
out.show()

#output
out.save('out.bmp')