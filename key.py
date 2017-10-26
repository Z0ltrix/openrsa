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
from codecs import StreamRecoder, getencoder, getdecoder, getreader, getwriter
from io import BytesIO, StringIO
from itertools import repeat
from multiprocessing import Pool, cpu_count
from sys import byteorder


class Key(object):
    """
    A Base Class for the Private- and Public-Key
    """

    _FILLER = '#'
    _PACKAGE_WIDTH = 100
    _LINE_SEPARATOR = '\n'
    _EMPTY_SEPARATOR = ''
    _EMPTY_UTF32_BYTE = b'\x00\x00\x00\x00'

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
        del buffer, input_stream
        # create a pool to compute the modular exponentiation in parallel processors
        worker = Pool(cpu_count())
        # compute the modular exponentiation parallel
        output_integers = worker.map(self._modular_exponentiation, input_integers)
        # clean memory
        del input_integers, worker
        # write the calculated integer values into an output stream
        for output_integer in output_integers:
            # save the output integers as bytes, trim empty UTF-32 formatted bytes and write them to the output stream
            output_stream.write(self._trim_empty_utf32bytes(output_integer.to_bytes(buffer_length, byteorder)))
        # clean memory
        del buffer_length
        # return the whole stream as bytes
        return output_stream.getvalue()

    @staticmethod
    def _utf8str2utf32bytes(utf8str):
        """
        Change the format of a given UTF-8 string into UTF-32 with a fix length of bytes.

        :param utf8str: UTF-8 string.
        :return: UTF-32 string.
        :rtype: string
        """
        return StreamRecoder(stream=BytesIO(utf8str.encode(encoding='utf8')),
                             encode=getencoder('utf32'),
                             decode=getdecoder('utf8'),
                             Reader=getreader('utf8'),
                             Writer=getwriter('utf32')).read()

    @staticmethod
    def _utf32bytes2utf8str(utf32bytes):
        """
        Change the format of a given UTF-32 string with a fix length of bytes into an UTF-8 string
        with variable length of bytes.

        :param utf32bytes: UTF-32 string.
        :return: UTF-8 string.
        :rtype: string
        """
        return StreamRecoder(stream=BytesIO(utf32bytes),
                             encode=getencoder('utf8'),
                             decode=getdecoder('utf32'),
                             Reader=getreader('utf32'),
                             Writer=getwriter('utf8')).read().decode(encoding='utf8')

    def _pack(self, content, title='OPEN RSA DATA',
              description='build with OpenRSA - a free and simple pure python implementation'):
        """
        Packs the content into an human readable format.

        :param content: Hex representation of an UTF-32 string.
        :return: Human readable format for the content.
        :rtype: string
        """
        # calculate configured length of the fillers
        filler_length = (self._PACKAGE_WIDTH - len(title)) // 2
        input_stream = StringIO(content)
        # clean memory
        del content
        output_stream = StringIO()
        # write header line
        output_stream.write(self._EMPTY_SEPARATOR.join(repeat(self._FILLER, filler_length))
                            + title
                            + self._EMPTY_SEPARATOR.join(repeat(self._FILLER, filler_length))
                            + self._LINE_SEPARATOR)
        # write description
        output_stream.write(description + self._LINE_SEPARATOR)
        # clean memory
        del description, title, filler_length
        # split content into lines
        while True:
            # read input lines
            line = input_stream.read(self._PACKAGE_WIDTH)
            # check if something could be read
            if len(line) > 0:
                # write the line into the output stream
                output_stream.write(line + self._LINE_SEPARATOR)
            else:
                # clean memory
                del line, input_stream
                break
        # write footer line
        output_stream.write(self._EMPTY_SEPARATOR.join(repeat(self._FILLER, self._PACKAGE_WIDTH)))
        # return the output stream as a single string
        return output_stream.getvalue()

    def _unpack(self, packed):
        """
        Unpacks the content from an human readable format, into a raw hex representation.

        :param packed: Human readable format for the content.
        :return: Hex representation of an UTF-32 string.
        :rtype: string
        """
        # split the packed content into lines
        content = packed.splitlines()
        # remove header
        del content[0]
        # remove description
        del content[0]
        # remove footer
        del content[len(content) - 1]
        # join and return the remaining lines without a separator
        return self._EMPTY_SEPARATOR.join(content)

    def _trim_empty_utf32bytes(self, utf32bytes):
        """
        Usual trim function for UTF-32 bytes.

        :param utf32bytes: UTF-32 bytes.
        :return: Trimmed UTF-32 bytes.
        :rtype: bytes
        """
        input_stream = BytesIO(utf32bytes)
        # clean memory
        del utf32bytes
        output_stream = BytesIO()
        buffer = bytearray(32 // 8)
        while input_stream.readinto(buffer) > 1:
            if buffer != self._EMPTY_UTF32_BYTE:
                output_stream.write(buffer)
        # clean memory
        del buffer, input_stream
        return output_stream.getvalue()
