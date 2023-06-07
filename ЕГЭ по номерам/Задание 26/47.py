f=open('data/26-47.txt')
n=int(f.readline())

a=[int(x) for x in f.readlines()]
b=sorted(set(a))

ans=[]

for i in range(n):
    for j in range(i+1,n):
        sr=(a[i]+a[j])//2
        k=0
        for m in range(len(b)):
            if b[m]<sr:k+=1
            else:
                if k%100==0:ans.append(k)
                break
print(len(ans), max(ans))