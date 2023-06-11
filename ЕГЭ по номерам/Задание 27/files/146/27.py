f=open('27-146b.txt')
n=int(f.readline())
k=int(f.readline())
a=[int(x) for x in f.readlines()]

k41=[0]*120
k0=[0]*120

count=0

for i in range(k,n):
    if a[i-k]%41==0: k41[ a[i-k]%120 ]+=1
    else:k0[ a[i-k]%120 ]+=1

    ost2=0 if a[i]%120==0 else 120-a[i]%120

    if a[i]%41==0:count+=k0[ost2]
    if a[i] % 41 != 0: count += k41[ost2]
print(count)
