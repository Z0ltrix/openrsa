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


class Key:
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

    def get_bits(self):
        """
        Returns the length of the key in bit

        :return: length of the key in bit
        :rtype: int
        """
        return self._modulo.bit_length()

    def get_modulo(self):
        """
        Returns the modulo of the key

        :return: modulo of the key
        :rtype: int
        """
        return self._modulo

    def get_exponent(self):
        """
        Returns the exponent of the key

        :return: exponent of the key
        :rtype: int
        """
        return self._exponent

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

    exponent = property(get_exponent)


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

    def get_decipher_exponent(self):
        """
        Returns the decipher exponent of the private key.

        :return: decipher exponent of the private key
        :rtype: int
        """
        return self.get_exponent()

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

    decipher_exponent = property(get_decipher_exponent)


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

    def get_encipher_exponent(self):
        """
        Returns the encipher exponent of the public key.

        :return: the encipher exponent of the public key
        :rtype: int
        """
        return self.get_exponent()

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

    encipher_exponent = property(get_encipher_exponent)
