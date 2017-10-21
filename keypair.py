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
from multiprocessing import Pool, cpu_count
from random import SystemRandom

from euclid import Euclid
from euler import Euler
from prime import Prime
from privatekey import PrivateKey
from publickey import PublicKey


class KeyPair:
    """
    Class to store the private and public key in one object.
    """

    def __init__(self, bit_length=2048):
        """
        Creates the key pair with a given bit length.
        Works with 2 seperate processes if possible.

        :param bit_length: the lenght of the modulo in bits
        """
        worker = Pool(min(2, cpu_count()))
        bits = [(bit_length // 2), (bit_length // 2)]
        p = 0
        q = 0
        modulo = 0
        while modulo.bit_length() != bit_length:
            primes = worker.map(Prime, bits)
            p = primes[0]
            q = primes[1]
            modulo = p * q
        phi = Euler.phi(p, q)
        encipher_exponent = SystemRandom().randint(1, phi)
        while Euclid.algorithm(encipher_exponent, phi) != 1:
            encipher_exponent = SystemRandom().randint(1, phi)
        gcd, u, decipher_exponent = Euclid.extended_algorithm(phi, encipher_exponent)
        if decipher_exponent < 0:
            decipher_exponent += phi
        self._private_key = PrivateKey(modulo, decipher_exponent)
        self._public_key = PublicKey(modulo, encipher_exponent)

    def __del__(self):
        pass

    def _get_private_key(self):
        return self._private_key

    def _get_public_key(self):
        return self._public_key

    private_key = property(_get_private_key)
    public_key = property(_get_public_key)
