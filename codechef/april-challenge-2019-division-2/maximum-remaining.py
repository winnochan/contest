#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    try:
        N = int(input())
        A = sorted(map(int, input().strip().split()))
        m, i = 0, len(A) - 2
        while i >= 0:
            if A[i] != A[-1]:
                m = A[i]
                break
            i -= 1
        print(m)
    except:
        break
