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

from multiprocessing import Pool
from multiprocessing import cpu_count
from random import SystemRandom

from euclid import Euclid
from euler import Euler
from key import PrivateKey, PublicKey
from prime import Prime


class OpenRsa:
    def __init__(self):
        pass

    @staticmethod
    def _calculate_modulo(p, q):
        return p * q

    @staticmethod
    def _calculate_encipher_exponent(phi):
        encipher_exponent = 0
        while Euclid.algorithm(encipher_exponent, phi) != 1:
            encipher_exponent = SystemRandom().randint(1, phi)
        return encipher_exponent

    @staticmethod
    def _calculate_decipher_exponent(phi, encipher_exponent):
        gcd, u, decipher_exponent = Euclid.extended_algorithm(phi, encipher_exponent)
        if decipher_exponent < 0:
            decipher_exponent += phi
        else:
            pass
        return decipher_exponent

    @staticmethod
    def generate_key_pair(bit_length=2048):
        worker = Pool(min(2, cpu_count()))
        bits = [(bit_length // 2), (bit_length // 2)]
        p = 0
        q = 0
        modulo = 0
        while modulo.bit_length() != bit_length:
            primes = worker.map(Prime, bits)
            p = primes[0]
            q = primes[1]
            modulo = OpenRsa._calculate_modulo(p, q)
        phi = Euler.phi(p, q)
        encipher_exponent = OpenRsa._calculate_encipher_exponent(phi)
        decipher_exponent = OpenRsa._calculate_decipher_exponent(phi, encipher_exponent)
        private_key = PrivateKey(modulo, decipher_exponent)
        public_key = PublicKey(modulo, encipher_exponent)
        return private_key, public_key

    @staticmethod
    def encipher_int(data, encipher_exponent, modulo):
        return pow(data, encipher_exponent, modulo)

    @staticmethod
    def decipher_int(data, decipher_exponent, modulo):
        return pow(data, decipher_exponent, modulo)

    @staticmethod
    def sign_int(data, decipher_exponent, modulo):
        return pow(data, decipher_exponent, modulo)

    @staticmethod
    def verify_int(data, encipher_exponent, modulo):
        return pow(data, encipher_exponent, modulo)


if __name__ == "__main__":
    private_key, public_key = OpenRsa.generate_key_pair(2048)
    print("private key: " + str(private_key))
    print("public key: " + str(public_key))
