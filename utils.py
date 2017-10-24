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

OPEN_RSA_DATA_TITLE = " OpenRSA Data "
OPEN_RSA_DATA_WITH = 100


def utf8str2utf32bytes(utf8str):
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


def utf32bytes2utf8str(utf32bytes):
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


def pack(content):
    """
    Packs the content into an human readable format.

    :param content: Hex representation of an UTF-32 string.
    :return: Human readable format for the content.
    :rtype: string
    """
    side = (OPEN_RSA_DATA_WITH - len(OPEN_RSA_DATA_TITLE)) // 2
    left = "".join(repeat("#", side))
    right = "".join(repeat("#", side))
    header = left + OPEN_RSA_DATA_TITLE + right
    footer = "".join(repeat("#", OPEN_RSA_DATA_WITH))
    input_stream = StringIO(content)
    output_stream = StringIO()
    output_stream.write(header + "\n")
    while True:
        line = input_stream.read(OPEN_RSA_DATA_WITH)
        if len(line) > 0:
            output_stream.write(line + "\n")
        else:
            break
    output_stream.write(footer)
    return output_stream.getvalue()


def unpack(packed):
    """
    Unpacks the content from an human readable format, into a raw hex representation.

    :param packed: Human readable format for the content.
    :return: Hex representation of an UTF-32 string.
    :rtype: string
    """
    content = packed.splitlines()
    content.remove(content[0])
    content.pop()
    return "".join(content)


def trim_empty_utf32bytes(utf32bytes):
    """
    Usual trim function for UTF-32 bytes.

    :param utf32bytes: UTF-32 bytes.
    :return: Trimmed UTF-32 bytes.
    :rtype: bytes
    """
    input_stream = BytesIO(utf32bytes)
    output_stream = BytesIO()
    buffer = bytearray(32 // 8)
    while input_stream.readinto(buffer) > 1:
        if buffer != b'\x00\x00\x00\x00':
            output_stream.write(buffer)
    return output_stream.getvalue()
