n, m = map(int, input().split())

a = [list(input()) for _ in range(n)]

t = 0
for r in range(n):
    for c in range(m):
        if a[r][c] != 's':
            continue

        if c + 3 < m:
            s = ((r, c + 1), (r, c + 2), (r, c + 3))
            if a[s[0][0]][s[0][1]] == 'a' and a[s[1][0]][s[1][1]] == 'b' and a[
                    s[2][0]][s[2][1]] == 'a':
                t += 1

        if r + 3 < n:
            s = ((r + 1, c), (r + 2, c), (r + 3, c))
            if a[s[0][0]][s[0][1]] == 'a' and a[s[1][0]][s[1][1]] == 'b' and a[
                    s[2][0]][s[2][1]] == 'a':
                t += 1

        if c + 3 < m and r - 3 >= 0:
            s = ((r - 1, c + 1), (r - 2, c + 2), (r - 3, c + 3))
            if a[s[0][0]][s[0][1]] == 'a' and a[s[1][0]][s[1][1]] == 'b' and a[
                    s[2][0]][s[2][1]] == 'a':
                t += 1

        if c + 3 < m and r + 3 < n:
            s = ((r + 1, c + 1), (r + 2, c + 2), (r + 3, c + 3))
            if a[s[0][0]][s[0][1]] == 'a' and a[s[1][0]][s[1][1]] == 'b' and a[
                    s[2][0]][s[2][1]] == 'a':
                t += 1

print(t)
