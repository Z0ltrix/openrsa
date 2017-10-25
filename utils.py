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
    # calculate configured length of side fillers
    side_length = (OPEN_RSA_DATA_WITH - len(OPEN_RSA_DATA_TITLE)) // 2
    # join the side fillers without separator
    left = "".join(repeat("#", side_length))
    right = "".join(repeat("#", side_length))
    # clean memory
    del side_length
    # join the fillers and the header
    header = left + OPEN_RSA_DATA_TITLE + right
    # clean memory
    del left
    del right
    # join the footer without separator
    footer = "".join(repeat("#", OPEN_RSA_DATA_WITH))
    input_stream = StringIO(content)
    # clean memory
    del content
    output_stream = StringIO()
    # write header line
    output_stream.write(header + "\n")
    # split content into lines
    while True:
        # read input lines
        line = input_stream.read(OPEN_RSA_DATA_WITH)
        # check if something could be read
        if len(line) > 0:
            # write the line into the output stream
            output_stream.write(line + "\n")
        else:
            break
    # write footer line
    output_stream.write(footer)
    # return the output stream as a single string
    return output_stream.getvalue()


def unpack(packed):
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
    # remove footer
    del content[len(content) - 1]
    # join and return the remaining lines without a separator
    return "".join(content)


def trim_empty_utf32bytes(utf32bytes):
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
        if buffer != b'\x00\x00\x00\x00':
            output_stream.write(buffer)
    # clean memory
    del buffer
    del input_stream
    return output_stream.getvalue()
