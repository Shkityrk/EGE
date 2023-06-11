f=open('27-145b.txt')
n=int(f.readline())
k=int(f.readline())
a=[int(x) for x in f.readlines()]
k70=k71=k0=k1=0
count=0
for i in range(k,n):
    if a[i-k]%7==0 and a[i-k]%2==0:k70+=1
    if a[i - k] % 7 == 0 and a[i - k] % 2 != 0: k71 += 1
    if a[i - k] % 7 != 0 and a[i - k] % 2 == 0: k0 += 1
    if a[i - k] % 7 != 0 and a[i - k] % 2 != 0: k1 += 1

    if a[i]%7==0 and a[i]%2==0:count+=k70+k0
    if a[i] % 7 == 0 and a[i] % 2 != 0: count += k71 + k1
    if a[i] % 7 != 0 and a[i] % 2 == 0: count += k70
    if a[i] % 7 != 0 and a[i] % 2 != 0: count += k71
print(count)