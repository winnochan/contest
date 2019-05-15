#!/usr/bin/evn python
# -*- coding: utf-8 -*-
while True:
    try:
        x = int(input())

        s = '{0:b}'.format(x)

        t, n, p = 0, [], 1
        if s.count('1') != len(s):
            while True:
                i = s.find('0')
                if i < 0:
                    break

                t += 1
                if p == 1:
                    ni = int((len(s) - i) * '1', base=2)
                    x ^= ni
                    n.append(len(s) - i)
                    p = 0
                else:
                    x += 1
                    p = 1

                s = '{0:b}'.format(x)

        print(t)
        if len(n) > 0:
            print(' '.join(map(str, n)))

    except:
        break
