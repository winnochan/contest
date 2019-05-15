#!/usr/bin/env python
# -*- coding: utf-8 -*-
# while True:
#     try:
#         t = int(input())

#         for _ in range(t):
#             n = int(input())
#             d = list(map(int, input().split()))
#             d.sort()
#             m = d[0] * d[-1]
#             if len(d) >= 3:
#                 for i in range(1, len(d) - 1):
#                     if i > len(d) - 1 - i:
#                         break
#                     if d[i] * d[len(d) - 1 - i] != m:
#                         m = -1
#                         break
#             print(m)
#     except:
#         break
