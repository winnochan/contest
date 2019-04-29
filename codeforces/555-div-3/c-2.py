#!/usr/bin/evn python
# -*- coding: utf-8 -*-
while True:
    try:
        n = int(input())
        a = list(map(int, input().strip().split()))
        o, t, l, r = [], 0, 0, len(a) - 1

        while l <= r and max(a[l], a[r]) > t:
            if a[l] > t and a[r] > t:
                if a[l] < a[r]:
                    t = a[l]
                    o.append('L')
                    l += 1
                elif a[r] < a[l]:
                    t = a[r]
                    o.append('R')
                    r -= 1
                else:
                    dl, dr = 0, 0
                    for i in range(l, r):
                        if a[i] < a[i + 1]:
                            dl += 1
                        else:
                            break

                    for i in range(r, l, -1):
                        if a[i] < a[i - 1]:
                            dr += 1
                        else:
                            break

                    if dl > dr:
                        t = a[l]
                        o.append('L')
                        l += 1
                    else:
                        t = a[r]
                        o.append('R')
                        r -= 1

            elif a[l] > t:
                t = a[l]
                o.append('L')
                l += 1
            elif a[r] > t:
                t = a[r]
                o.append('R')
                r -= 1

        # print(s)
        # print(o)
        print(len(o))
        print(''.join(o))

    except:
        break
