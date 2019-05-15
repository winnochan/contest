#!/usr/bin/evn python
# -*- coding: utf-8 -*-
while True:
    try:
        n, m = map(int, input().strip().split())

        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))

        ae, ao, be, bo = 0, 0, 0, 0

        for n in a:
            if n % 2 == 0:
                ae += 1
            else:
                ao += 1

        for n in b:
            if n % 2 == 0:
                be += 1
            else:
                bo += 1

        print(min(ae, bo) + min(ao, be))

    except:
        break
