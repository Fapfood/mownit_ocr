import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure

from deskewer import deskewer
from letter_cutter import LABELS
from letter_divider import divide, SPACE


def analise(file_name):
    img = ndimage.imread(file_name, flatten=True)
    pat = ndimage.imread('resources/arial/[B].png', flatten=True)

    img = 255 - img
    img = np.r_[np.zeros((5, img.shape[1])), img, np.zeros((5, img.shape[1]))]
    img = np.c_[np.zeros((img.shape[0], 5)), img, np.zeros((img.shape[0], 5))]

    pat = 255 - pat

    fpat = np.fft.fft2(np.rot90(pat, 2), img.shape)
    fimg = np.fft.fft2(img)
    m = np.multiply(fimg, fpat)
    corr = np.fft.ifft2(m)
    corr = np.abs(corr)
    corr = corr.astype('float')
    corr[corr < 0.9 * np.amax(corr)] = 0

    plt.imshow(corr)
    plt.show()

    img = ndimage.imread(file_name)
    for x in range(len(img)):
        for y in range(len(img[0])):
            if corr[x, y]:
                img[x, y, 0] = 255
                img[x, y, 1] = 0
                img[x, y, 2] = 0

    plt.imshow(img)
    plt.show()

    label = measure.label(corr, background=0)
    props = measure.regionprops(label)
    print(len(props))


def analise2(file_name, font):
    rotated = deskewer(file_name)
    img = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
    text = divide(img, True)

    recognized = ''
    for line in text:
        for letter in line:
            if letter == SPACE:
                recognized += ' '
            else:
                letter = 255 - letter
                find_letter = None
                max_val = 0
                for pattern in LABELS:
                    pat = ndimage.imread('resources/{}/[{}].png'.format(font, pattern))

                    factor = min(letter.shape[0] / pat.shape[0], letter.shape[1] / pat.shape[1])
                    resize = (factor, factor)
                    scale_pat = ndimage.interpolation.zoom(pat, resize)

                    scale_pat = 255 - scale_pat

                    fpat = np.fft.fft2(np.rot90(scale_pat, 2), letter.shape)
                    fimg = np.fft.fft2(letter)
                    m = np.multiply(fimg, fpat)
                    corr = np.fft.ifft2(m)
                    corr = np.abs(corr)
                    corr = corr.astype('float')

                    if max_val < corr.flatten()[corr.size - 1]:
                        max_val = corr.flatten()[corr.size - 1]
                        find_letter = pattern

                recognized += find_letter
        recognized += '\n'
    return recognized
