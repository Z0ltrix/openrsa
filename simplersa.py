# -*- coding: utf-8 -*-

import euclid
import prime
import key
import random


class SimpleRsa:
    def __init__(self):
        self.__euclid = euclid.Euclid()

    def __calculateModulo(self, p, q):
        modulo = p * q
        return modulo

    def __calculatePhi(self, p, q):
        phi = (p - 1) * (q - 1)
        return phi

    def __calculateEncipherExponent(self, phi):
        while True:
            encipherExponent = random.SystemRandom().randint(1, phi)
            if (self.__euclid.gcd(encipherExponent, phi) == 1):
                break
        return encipherExponent

    def __calculateDecipherExponent(self, phi, encipherExponent):
        gcd, k, decipherExponent = self.__euclid.extendedGcd(phi, encipherExponent)
        return decipherExponent

    def __checkModulo(self, modulo):
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
            modulo = self.__calculateModulo(p, q)
            if self.__checkModulo(modulo):
                break
            else:
                if (change == 0):
                    change = 1
                else:
                    change = 0
                continue
        phi = self.__calculatePhi(p, q)
        encipherExponent = self.__calculateEncipherExponent(phi)
        decipherExponent = self.__calculateDecipherExponent(phi, encipherExponent)
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


# TESTS
rsa = SimpleRsa()
data = int(input("Data      : "))
while True:
    bits = int(input("Bits      : "))
    privateKey, publicKey = rsa.generateKeyPair(bits)
    print("encipherExponent : ", publicKey.getEncipherExponent())
    print("decipherExponent : ", privateKey.getDecipherExponent())
    encipheredData = rsa.encipher(data, publicKey.getEncipherExponent(), publicKey.getModulo())
    print("encipheredData   : ", encipheredData)
    decipheredData = rsa.decipher(encipheredData, privateKey.getDecipherExponent(), privateKey.getModulo())
    print("decipheredData   : ", decipheredData)
    if input("nochmal? ") == "nein": break
