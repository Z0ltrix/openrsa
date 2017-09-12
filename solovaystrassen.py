# -*- coding: utf-8 -*-

import euclid
import jacobi


class SolovayStrassen:
    def __init__(self):
        self.__euclid = euclid.Euclid()
        self.__jacobi = jacobi.Jacobi()

    def isComposite(self, a, maybe):
        g = self.__euclid.gcd(a, maybe)
        b = pow(a, maybe >> 1, maybe)
        if g > 1:
            return True
        elif (1 < b) and (b < maybe - 1):
            return True
        elif (b == 1) or (b == maybe - 1):
            j = self.__jacobi.symbol(a, maybe)
            c = b % maybe
            if (j == c): return False
        return False
