#!/usr/bin/evn python
# -*- coding: utf-8 -*-
while True:
    try:
        n, t = map(int, input().strip().split())
        m, r = -1, 0
        for i in range(n):
            s, d = map(int, input().strip().split())
            if s >= t:
                w = s - t
            else:
                w = ((t - s) // d + 1) * d + s - t if (t - s) % d != 0 else 0
            if m < 0 or w < m:
                m = w
                r = i + 1
            # print(w, r)
        print(r)
    except:
        break
