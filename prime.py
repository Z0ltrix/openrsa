# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2017 Christian Pfarr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import random

from solovaystrassen import SolovayStrassen


class Prime(object):
    """
    Class for working with prime numbers
    """

    SOLOVAY_STRASSEN_ROUNDS = 54

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

    def __floordiv__(self, other):
        """
        Divides a potential prime number with integer division.

        :param other: the potential prime number
        :return: the result
        """
        if isinstance(other, Prime):
            return self._value // other._value
        else:
            return self._value // other

    def __truediv__(self, other):
        """
        Divides a potential prime number with true division

        :param other: the potential prime number
        :return: the result
        """
        if isinstance(other, Prime):
            return self._value / other._value
        else:
            return self._value / other

    @property
    def value(self):
        """
        Returns the value of the prime number.

        :return: The value.
        :rtype: int
        """
        return self._value

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

    @classmethod
    def security(cls):
        """
        Calculates the security level in percent.
        To change the security level, just change the static value SOLOVAY_STRASSEN_ROUNDS.

        :return: The security level in percent.
        :rtype: float
        """
        return (100 * (1 - (1 / (pow(2, cls.SOLOVAY_STRASSEN_ROUNDS)))))
