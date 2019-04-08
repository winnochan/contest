#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
abcabc bcabc cabc abc bc c  -> 6
abcab bcab cab ab b         -> 3
abca bca ca a               -> 3
abc bc c                    -> 3
ab b                        -> 0
a                           -> 0

"""

while True:
    try:
        T = int(input())
        for _ in range(T):
            N = int(input())
            S, X = input().strip().split()
            l, a = 0, []
            for i in range(len(S)):
                if S[i] != X:
                    a.append(l)
                else:
                    l = i + 1
                    a.append(l)
            print(sum(a))
    except:
        break
