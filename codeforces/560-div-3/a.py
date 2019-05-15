#!/usr/bin/env python
# -*- coding: utf-8 -*-
while True:
    try:
        n, x, y = map(int, input().split())

        s = input()
        c = 0
        for i in range(n - x - 1, n):
            if i == n - x - 1:
                if s[i] == '0':
                    c += 1
            elif n - x - 1 < i < n - y - 1:
                if s[i] == '1':
                    c += 1
            elif i == n - y - 1:
                if s[i] == '0':
                    c += 1
            elif i > n - y - 1:
                if s[i] == '1':
                    c += 1

        print(c)
    except:
        break
