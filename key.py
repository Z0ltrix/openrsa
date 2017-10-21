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


class Key(object):
    """
    A Base Class for the Private- and Public-Key
    """

    def __init__(self, modulo, exponent):
        """
        Creates the keystore

        :param modulo: the modulo of the key
        :param exponent: either the encipher or the decipher exponent
        """
        self._modulo = modulo
        self._exponent = exponent

    @property
    def bit_length(self):
        """
        Returns the length of the key in bit

        :return: Length of the key in bit
        :rtype: int
        """
        return self._modulo.bit_length()

    @staticmethod
    def is_public():
        """
        Implements the base method for the indicator of public key.
        Returns always False

        :return: False
        :rtype: bool
        """
        return False

    @staticmethod
    def is_private():
        """
        Implements the base method for the indicator of private key.
        Returns always False.

        :return: False
        :rtype: bool
        """
        return False

    @property
    def exponent(self):
        """
        Get the exponent of the key.

        :return: Exponent of the key.
        :rtype: int
        """
        return self._exponent

    @property
    def modulo(self):
        """
        Get the modulo of the key.

        :return: Modulo of the key.
        :rtype: int
        """
        return self._modulo

    def modular_exponentiation(self, data):
        """
        The operation of modular exponentiation calculates the remainder when an integer data (the base)
        raised to the power of the exponent, divided by a positive integer modulo.

        :param data: Data to process the modular exponentiation.
        :return: The result of the modular exponentiation.
        :rtype: int
        """
        return pow(data, self._exponent, self._modulo)
