f=open('schelchok/10__1vf5g.txt')
a=[int(x) for x in f.readlines()]

k = 0 #количество пар
mn = 10000 #минимальная сумма


for i in range(len(a)): #i = 0, j = 1, 2, 3...n => i = 1, j = 2, 3, 4...n и так далее
    for j in range(i+1, len(a)):
        if ((a[i]-a[j]) % 2 == 0) and (a[i] % 11 == 0 or a[j] % 11 == 0):
            k += 1
            mn = min(mn,a[i]+a[j])
print(k, mn)