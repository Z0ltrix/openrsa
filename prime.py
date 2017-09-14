# -*- coding: utf-8 -*-

import random

from solovaystrassen import SolovayStrassen


class Prime:
    """
    Class for working with prime numbers
    """

    SOLOVAY_STRASSEN_ROUNDS = 100

    def __init__(self, bits):
        """
        Constructor for prime numbers.
        The Constructor reads a random Number and loops until one is a primality

        :param bits: number of bits the prime number should have
        """
        while True:
            maybe = random.SystemRandom().getrandbits(bits)
            maybe |= 1
            if maybe.bit_length() != bits:
                continue
            if self._is_primality(maybe):
                break
        self._value = maybe

    def __del__(self):
        """
        Destructor for prime numbers.
        Deletes the value.
        """
        del self._value

    def __eq__(self, b):
        """
        Checks if two prime numbers are equal

        :param b: the other prime number
        :return:
            True if the primes are equal
            False if the primes are not equal
        :rtype: bool
        """
        if isinstance(b, Prime):
            if self._value == b._value:
                return True
            else:
                return False
        else:
            if self._value == b:
                return True
            else:
                return False

    def __add__(self, b):
        """
        Adds a potential prime number

        :param b: the potential prime number
        :return: the result
        :rtype: int
        """
        if isinstance(b, Prime):
            return self._value + b._value
        else:
            return self._value + b

    def __sub__(self, b):
        """
        Subtracts a potential prime number

        :param b: the potential prime number
        :return: the result
        :rtype: int
        """
        if isinstance(b, Prime):
            return self._value - b._value
        else:
            return self._value - b

    def __mul__(self, b):
        """
        Multiplicates a potential prime number

        :param b: the potential prime number
        :return: the result
        :rtype: int
        """
        if isinstance(b, Prime):
            return self._value * b._value
        else:
            return self._value * b

    def __truediv__(self, b):
        """
        Divides a potential prime number

        :param b: the potential prime number
        :return: the result
        """
        if isinstance(b, Prime):
            return self._value / b._value
        else:
            return self._value / b

    def _get_value(self):
        """
        Returns the value of the prime number

        :return: The value
        :rtype: int
        """
        return self._value

    value = property(_get_value)

    def _is_primality(self, maybe):
        """
        Checks if the potential prime number is a prime number via Solovay Strassen Test
        with a configured number of rounds.

        :param maybe: The potential prime number.
        :return:
            True if its a prime
            False if its no prime
        """
        for _ in range(self.SOLOVAY_STRASSEN_ROUNDS):
            x = random.SystemRandom().randint(1, maybe)
            if SolovayStrassen.is_composite(x, maybe):
                return False
        return True
