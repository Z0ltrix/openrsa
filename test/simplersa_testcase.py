# -*- coding: utf-8 -*-
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
