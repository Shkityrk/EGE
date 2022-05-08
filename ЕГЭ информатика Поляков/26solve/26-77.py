# Автор: А. Кабанов

f = open('26-77.txt')
n = int(f.readline())
a = [[0]*9 for i in range(2000)]
for i in range(n):
    year, t = map(int,f.readline().split())
    a[year][t] = 1

count = 0
m, my = 0, 0
for i in range(1961,1992):
    k = 0
    for j in range(1,9):
        if a[i][j]==0: k+=1
    count+=k
    if k>=m: m, my = k, i
print(count, my)
