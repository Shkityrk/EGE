# Автор: А. Кабанов

f = open('26-76.txt')
L, M, N = map(int, f.readline().split())
a = [[int(x) for x in s.split()] for s in f]
a.sort()

count, m = 0, 0
if a[0][0] >= M:
    count+=1
    m = max(m, a[0][0])

for i in range(1,N):
    k = a[i][0]-a[i-1][1]
    if k>=M:
        count+=1
        m = max(m, k)

if L - a[N-1][1]>=M:
    count+=1
    m = max(m, L - a[N-1][1])

print(count,m)
