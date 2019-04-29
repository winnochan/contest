#!/usr/bin/evn python
# -*- coding: utf-8 -*-
while True:
    try:
        n = int(input())

        s = list(map(int, list(input())))

        f = [0]
        f.extend(list(map(int, input().strip().split())))

        l, r = 0, len(s)
        for i in range(len(s)):
            n = s[i]
            if n < f[n]:
                l = i
                break

        for i in range(l, len(s)):
            n = s[i]
            if n > f[n]:
                r = i
                break

        for i in range(l, r):
            s[i] = f[s[i]]

        print(''.join(map(str, s)))

    except:
        break
