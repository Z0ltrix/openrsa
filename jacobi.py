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


class Jacobi(object):
    """
    A Class to compute the Jacobi Symbol
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
    def symbol(a, n):
        """
        The Jacobi Symbol is a generalization of the Legendre symbol.
        Its main use is in computational number theory, especially primality testing and integer factorization.

        :param a: any number
        :param n: any positive odd number > 1
        :return:
            0 if n is divider of a
            1 if a is square rest of modulo n
           -1 if a is no square rest of modulo n
        """
        result = 1
        while a != 0:
            while a % 2 == 0:
                a = a // 2
                if (n == (3 % 8)) or (n == (5 % 8)):
                    result = -result
            (a, n) = (n, a)
            if (a == (3 % 4)) or (n == (3 % 4)):
                result = -result
            a = a % n
        if n == 1:
            return result
        return 0
