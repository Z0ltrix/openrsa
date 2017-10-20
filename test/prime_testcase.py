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

from prime import Prime


class PrimeTestCase(unittest.TestCase):
    def setUp(self):
        self.bits = 128
        self.prime = Prime(self.bits)
        self.value = 25

    def tearDown(self):
        del self.bits
        del self.prime

    def test_bits(self):
        self.assertTrue(self.prime.value.bit_length() == self.bits, "Wrong number of bits")

    def test_add(self):
        self.assertTrue(self.prime + self.value == self.prime.value + self.value, "Wrong addition")

    def test_sub(self):
        self.assertTrue(self.prime - self.value == self.prime.value - self.value, "Wrong subtraction")

    def test_mul(self):
        self.assertTrue(self.prime * self.value == self.prime.value * self.value, "Wrong multiplication")

    def test_truediv(self):
        self.assertTrue(self.prime / self.value == self.prime.value / self.value, "Wrong float division")

    def test_floordiv(self):
        self.assertTrue(self.prime // self.value == self.prime.value // self.value, "Wrong integer division")

    def test_security(self):
        self.assertTrue(Prime.security() == 100.0, "Security is not 100 %")
