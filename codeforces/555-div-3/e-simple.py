#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import math


class TreeNode(object):
    def __init__(self, v, l=None, r=None, p=None) -> None:
        this.v = v
        this.l = l
        this.r = r
        this.p = p


class AVLTreeNode(TreeNode):
    def __init__(self, v, l=None, r=None) -> None:
        super(AVLTreeNode, self).__init__(v, l, r)


class RedBlackTreeNode(TreeNode):
    def __init__(self, v, c, l=None, r=None) -> None:
        super(RedBlackTreeNode, self).__init__(v, l, r)
        self.c = c

    def set_c(self, c):
        self.c = c


while True:
    try:
        n = int(input())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        c = [(n - a[i] % n) % n for i in range(n)]

        b.sort()

        table = OrderedDict()
        for num in b:
            table.setdefault(num, 0)
            table[num] += 1

        # for i in range(len(b)):
        #     num = b[i]
        #     table.setdefault(num, {'c': 0, 'n': 0, 'p': 0})
        #     node = table[num]
        #     node['c'] += 1
        #     nextIndex = (i + 1) % len(b)
        #     if b[nextIndex] != num:
        #         node['n'] = b[nextIndex]
        #         table.setdefault(b[nextIndex], {'c': 0, 'n': 0, 'p': 0})
        #         table[b[nextIndex]]['p'] = num

        print(a, b, c, table)

        # r = []
        # for num in c:
        #     if num in numMap and numMap[num] > 0:
        #         numMap[num] -= 1
        #         r.append((a[len(r)] + num) % n)
        #         continue

        #     find = 0
        #     for i in range(num + 1, n):
        #         if i in numMap and numMap[i] > 0:
        #             find = 1
        #             numMap[i] -= 1
        #             r.append((a[len(r)] + i) % n)
        #             break

        #     if find:
        #         continue

        #     for i in range(num):
        #         if i in numMap and numMap[i] > 0:
        #             numMap[i] -= 1
        #             r.append((a[len(r)] + i) % n)
        #             break

        # print(' '.join(map(str, r)))
    except:
        break
