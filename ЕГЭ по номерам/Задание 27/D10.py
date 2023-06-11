f=open('files_compege/27B_2751.txt')
n=int(f.readline())
k=5
k131=k130=k0=k1=0
a=[int(x) for x in f.readlines()]
count=0

for i in range(k,n):
    if a[i-k]%13==0 and a[i-k]%2==0:k130+=1
    if a[i-k] % 13 == 0 and a[i-k] % 2 != 0: k131 += 1

    if a[i-k] % 13 != 0 and a[i-k] % 2 == 0: k0 += 1
    if a[i-k] % 13 != 0 and a[i-k] % 2 != 0: k1 += 1

    if a[i]%13==0 and a[i]%2==0:count+=k131+k1
    if a[i]%13==0 and a[i]%2!=0:count+=k130+k0
    if a[i] % 13 != 0 and a[i] % 2 == 0: count += k131
    if a[i] % 13 != 0 and a[i] % 2 != 0: count += k130
print(count)