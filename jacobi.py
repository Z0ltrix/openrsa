# -*- coding: utf-8 -*-


class Jacobi:
    """
    A Class to compute the Jacobi Symbol
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
    def symbol(a, n):
        """
        The Jacobi Symbol is a generalization of the Legendre symbol.
        Its main use is in computational number theory, especially primality testing and integer factorization.

        :param a: any number
        :param n: any positive odd number > 1
        :return:
            0 if n is divider of a
            1 if a is square rest of modulo n
           -1 if a is no square rest of modulo n
        """
        result = 1
        while a != 0:
            while a % 2 == 0:
                a = a // 2
                if (n == (3 % 8)) or (n == (5 % 8)):
                    result = -result
            (a, n) = (n, a)
            if (a == (3 % 4)) or (n == (3 % 4)):
                result = -result
            a = a % n
        if n == 1:
            return result
        return 0
