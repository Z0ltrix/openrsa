# -*- coding: utf-8 -*-

from euclid import Euclid
from jacobi import Jacobi


class SolovayStrassen:
    """
    A Class to compute the Solovay–Strassen primality test
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
    def is_composite(a, maybe):
        """
        The Solovay–Strassen primality test is a probabilistic test to determine if a number is
        composite or probably prime.

        :param a: any number
        :param maybe: potential prime
        :return:
            True if maybe is definitely not a prime
            False if may is probably a prime
        """
        g = Euclid.algorithm(a, maybe)
        b = pow(a, maybe >> 1, maybe)
        if g > 1:
            return True
        elif (1 < b) and (b < maybe - 1):
            return True
        elif (b == 1) or (b == maybe - 1):
            j = Jacobi.symbol(a, maybe)
            c = b % maybe
            if j == c:
                return False
            else:
                pass
        return False


if __name__ == '__main__':
    a1 = 17
    a2 = 29
    a3 = 23
    maybe = 91
    print(SolovayStrassen.is_composite(a1, maybe))
    print(SolovayStrassen.is_composite(a2, maybe))
    print(SolovayStrassen.is_composite(a3, maybe))
