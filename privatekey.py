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


class PrivateKey(Key):
    """
    A class for storing the private key.
    """

    def __init__(self, modulo, decipher_exponent):
        """
        Creates the private key.
        Just calls the base-class Key.__init__(...) with the given parameters.

        :param modulo: the modulo of the private key
        :param decipher_exponent: the decipher_exponent of the private key
        """
        Key.__init__(self, modulo, decipher_exponent)

    @property
    def decipher_exponent(self):
        """
        Returns the decipher exponent of the private key.

        :return: decipher exponent of the private key
        :rtype: int
        """
        return self._exponent

    @staticmethod
    def is_private():
        """
        Indicator of private key.
        Overrides base method of Key.
        Returns always True, because this is a private key.

        :return: True
        :rtype: bool
        """
        return True

    def decipher_int(self, data):
        """
        Decipher an integer value.

        :param data: Data to be deciphered.
        :return: The deciphered data.
        :rtype: int
        """
        return self.modular_exponentiation(data)

    def sign_int(self, data):
        """
        Sign an integer value.

        :param data: Data to be signed.
        :return: The signed data
        :rtype: int
        """
        return self.modular_exponentiation(data)
