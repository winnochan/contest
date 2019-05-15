#!/usr/bin/env python
# -*- coding: utf-8 -*-
while True:
    try:
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        k = 1
        c = 0
        for i in a:
            if i < k:
                continue
            c += 1
            k += 1
        print(c)
    except:
        break
