#!/usr/bin/env python

import numpy as np

import matplotlib.pyplot as plt


class ImageProcessor:
    IND = 1

    @staticmethod
    def load(path):
        img = plt.imread(path)
        print('Loading image of dimensions {} x {}'.format(
            img.shape[0], img.shape[1]))
        return img
    @staticmethod
    def display(array):
        plt.figure(ImageProcessor.IND)
        plt.imshow(array)
        plt.show()
        ImageProcessor.IND += 1


if __name__ == '__main__':
    img = ImageProcessor()
    arr = img.load('../resources/42AI.png')
    print(arr)
    img.display(arr)
