# -*- coding: utf-8 -*-


class Key:
    def __init__(self, modulo, exponent):
        self._modulo = modulo
        self._exponent = exponent

    def get_bits(self):
        return self._modulo.bit_length()

    def get_modulo(self):
        return self._modulo

    def get_exponent(self):
        return self._exponent

    @staticmethod
    def is_public():
        return False

    @staticmethod
    def is_private():
        return False


class PrivateKey(Key):
    def __init__(self, modulo, decipher_exponent):
        Key.__init__(self, modulo, decipher_exponent)

    def get_decipher_exponent(self):
        return self.get_exponent()

    @staticmethod
    def is_private():
        return True


class PublicKey(Key):
    def __init__(self, modulo, encipher_exponent):
        Key.__init__(self, modulo, encipher_exponent)
        self.__isPublic = True

    def get_encipher_exponent(self):
        return self.get_exponent()

    @staticmethod
    def is_public():
        return True
