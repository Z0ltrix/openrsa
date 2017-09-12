# -*- coding: utf-8 -*-


class Euclid:
    """
    A class to compute the Euclidean algorithm and extendet Euclidean algorithm.
    """

    def __init__(self):
        """
        The constructor of this class does nothing
        """
        pass

    def gcd(self, a, b):
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

    def extended_gcd(self, a, b):
        """
         The extended Euclidean algorithm is an extension to the Euclidean algorithm, in addition to the
         greatest common divisor of integers a and b, also the coefficients of Bézout's identity,
         which are integers x and y such that a x + b y = gcd ( a , b )

        :param self: instance of the class
        :param a: first divisor
        :param b: second divisor
        :return: greatest common divisor and the coefficients of Bézout's identity
        :rtype: int
        """
        u, v, s, t = 1, 0, 0, 1
        oa, ob = a, b
        while b > 0:
            q = a // b
            a, b = b, a - q * b
            u, s = s, u - q * s
            v, t = t, v - q * t
        if u < 0: u += ob
        if v < 0: v += oa
        return a, u, v
