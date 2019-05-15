#!/usr/bin/evn python
# -*- coding: utf-8 -*-
'''
gcd(a + k, b + k) = gcd(b - a, a + k) =

(a + k) * (b + k) / gcd(a + k, b + k)

(a + b) * k + a * b + k ** 2 / ()
'''


def gcd(a, b):
    mi, ma = min(a, b), max(a, b)
    if ma % mi == 0:
        return mi

    return gcd(mi, ma % mi)


# print(gcd(40, 45))

while True:
    try:
        a, b = map(int, input().strip().split())

        m = a * b // gcd(a, b)

        k = 0
        # print(k, m, gcd(a, b))
        for i in range(1, min(min(a, b), abs(a - b))):
            g = gcd(a + i, b + i)
            n = (a + i) * (b + i) // g
            if n < m:
                m = n
                k = i
                # if min(a + i, b + i)
            # print(i, n, gcd(a + i, b + i))

        print(k)
        # print(gcd(a + k, b + k), (a + k) * (b + k) // gcd(a + k, b + k))

    except:
        break
