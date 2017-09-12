# -*- coding: utf-8 -*-

class Key:
    def __init__(self, modulo, exponent):
        self.__modulo = modulo
        self.__exponent = exponent

    def getBits(self):
        return self.__modulo.bit_length()

    def getModulo(self):
        return self.__modulo

    def getExponent(self):
        return self.__exponent

    def isPublic(self):
        return False

    def isPrivate(self):
        return False


class PrivateKey(Key):
    def __init__(self, modulo, decipherExponent):
        Key.__init__(self, modulo, decipherExponent)

    def getDecipherExponent(self):
        return self.getExponent()

    def isPrivate(self):
        return True


class PublicKey(Key):
    def __init__(self, modulo, encipherExponent):
        Key.__init__(self, modulo, encipherExponent)
        self.__isPublic = True

    def getEncipherExponent(self):
        return self.getExponent()

    def isPublic(self):
        return True
