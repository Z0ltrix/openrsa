# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2017 Christian Pfarr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


class Euclid(object):
    """
    A class to compute the Euclidean algorithm and extended Euclidean algorithm.
    """

    def __init__(self):
        """
        The constructor of this class does nothing
        """
        pass

    def __del__(self):
        """
        The destructor of this class does nothing
        """
        pass

    @staticmethod
    def algorithm(a, b):
        """
        the Euclidean algorithm is an efficient method for computing the greatest common divisor (GCD) of two numbers,
        the largest number that divides both of them without leaving a remainder.

        :param a: first divisor
        :param b: second divisor
        :return: greatest common divisor
        :rtype: int
        """
        while b != 0:
            (a, b) = (b, a % b)
        return abs(a)

    @staticmethod
    def extended_algorithm(a, b):
        """
         The extended Euclidean algorithm is an extension to the Euclidean algorithm, in addition to the
         greatest common divisor of integers a and b, also the coefficients of Bézout's identity,
         which are integers u and v such that a * u + b * v = gcd ( a , b )

        :param a: first divisor
        :param b: second divisor
        :return: greatest common divisor and the coefficients of Bézout's identity u and v
        :rtype: (int, int, int)
        """
        u, v, s, t = 1, 0, 0, 1
        while b > 0:
            q = a // b
            a, b = b, a - q * b
            u, s = s, u - q * s
            v, t = t, v - q * t
        return a, u, v
