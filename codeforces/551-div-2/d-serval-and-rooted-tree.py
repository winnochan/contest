#!/usr/bin/evn python
# -*- coding: utf-8 -*-
while True:
    try:
        n = int(input().strip())

        n, m, h = map(int, input().strip().split())
        f = list(map(int, input().strip().split()))
        l = list(map(int, input().strip().split()))
        t = [list(map(int, input().strip().split())) for _ in range(n)]

        for j in range(n):
            for k in range(m):
                if t[j][k] and f[k] > t[j][k]:
                    t[j][k] = min(f[k], l[j])

        for r in range(n):
            print(' '.join(map(str, t[r])))

    except:
        break
