# Автор: А. Кабанов
# Разбор: https://youtu.be/1sTNUjverpE

f = open('26-71.txt')
N, S = map(int, f.readline().split())
a = [list(map(int, f.readline().split())) for i in range(N)]
a.sort()

s = a[0][1]
k, count = 0, 0
mk, mt = 0, 0

for i in range(1,N):
    if a[i][0] == a[i-1][0]:
        s+=a[i][1]
        if s > S:
            k += 1
    else:
        s = a[i][1]
        count += k
        if k>mk:
            mk, mt = k, a[i-1][0]
        k = 0
print(count, mt)



