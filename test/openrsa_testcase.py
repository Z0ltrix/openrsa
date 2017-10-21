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
from unittest import TestCase

from keypair import KeyPair


class OpenRsaTestCase(TestCase):
    def setUp(self):
        self.data = 42
        self.bits = 128
        self.key_pair = KeyPair(self.bits)

    def tearDown(self):
        del self.data
        del self.bits
        del self.key_pair

    def test_decipher(self):
        enciphered_data = self.key_pair.public_key.encipher_int(self.data)
        deciphered_data = self.key_pair.private_key.decipher_int(enciphered_data)
        self.assertTrue(self.data == deciphered_data, "Decryption doesnt work")

    def test_verify(self):
        signed_data = self.key_pair.private_key.sign_int(self.data)
        verified_data = self.key_pair.public_key.verify_int(signed_data)
        self.assertTrue(self.data == verified_data, "Verification doesnt work")
