#!/usr/bin/evn python
# -*- coding: utf-8 -*-
while True:
    try:
        n = int(input())

        a = list(map(int, input().strip().split()))

        c, l, r = 0, 0, len(a) - 1
        s = []
        o = []

        while (not o or a[l] >= s[-1] or a[r] >= s[-1]) and l <= r:
            if not s:
                if a[l] < a[r]:
                    s.append(a[l])
                    o.append('L')
                    l += 1
                else:
                    s.append(a[r])
                    o.append('R')
                    r -= 1
            else:
                if a[l] < s[-1]:
                    s.append(a[r])
                    o.append('R')
                    r -= 1
                elif a[r] < s[-1]:
                    s.append(a[l])
                    o.append('L')
                    l += 1
                elif a[l] < a[r]:
                    s.append(a[l])
                    o.append('L')
                    l += 1
                else:
                    s.append(a[r])
                    o.append('R')
                    r -= 1

        # print(s)
        # print(o)
        print(len(o))
        print(''.join(o))

    except:
        break
