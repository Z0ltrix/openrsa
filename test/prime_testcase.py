# -*- coding: utf-8 -*-
import unittest

from prime import Prime


class PrimeTestCase(unittest.TestCase):
    def setUp(self):
        self.bits = 256
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

    def test_div(self):
        self.assertTrue(self.prime / self.value == self.prime.value / self.value, "Wrong division")
