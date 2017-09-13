# -*- coding: utf-8 -*-
import unittest

from solovaystrassen import SolovayStrassen


class SolovayStrassenTestCase(unittest.TestCase):
    def setUp(self):
        self.a1 = 17
        self.a2 = 29
        self.a3 = 23
        self.maybe = 91

    def tearDown(self):
        del self.a1
        del self.a2
        del self.a3
        del self.maybe

    def test_composition(self):
        self.assertTrue(not SolovayStrassen.is_composite(self.a1, self.maybe),
                        "SolovayStrassen detects a composition, but it could be prime")
        self.assertTrue(not SolovayStrassen.is_composite(self.a2, self.maybe),
                        "SolovayStrassen detects a composition, but it could be prime")
        self.assertTrue(SolovayStrassen.is_composite(self.a3, self.maybe),
                        "SolovayStrassen detects no composition, but it is one")
