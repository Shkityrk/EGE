a = [int(x) for x in open('schelchok/9__1vf5f.txt')] #считываем элементы файла и добавляем их в список
k = 0 #количество пар
mx = -10000 #максимальная сумма


for i in range(len(a)): #i = 0, j = 1, 2, 3...n => i = 1, j = 2, 3, 4...n и так далее
    for j in range(i+1, len(a)):
        if ((a[i]+a[j]) % 134 == 0):
            k += 1
            mx = max(mx,a[i]+a[j])
print(k, mx)
