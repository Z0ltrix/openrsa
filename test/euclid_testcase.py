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
import unittest

from euclid import Euclid


class EuclidTestCase(unittest.TestCase):
    def setUp(self):
        self.divisor_a = 180
        self.divisor_b = 235
        self.gcd = 5
        self.coefficient_u = 17
        self.coefficient_v = -13

    def tearDown(self):
        del self.divisor_a
        del self.divisor_b
        del self.gcd
        del self.coefficient_u
        del self.coefficient_v

    def test_gcd(self):
        self.assertTrue(Euclid.algorithm(self.divisor_a, self.divisor_b) == self.gcd,
                        "Method gcd of class Euclid is not giving the expected values back")

    def test_extended_gcd(self):
        self.assertTrue(Euclid.extended_algorithm(self.divisor_a, self.divisor_b) == (
            self.gcd, self.coefficient_u, self.coefficient_v),
                        "Method extended_gcd of class Euclid is not giving the expected values back")

    def test_bezout_identity(self):
        var_gcd, var_coefficient_u, var_coefficient_v = Euclid.extended_algorithm(self.divisor_a, self.divisor_b)
        self.assertTrue(self.divisor_a * var_coefficient_u + self.divisor_b * var_coefficient_v == var_gcd,
                        "Method extended_gcd of class Euclid is not fulfilling Bézout's identity")
