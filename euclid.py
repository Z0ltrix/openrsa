# -*- coding: utf-8 -*-


class Euclid:
    """
    A class to compute the Euclidean algorithm and extended Euclidean algorithm.
    """

    def __init__(self):
        """
        The constructor of this class does nothing
        """
        pass

    @staticmethod
    def algorithm(a, b):
        """
        the Euclidean algorithm is an efficient method for computing the greatest common divisor (GCD) of two numbers,
        the largest number that divides both of them without leaving a remainder.

        :param self: instance of the class
        :param a: first divisor
        :param b: second divisor
        :return: greatest common divisor
        :rtype: int
        """
        while b != 0:
            (a, b) = (b, a % b)
        return abs(a)

    @staticmethod
    def extended_algorithm(a, b):
        """
         The extended Euclidean algorithm is an extension to the Euclidean algorithm, in addition to the
         greatest common divisor of integers a and b, also the coefficients of Bézout's identity,
         which are integers u and v such that a * u + b * v = gcd ( a , b )

        :param self: instance of the class
        :param a: first divisor
        :param b: second divisor
        :return: greatest common divisor and the coefficients of Bézout's identity u and v
        :rtype: int, int, int
        """
        u, v, s, t = 1, 0, 0, 1
        while b > 0:
            q = a // b
            a, b = b, a - q * b
            u, s = s, u - q * s
            v, t = t, v - q * t
        return a, u, v
