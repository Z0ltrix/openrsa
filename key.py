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
from io import BytesIO
from multiprocessing import Pool, cpu_count
from sys import byteorder

from utils import trim_empty_utf32bytes


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

    def _modular_exponentiation(self, integer):
        """
        The operation of modular exponentiation calculates the remainder when an integer (the base)
        raised to the power of the exponent, divided by an modulo.

        :param integer: Integer to process the modular exponentiation.
        :return: The result of the modular exponentiation.
        :rtype: int
        """
        return pow(integer, self._exponent, self._modulo)

    def _stream_modular_exponentiation(self, utf32bytes):
        """
        Calculates the operation of modular exponentiation over a stream of UTF-32 formatted bytes.
        Works with a pool of processes by cpu_count().

        :param utf32bytes: UTF-32 formatted input bytes.
        :return: UTF-32 formatted output bytes.
        :rtype: bytes
        """
        # input stream of UTF-32 formatted bytes
        input_stream = BytesIO(utf32bytes)
        # clean memory
        del utf32bytes
        # output stream of UTF-32 formatted bytes
        output_stream = BytesIO()
        # biggest possible buffer size is length of the modulo in bytes
        buffer_length = self.bit_length // 8
        buffer = bytearray(buffer_length)
        input_integers = []
        # read the integer values into an array
        while input_stream.readinto(buffer) > 1:
            input_integers.append(int.from_bytes(buffer, byteorder))
            # clear the buffer after every read
            buffer = bytearray(buffer_length)
        # clean memory
        del buffer
        del input_stream
        # create a pool to compute the modular exponentiation in parallel processors
        worker = Pool(cpu_count())
        # compute the modular exponentiation parallel
        output_integers = worker.map(self._modular_exponentiation, input_integers)
        # clean memory
        del input_integers
        del worker
        # write the calculated integer values into an output stream
        for output_integer in output_integers:
            # save the output integers as bytes, trim empty UTF-32 formatted bytes and write them to the output stream
            output_stream.write(trim_empty_utf32bytes(output_integer.to_bytes(buffer_length, byteorder)))
        # clean memory
        del buffer_length
        # return the whole stream as bytes
        return output_stream.getvalue()
