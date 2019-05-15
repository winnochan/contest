#!/usr/bin/evn python
# -*- coding: utf-8 -*-
while True:
    try:
        n, m, r = map(int, input().split())
        s = list(map(int, input().split()))
        b = list(map(int, input().split()))

        sm = min(s)
        sb = max(b)
        if sm < sb:
            print(r % sm + r // sm * sb)
        else:
            print(r)
    except:
        break
