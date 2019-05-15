#!/usr/bin/evn python
# -*- coding: utf-8 -*-
import math


# from functools import reduce
def solution():
    n = int(input())
    a = list(map(int, input().split()))
    num1 = 0
    num2 = 0
    for num in a:
        if num == 1:
            num1 += 1
        else:
            num2 += 1

    p = list(range(200001))
    p[1] = 0
    l = math.floor(math.sqrt(200000)) + 1
    for i in range(2, l):
        if p[i]:
            k = 2 * i
            while k <= 200000:
                if p[k]:
                    p[k] = 0
                k += i

    np = []
    for i in range(1, 200001):
        if p[i]:
            np.append(i)

    last = 0
    r = []
    for i in range(len(np)):
        if num1 <= 0 and num2 <= 0:
            break

        total = np[i] - last

        if 2 * num2 + num1 <= total:
            for j in range(num2):
                r.append(2)
            for j in range(num1):
                r.append(1)
            break

        n2 = total // 2
        n1 = total % 2

        if n2 > num2:
            n1 += 2 * (n2 - num2)
            n2 = num2
            for j in range(n2):
                r.append(2)
            for j in range(n1):
                r.append(1)
            num1 -= n1
            num2 -= n2
            last = np[i]
            continue

        for j in range(n2):
            r.append(2)
        for j in range(n1):
            r.append(1)
        num1 -= n1
        num2 -= n2
        last = np[i]

    print(' '.join(map(str, r)))


while True:
    try:
        solution()

    except:
        break
# solution()
