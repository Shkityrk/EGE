f=open('data/26-56.txt')
v,K,n=map(int, f.readline().split())
a=[int(x) for x in f.readlines()]
a.sort(reverse=True)

b= [0] * K
ost=[]

k=0
for i in range(n):
    for j in range(k, k + K):
        if b[j % K]+a[i]<=v:
            b[j % K]+=a[i]
            k= j + 1
            break
    else:ost.append(a[i])

print(sum(ost), len(ost))