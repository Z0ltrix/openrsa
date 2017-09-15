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


import random

from euclid import Euclid
import key
import prime


class SimpleRsa:
    def __init__(self):
        pass

    def _calculateModulo(self, p, q):
        modulo = p * q
        return modulo

    def _calculatePhi(self, p, q):
        phi = (p - 1) * (q - 1)
        return phi

    def _calculateEncipherExponent(self, phi):
        while True:
            encipherExponent = random.SystemRandom().randint(1, phi)
            if (Euclid.algorithm(encipherExponent, phi) == 1):
                break
        return encipherExponent

    def _calculateDecipherExponent(self, phi, encipherExponent):
        gcd, u, decipherExponent = Euclid.extended_algorithm(phi, encipherExponent)
        if decipherExponent < 0:
            decipherExponent += phi
        else:
            pass
        return decipherExponent

    def _checkModulo(self, modulo, bits):
        if (modulo.bit_length() == bits):
            return True
        else:
            return False

    def generateKeyPair(self, bits=2048):
        p = 0
        q = 0
        pBits = bits // 2
        qBits = bits // 2
        change = 0
        while True:
            if (p == 0) or (change == 1):
                p = prime.Prime(pBits)
            if (q == 0) or (change == 0):
                q = prime.Prime(qBits)
            modulo = self._calculateModulo(p, q)
            if self._checkModulo(modulo, bits):
                break
            else:
                if (change == 0):
                    change = 1
                else:
                    change = 0
                continue
        phi = self._calculatePhi(p, q)
        encipherExponent = self._calculateEncipherExponent(phi)
        decipherExponent = self._calculateDecipherExponent(phi, encipherExponent)
        privateKey = key.PrivateKey(modulo, decipherExponent)
        publicKey = key.PublicKey(modulo, encipherExponent)
        return (privateKey, publicKey)

    def encipher(self, data, encipherExponent, modulo):
        return pow(data, encipherExponent, modulo)

    def decipher(self, data, decipherExponent, modulo):
        return pow(data, decipherExponent, modulo)

    def sign(self, data, decipherExponent, modulo):
        return pow(data, decipherExponent, modulo)

    def verify(self, data, encipherExponent, modulo):
        return pow(data, encipherExponent, modulo)
