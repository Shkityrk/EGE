# Автор: А. Кабанов
# Разбор: https://youtu.be/zeEo5jOMGmI

f = open('26-70.txt')
n = int(f.readline())
a = [int(x) for x in f]
a.sort()

s = 0
k = 0
for x in a:
    if x-s>1:
        print(s+1, k)
        break
    k+=1
    s+=x
