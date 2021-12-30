import cv2 as cv
import numpy as np
import utils


class VConvolutionFilter(object):
    """ A filter that applies a convolution to V (or all of BGR). """
    def __init__(self, kernel):
        self._kernel = kernel
    
    def apply(self, src, dst):
        """ Apply the filter with a BGR or gray source/destination."""
        cv.filter2D(src, -1, self._kernel, dst)


class SharpenFilter(VConvolutionFilter):
    """ A sharpen filter with a 1-pixel radius."""
    def __init__(self):
        kernel = np.array([[-1, -1, -1],
                           [-1, 9, -1],
                           [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)


class FindEdgesFilter(VConvolutionFilter):
    """ An edge-finding filter with a 1-pixel radius."""
    def __init__(self):
        kernel = np.array([[-1, -1, -1],
                           [-1, 8, -1],
                           [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)


class BlurFilter(VConvolutionFilter):
    """A blur filter with a 2-pixel radius."""
    def __init__(self):
        kernel = numpy.array([[0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04]])
        VConvolutionFilter.__init__(self, kernel)


class EmbossFilter(VConvolutionFilter):
    """An emboss filter with 1-pixel radius."""
    def __init__(self):
        kernel = np.array([[-2, -1, 0],
                           [-1, 1, 1],
                           [0, 1, 2]])
        VconvolutionFilter.__init__(self, kernel)


def strokeEdges(src, dst, blurKsize=7, edgeKsize=5):
    if blurKsize >= 3:
        blurredSrc = cv.medianBlur(src, blurKsize)
        graySrc = cv.cvtColor(blurredSrc, cv.COLOR_BGR2GRAY)
    else:
        graySrc = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.Laplacian(graySrc, cv.CV_8U, graySrc, ksize=edgeKsize)
    normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc)
    channels = cv.split(src)
    for channel in channels:
        channel[:] = channel * normalizedInverseAlpha
    cv.merge(channels, dst)
