# Автор В.Н. Шубинкин

with open('27-157a.txt') as f:
    n, k = map(int, f.readline().split())
    a = []
    for line in f.readlines():
        t, x = map(int, line.split())
        a.append([t, x])
max_s = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[j][0] - a[i][0] >= k and (a[i][1] + a[j][1]) % 2 == 0:
            max_s = max(max_s, a[i][1] + a[j][1])
print(max_s)
