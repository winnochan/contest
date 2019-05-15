N, K = map(int, input().split())
A = list(map(int, input().split()))

# A = [(i, A[i]) for i in range(len(A))]

# def custom_cmp(a, b):
#     if a[0] == b[0]

# A.sort()

# B = []
# C = []

# for ai, i in A:
#     if not B:
#         B.append(i)
#     elif len(B) >= N:
#         C.append(i)
#     elif len(B) >= 3 and B[-1] - B[-3] == 2:
#         C.append(B[-1])
#         B[-1] = i
#     else:
#         B.append(i)

B, C, i = [], [], 0

while i < len(A) - 1:
    if len(B) == len(C):
        if A[i] < A[i + 1]:
            B.append(i)
            C.append(i + 1)
            i += 2
        elif A[i] > A[i + 1]:
            B.append(i + 1)
            C.append(i)
            i += 2
        else:
            find = 0
            for j in range(i + 2, i + K):
                if A[j] != A[i]:
                    find = j
                    break

# for i in range(len(A)):

print(A, B, C)
