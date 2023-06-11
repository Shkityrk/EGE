# Автор В.Н. Шубинкин

with open('27-156a.txt') as f:
    n, k, *a = map(int, f.read().split())

D = 131
s_min = 10**20
for i in range(n - k):
    s = 0
    for j in range(i, n):
        s += a[j]
        if s % D == 0 and j - i + 1 >= k:
            s_min = min(s_min, s)
print(abs(s_min))
