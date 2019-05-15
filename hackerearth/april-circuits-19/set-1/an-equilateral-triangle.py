n = int(input())

a = [0] * n
if n >= 3:
    a = [0] * n
    a[1] = 1
    for i in range(2, n - 1):
        a[i] = (i + 1) * i // 2 + a[i - 2]

print(sum(a))
