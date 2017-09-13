# -*- coding: utf-8 -*-

import random

import solovaystrassen


class Prime:
    __SOLOVAYSTRASSENROUNDS = 100

    def __init__(self, bits):
        self.__solovayStrassen = solovaystrassen.SolovayStrassen()
        while True:
            prime = random.SystemRandom().getrandbits(bits)
            prime |= 1
            if self.__isPrimality(prime): break
        self.__value = prime

    def __del__(self):
        del self.__value

    def __eq__(self, b):
        if isinstance(b, Prime):
            if self.__value == b.__value:
                return True
            else:
                return False
        else:
            if self.__value == b:
                return True
            else:
                return False

    def __add_(self, b):
        if isinstance(b, Prime):
            return (self.__value + b.__value)
        else:
            return (self.__value + b)

    def __sub__(self, b):
        if isinstance(b, Prime):
            return (self.__value - b.__value)
        else:
            return (self.__value - b)

    def __mul__(self, b):
        if isinstance(b, Prime):
            return (self.__value * b.__value)
        else:
            return (self.__value * b)

    def __div__(self, b):
        if isinstance(b, Prime):
            return (self.__value / b.__value)
        else:
            return (self.__value / b)

    def getValue(self):
        return self.__value

    def __isPrimality(self, maybe):
        for _ in range(self.__SOLOVAYSTRASSENROUNDS):
            x = random.SystemRandom().randint(1, maybe)
            if self.__solovayStrassen.is_composite(x, maybe):
                return False
        return True
