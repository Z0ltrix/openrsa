# -*- coding: utf-8 -*-

class Jacobi:

    def symbol(self, a, b):
        result = 1
        while (a != 0):
            while ((a % 2) == 0):
                a = a // 2
                if ((b == (3 % 8)) or (b == (5 % 8))):
                    result = -result
            (a, b) = (b, a)
            if ((a == (3 % 4)) or (b == (3 % 4))):
                result = -result
            a = a % b
        if (b == 1):
            return result
        return 0
