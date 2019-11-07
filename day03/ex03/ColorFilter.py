#!/usr/bin/env python

from ImageProcessor import ImageProcessor
import numpy as np

class ColorFilter:
    
    @staticmethod
    def invert(array):
        return 255 - array

    def to_blue(self, array):
        img = np.zeros(array.shape)
        img[:,:,2] = array[:,:,2]
        return img

    def to_green(self, array):
        return array * np.array([0,1,0]) 

    def to_red(self, array):
        return array - self.to_green(array) - self.to_blue(array)

    @staticmethod
    def celluloid(array, k):
        group = int(255 / k)
        new = array / group
        new = new.astype('int', copy=False)
        new *= group
        return new
        


if __name__ == '__main__':
    im = ImageProcessor()
    arr = im.load('../resources/Toon-shader.jpg')
    print(arr[:10,0,0])
    print(arr.shape)
    #im.display(arr)

    fil = ColorFilter()
    
    #inv = fil.invert(arr)
    #im.display(inv)

    #blu = fil.to_blue(arr)
    #im.display(blu)

    # gre = fil.to_green(arr)
    # print(gre.shape)
    # im.display(gre)

    # red = fil.to_red(arr)
    # print(red.shape)
    # im.display(red)

    cel = fil.celluloid(arr, 3)
    # print(cel.shape)
    im.display(cel)

