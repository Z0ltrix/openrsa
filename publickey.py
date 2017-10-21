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

from key import Key


class PublicKey(Key):
    """
    A class for storing the public key.
    """

    def __init__(self, modulo, encipher_exponent):
        """
        Creates the public key.
        Just calls the base-class Key.__init__(...) with the given parameters.

        :param modulo: the modulo of the public key
        :param encipher_exponent: the encipher exponent of the public key
        """
        Key.__init__(self, modulo, encipher_exponent)

    def _get_encipher_exponent(self):
        """
        Returns the encipher exponent of the public key.

        :return: the encipher exponent of the public key
        :rtype: int
        """
        return self._get_exponent()

    @staticmethod
    def is_public():
        """
        Indicator of public key.
        Overrides base method of Key.
        Returns always True, because this is a public key.

        :return: True
        :rtype: bool
        """
        return True

    encipher_exponent = property(_get_encipher_exponent)

    def encipher_int(self, data):
        """
        Encipher an integer value.

        :param data: Data to be enciphered.
        :return: The enciphered Data.
        :rtype: int
        """
        return self.modular_exponentiation(data)

    def verify_int(self, data):
        """
        Verify an integer value.


        :param data: Data to be verified.
        :return: The verified Data.
        :rtype: int
        """
        return self.modular_exponentiation(data)
