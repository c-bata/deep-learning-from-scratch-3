import unittest
import numpy as np
from dezero import Variable
import dezero.functions as F
from dezero.utils import check_backward
from dezero import utils


class TestIm2col(unittest.TestCase):
    '''
    def test_forward1(self):
        n, c, h, w = 1, 1, 3, 3
        x = np.arange(n*c*h*w).reshape((n,c,h,w))
        y = F.im2col(x, 3, 3, 0)
        expected = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8]])
        res = np.array_equal(y.data, expected)
        self.assertTrue(res)
    '''

    def test_backward1(self):
        n, c, h, w = 1, 1, 3, 3
        x = np.arange(n * c * h * w).reshape((n, c, h, w))
        # y = F.im2col(x, 3, 3, 0)

        f = lambda x: F.im2col(x, 3, 3, 0)
        self.assertTrue(check_backward(f, x))