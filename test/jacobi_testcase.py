# -*- coding: utf-8 -*-
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
