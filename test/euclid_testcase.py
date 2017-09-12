# -*- coding: utf-8 -*-
import unittest

from euclid import Euclid


class EuclidTestCase(unittest.TestCase):
    def setUp(self):
        self.testobject = Euclid()
        self.gcd_divisor_a = 1268542
        self.gcd_divisor_b = 10815354
        self.gcd = 22

    def tearDown(self):
        self.testobject = None
        self.gcd_divisor_a = None
        self.gcd_divisor_b = None
        self.gcd = None

    def test_gcd(self):
        self.assertTrue(self.testobject.gcd(self.gcd_divisor_a, self.gcd_divisor_b) == 22,
                        "Method gcd of class Euclid is not working correktly")

    def test_extended_gcd(self):
        pass
