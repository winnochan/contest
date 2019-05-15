#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import math
while True:
    try:
        n = int(input())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        c = [(n - a[i] % n) % n for i in range(n)]

        segNum = math.floor(math.sqrt(n))
        segMap = {}
        numMap = {}

        for num in b:
            seg = num // segNum
            segMap.setdefault(seg, 0)
            numMap.setdefault(num, 0)
            segMap[seg] += 1
            numMap[num] += 1

        # print(a, b, c, segNum, segMap, numMap)

        r = []
        for num in c:
            if num in numMap and numMap[num] > 0:
                numMap[num] -= 1
                segMap[num // segNum] -= 1
                r.append((a[len(r)] + num) % n)
                continue

            isFind = 0
            findNum = 0
            for seg in range(num // segNum, (n - 1) // segNum + 1):
                if seg not in segMap or segMap[seg] <= 0:
                    continue

                for i in range(max(num + 1, seg * segNum), (seg + 1) * segNum):
                    if i in numMap and numMap[i] > 0:
                        isFind = 1
                        findNum = i
                        break

                if isFind:
                    break

            if isFind:
                numMap[findNum] -= 1
                segMap[findNum // segNum] -= 1
                r.append((a[len(r)] + findNum) % n)
                continue

            for seg in range(0, num // segNum + 1):
                if seg not in segMap or segMap[seg] <= 0:
                    continue

                for i in range(seg * segNum, min(num - 1, (seg + 1) * segNum)):
                    if i in numMap and numMap[i] > 0:
                        isFind = 1
                        findNum = i
                        break

                if isFind:
                    break

            if isFind:
                numMap[findNum] -= 1
                segMap[findNum // segNum] -= 1
                r.append((a[len(r)] + findNum) % n)
                continue

        print(' '.join(map(str, r)))
    except:
        break
