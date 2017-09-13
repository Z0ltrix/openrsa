# -*- coding: utf-8 -*-

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
