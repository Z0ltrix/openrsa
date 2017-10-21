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

from euclid import Euclid
from jacobi import Jacobi


class SolovayStrassen(object):
    """
    A Class to compute the Solovay–Strassen primality test
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
    def is_composite(a, maybe):
        """
        The Solovay–Strassen primality test is a probabilistic test to determine if a number is
        composite or probably prime.

        :param a: any number
        :param maybe: potential prime
        :return:
            True if maybe is definitely not a prime, because its a composition.
            False if maybe is probably a prime, but not verified.
        """
        g = Euclid.algorithm(a, maybe)
        b = pow(a, maybe >> 1, maybe)
        if g > 1:
            return True
        elif (1 < b) and (b < maybe - 1):
            return True
        elif (b == 1) or (b == maybe - 1):
            j = Jacobi.symbol(a, maybe)
            c = b % maybe
            if j == c:
                return False
            else:
                pass
        return False
