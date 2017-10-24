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
from utils import utf8str2utf32bytes, utf32bytes2utf8str, pack, unpack


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

    def decipher(self, hex_utf32bytes):
        """
        Deciphers the given hex string of UTF-32 formatted bytes.

        :param hex_utf32bytes: The enciphered data as hex string of UTF-32 formatted bytes
        :return: The deciphered Data as UTF-8 string
        :rtype: string
        """
        return utf32bytes2utf8str(self._stream_modular_exponentiation(bytes.fromhex(unpack(hex_utf32bytes))))

    def sign(self, utf8str):
        """
        Sign the given plain text as UTF-8 string and return the signed data as a hex representation of UTF-32 bytes.

        :param utf8str: The plain text as UTF-8 string.
        :return: The signed data as hex representation of UTF-32 bytes.
        :rtype: string
        """
        return pack(self._stream_modular_exponentiation(utf8str2utf32bytes(utf8str)).hex())
