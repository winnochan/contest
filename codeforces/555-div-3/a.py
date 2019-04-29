#!/usr/bin/evn python
# -*- coding: utf-8 -*-
while True:
    try:
        n = int(input())
        r = set([])

        while n not in r:
            r.add(n)

            n += 1
            while n % 10 == 0:
                n //= 10

        # print(r)
        print(len(r))

    except:
        break
