f = open('26-125.txt')
N, P = map(int,f.readline().split())
a = []
for i in range(N):
    time, mana = map(int, f.readline().split())
    if mana>1:
        a.append([time, mana // 2])
a.sort()

kotl = [0]*P
count = 0
mx = 0
for i in range(len(a)):
    time, kol = a[i]
    for j in range(P):
        if kotl[j]<=time:
            kotl[j] = time + kol if kotl[j] == 0 else time + kol + 2
            count += kol if kotl[j] <= 1440 else 1440 - time - 2
            mx = max(mx, kol if kotl[j] <= 1440 else 1440 - time - 2)
            break
print(count, mx)
