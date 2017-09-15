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

from jacobi import Jacobi


class JacobiTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 5
        self.n_divider = 15
        self.n_square_rest = 11
        self.n_no_square_rest = 17
        self.symbol_divider = 0
        self.symbol_square_rest = 1
        self.symbol_no_square_rest = -1

    def tearDown(self):
        del self.a
        del self.n_divider
        del self.n_square_rest
        del self.n_no_square_rest
        del self.symbol_divider
        del self.symbol_square_rest
        del self.symbol_no_square_rest

    def test_symbol_divider(self):
        self.assertTrue(Jacobi.symbol(self.a, self.n_divider) == self.symbol_divider,
                        "Jacobi Symbol cant test if n is divider of a")

    def test_symbol_square_rest(self):
        self.assertTrue(Jacobi.symbol(self.a, self.n_square_rest) == self.symbol_square_rest,
                        "Jacobi Symbol cant test if a is square rest of modulo n")

    def test_symbol_no_square_rest(self):
        self.assertTrue(Jacobi.symbol(self.a, self.n_no_square_rest) == self.symbol_no_square_rest,
                        "Jacobi Symbol cant test if a is no square rest of modulo n")
