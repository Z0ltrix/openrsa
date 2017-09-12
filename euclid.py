# -*- coding: utf-8 -*-

class Euclid:
    def gcd(self, a, b):
        while (b != 0):
            (a, b) = (b, a % b)
        return abs(a)

    def extendedGcd(self, a, b):
        u, v, s, t = 1, 0, 0, 1
        oa, ob = a, b
        while b > 0:
            q = a // b
            a, b = b, a - q * b
            u, s = s, u - q * s
            v, t = t, v - q * t
        if (u < 0): u += ob
        if (v < 0): v += oa
        return a, u, v
