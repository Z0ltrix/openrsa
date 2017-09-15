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
import unittest

from simplersa import SimpleRsa


class SimpleRsaTestCase(unittest.TestCase):
    def setUp(self):
        self.simple_rsa = SimpleRsa()
        self.data = 42
        self.bits = 128
        self.private_key, self.public_key = self.simple_rsa.generateKeyPair(self.bits)
        self.enciphered_data = self.simple_rsa.encipher(self.data,
                                                        self.public_key.get_encipher_exponent(),
                                                        self.public_key.get_modulo())
        self.deciphered_data = self.simple_rsa.decipher(self.enciphered_data,
                                                        self.private_key.get_decipher_exponent(),
                                                        self.public_key.get_modulo())
        self.signed_data = self.simple_rsa.sign(self.data,
                                                self.private_key.get_decipher_exponent(),
                                                self.private_key.get_modulo())
        self.verified_data = self.simple_rsa.verify(self.signed_data,
                                                    self.public_key.get_encipher_exponent(),
                                                    self.public_key.get_modulo())

    def tearDown(self):
        del self.simple_rsa
        del self.data
        del self.bits
        del self.private_key
        del self.public_key
        del self.enciphered_data
        del self.deciphered_data
        del self.signed_data
        del self.verified_data

    def test_decipher(self):
        self.assertTrue(self.data == self.deciphered_data, "Decryption doesnt work")

    def test_verify(self):
        self.assertTrue(self.data == self.verified_data, "Verification doesnt work")
