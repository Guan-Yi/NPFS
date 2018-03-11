
import sys
import numpy as np
from PIL import Image, ImageEnhance

def warm (img):
    temp = np.array(img)
    temp[:,:,0] = temp[:,:,0] + (255 - np.amax(temp[:,:,0]))  #Red
    temp[:,:,1] = temp[:,:,1] + (255 - np.amax(temp[:,:,1]))  #Green
    temp[:,:,2] = temp[:,:,2] + (255 - np.amax(temp[:,:,2]))  #Blue
    temp = Image.fromarray(temp)
    temp = ImageEnhance.Color(temp).enhance(1.1) 
    return temp

def cool (img):
    temp = np.array(img)
    temp[:,:,0] = temp[:,:,0]*0.9  #Red
    temp[:,:,1] = temp[:,:,1] + (255 - np.amax(temp[:,:,1]))*0.5 #Green
    temp[:,:,2] = temp[:,:,2] + (255 - np.amax(temp[:,:,2]))*0.5 #Blue
    temp = Image.fromarray(temp)
    temp = ImageEnhance.Color(temp).enhance(0.95)
    return temp

def nippon (img):
    temp = np.array(img)
    temp[:,:,0] = temp[:,:,0]*0.82  #Red
    temp[:,:,1] = (temp[:,:,1] + (255 - np.amax(temp[:,:,1])))*0.85 #Green
    temp[:,:,2] = (temp[:,:,2] + (255 - np.amax(temp[:,:,2]))) #Blue
    temp = Image.fromarray(temp)
    temp = ImageEnhance.Color(temp).enhance(0.7)
    temp = ImageEnhance.Brightness(temp).enhance(1.8)
    temp = ImageEnhance.Contrast(temp).enhance(0.7)
    return temp

def main (image, filter_type):
    origin_image = Image.open(image)
    if (filter_type == 'warm'):
        new_image = warm(origin_image)
    elif (filter_type == 'cool'):
        new_image = cool(origin_image)
    else:
        new_image = nippon(origin_image)
    
    new_image.save('test.png')
    return new_image
        
if __name__ == "__main__":
    img_name = str(sys.argv[1])
    select_filter = str(sys.argv[2])
    main(img_name, select_filter)
    
