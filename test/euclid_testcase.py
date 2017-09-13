# -*- coding: utf-8 -*-
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
