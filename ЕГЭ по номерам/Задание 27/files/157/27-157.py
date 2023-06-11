# Автор В.Н. Шубинкин

with open('27-157b.txt') as f:
    n, k = map(int, f.readline().split())
    a = [0]*5000000
    for line in f.readlines():
        t, x = map(int, line.split())
        a[t] = x
max_x = [0, 0]
max_s = 0
for i in range(k, 5000000):
    r2_prev = a[i - k] % 2
    max_x[r2_prev] = max(max_x[r2_prev], a[i - k])
    r2 = a[i] % 2
    max_s = max(max_s, (a[i] + max_x[r2])*bool(max_x[r2])*bool(a[i]))
print(max_s)

# есть подвох: единственное чётное число в файле A
# больше суммы любых двух нечётных чисел
