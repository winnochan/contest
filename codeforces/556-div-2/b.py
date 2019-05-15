#!/usr/bin/evn python
# -*- coding: utf-8 -*-
while True:
    try:
        n = int(input())
        b = [list(input()) for _ in range(n)]

        a = ((-1, 0), (1, 0), (0, 1), (0, -1))
        for r in range(1, n - 1):
            for c in range(1, n - 1):
                if b[r][c] == '.':
                    alldot = True
                    for ro, co in a:
                        if b[r + ro][c + co] != '.':
                            alldot = False
                            break

                    if alldot:
                        b[r][c] = '#'
                        for ro, co in a:
                            b[r + ro][c + co] = '#'

        allhash = True
        for r in range(n):
            for c in range(n):
                if b[r][c] == '.':
                    allhash = False
                    break
            if not allhash:
                break
        print('YES' if allhash else 'NO')

    except:
        break
