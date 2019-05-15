#!/usr/bin/env python
# -*- coding: utf-8 -*-
while True:
    try:
        n = int(input())
        s = input()
        a = []

        if s == '':
            print(0)
        i = 0
        while True:
            if i >= n or i + 1 >= n:
                break
            if s[i] != s[i + 1]:
                a.append(s[i:i + 2])
                i += 2
            else:
                i += 1

        r = ''.join(a)
        print(len(s) - len(r))
        print(r)
    except:
        break
