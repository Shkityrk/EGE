# Автор В.Н. Шубинкин

with open('27-156b.txt') as f:
    n, k, *a = map(int, f.read().split())

D = 131
tail_sum = [-10**20]*D
tail_sum[0] = 0
s = sum(a[:k - 1])
s_prev = 0
s_min = 10**20
for i in range(k - 1, n):
    s += a[i]
    s_min = min(s_min, s - tail_sum[s % D])
    s_prev += a[i - k + 1]
    tail_sum[s_prev % D] = max(tail_sum[s_prev % D], s_prev)
print(abs(s_min))
