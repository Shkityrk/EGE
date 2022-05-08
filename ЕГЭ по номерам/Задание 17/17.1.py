f = open("1.txt")
a = []
for s in f:
    a.append(int(s))
minsum = 200000
kol = 0
for i in range(0, len(a) - 1):
    if (a[i + 1] % 8 == 0 and a[i] % 18 != 0) or (a[i] % 8 == 0 and a[i + 1] % 18 != 0):
        kol += 1
        if (a[i] + a[i + 1]) < minsum:
            minsum = a[i] + a[i + 1]
print(kol, minsum)
