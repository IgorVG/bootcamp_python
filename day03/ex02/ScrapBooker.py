#!/usr/bin/env python

from ImageProcessor import ImageProcessor
import numpy as np


class ScrapBooker:
    @staticmethod
    def crop(array, dimensions, position=(0, 0)):
        x_l = position[0]
        x_r = position[0] + dimensions[0]
        y_l = position[1]
        y_r = position[1] + dimensions[1]
        if all(np.array(dimensions) + np.array(position)
               < np.array(array.shape[:2])):
            return array[x_l: x_r, y_l: y_r]
        else:
            print("Specified dimensions exceeds current shape")

    @staticmethod
    def thin(array, n, axis):
        axis = 1 - axis
        if n > 0:
            slc = slice(n-1, array.shape[axis], n)
            return np.delete(array, slc, axis=axis)
        else:
            return array

    @staticmethod
    def juxtapose(array, n, axis):
        return np.concatenate([array] * n, axis=axis)

    @staticmethod
    def mosaic(array, dimensions):
        return np.tile(array, dimensions + (1,))


if __name__ == '__main__':
    img = ImageProcessor()
    arr = img.load("../resources/42AI.png")
    print(np.array(arr.shape[:2]))

    img.display(arr)

    imop = ScrapBooker()

    crop_arr = imop.crop(arr, (100, 100), (20, 20))
    img.display(crop_arr)

    juxt_arr = imop.juxtapose(arr, 3, axis=1)
    img.display(juxt_arr)

    mos_arr = imop.mosaic(arr, (2, 3))
    print(mos_arr.shape)
    img.display(mos_arr)

    myarr = np.array([[11, 2, 3, 4, 5, 6, 7, 8, 9], [
                          12, 2, 3, 4, 5, 6, 7, 8, 9],
                      [13, 2, 3, 4, 5, 6, 7, 8, 9], [
                          14, 2, 3, 4, 5, 6, 7, 8, 9],
                      [15, 2, 3, 4, 5, 6, 7, 8, 9]])
    print(imop.thin(myarr, 4, axis=0))
